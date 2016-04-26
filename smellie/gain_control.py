import daqmx.fuctions
import daqmx.constants
from config import GAIN_CONTROL_N_SAMPLES, GAIN_CONTROL_SAMP_FREQ
class GainContolLogicError(Exception):
    pass

class GainVoltageGenerator(object):
    def __enter__(self)
        taskHandle = TaskHandle(0)
        DAQmxCreateTask("",byref(taskHandle))
        self.number_of_samples = GAIN_CONTROL_N_SAMPLES

        self.sampling_frequency = GAIN_CONTROL_SAMP_FREQ
        self.taskHandle = taskHandle
        #not in use below for testing purposes. Forced with "Dev1/ao1" argument.
        vMin = 0.0
        vMax = 1.0
        vRes = 0.0044 # Residual voltage on MPU
        functions.DAQmxCreateAOVoltageChan(self.taskHandle, "Dev1/ao0", "",
                                           vMin, vMax, 
                                           constants.DAQmx_Val_Volts,
                                           None)
        DAQmxCfgSampClkTiming(self.taskHandle, "", 
                              self.sampling_frequency,
                              constants.DAQmx_Val_Rising,
                              constants.DAQmx_Val_ContSamps,
                              self.number_of_samples)

    def set_voltage(self, voltage):
        # FIXME: 0.1 or 0.0124????
        if(voltage > 1.0 or voltage < 0.0124):
            raise  GainControlLogicError("Gain voltage must be set between 0.1V and 1.0V to avoid damage to MPU")

        #Creating and shaping the data buffer:
        self.data = np.zeros(3000, dtype = numpy.float64)
        data_length = self.data.shape[0]

        for i in range(0, data_length):
            self.data[i]= vGain - vRes
            functions.DAQmxWriteAnalogF64(self.taskHandle, 
                                          3000, 0, 10.0,
                                          constants,
                                          DAQmx_Val_GroupByChannel, 
                                          data, None, None)

        DAQmxStartTask(self.taskHandle)

    def __exit__(self):
        functions.DAQmxStopTask(self.taskHandle)
        data = np.zeros(3000, dtype = numpy.float64)
        data_length = data.shape[0]
        for i in range(0, data_length):
            data[i]= 0.0
        functions.DAQmxWriteAnalogF64(self.taskHandle,
                                      3000, 0, 10.0,
                                      DAQmx_Val_GroupByChannel, 
                                      data, None, None)

        functions.DAQmxClearTask(self.taskHandle)

