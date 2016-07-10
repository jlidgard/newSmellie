import daqmx.functions
import daqmx.constants
from config import GAIN_CONTROL_N_SAMPLES, GAIN_CONTROL_SAMP_FREQ
class GainContolLogicError(Exception):
    pass

class GainVoltageGenerator(object):
    def __init__(self):
        self.number_of_samples  = GAIN_CONTROL_N_SAMPLES
        self.sampling_frequency = GAIN_CONTROL_SAMP_FREQ
        set_voltage(0)

    def set_voltage(self, voltage):
        self._set_up()
        try:
            self._set_voltage(voltage)
            self.voltage = voltage
        finally:
            self._clear_up()

    def _set_up(self):
        self.taskHandle = TaskHandle(0)
        functions.DAQmxCreateTask("",byref(self.taskHandle))

        # not in use below for testing purposes. 
        # Forced with "Dev1/ao1" argument.
        self.vMin = 0.0
        self.vMax = 1.0
        self.vRes = 0.0044 # Residual voltage on MPU
        functions.DAQmxCreateAOVoltageChan(self.taskHandle, "Dev1/ao0", "",
                                           self.vMin, self.vMax, 
                                           constants.DAQmx_Val_Volts,
                                           None)

        functions.DAQmxCfgSampClkTiming(self.taskHandle, "", 
                                        self.sampling_frequency,
                                        constants.DAQmx_Val_Rising,
                                        constants.DAQmx_Val_ContSamps,
                                        self.number_of_samples)

    def _set_voltage(self, voltage):
        # FIXME: 0.1 or 0.0124????
        if(voltage > 1.0 or voltage < 0.0124):
            raise  GainControlLogicError("Gain voltage must be set between 0.1V and 1.0V to avoid damage to MPU")

        #Creating and shaping the data buffer:
        data = np.zeros(3000, dtype = numpy.float64)

        for i in range(len(data)):
            data[i]= voltage - self.vRes

        functions.DAQmxWriteAnalogF64(self.taskHandle, 
                                      3000, 0, 10.0,
                                      constants,
                                      DAQmx_Val_GroupByChannel, 
                                      data, None, None)

        functions.DAQmxStartTask(self.taskHandle)

    def _clear_up(self):
        functions.DAQmxStopTask(self.taskHandle)
        data = np.zeros(3000, dtype = numpy.float64)
        functions.DAQmxWriteAnalogF64(self.taskHandle,
                                      3000, 0, 10.0,
                                      DAQmx_Val_GroupByChannel, 
                                      data, None, None)

        functions.DAQmxClearTask(self.taskHandle)
    
    def current_state(self):
        return "Gain Voltage : {0}".format(self.voltage)

    def go_safe(self):
        self.set_voltage(0)


