import daqmx.functions
import daqmx.constants
from config import NI_DEV_NAME, GAIN_CONTROL_N_SAMPLES, GAIN_CONTROL_SAMP_FREQ, GAIN_CONTROL_PIN_OUT

"""
Generation of the MPU Gain Voltage using the National Instruments (NI) Unit
"""

class GainControlLogicError(Exception):
    """
    Thrown if an inconsistency is noticed *before* any instructions are sent to the hardware (i.e. a problem with code logic)
    """
    pass

class GainVoltageGenerator(object):
    """
    Controls the Gain Voltage of the MPU's PMT, as produced by the NI Unit via commands sent down a USB port.
    """
    def __init__(self):
        """
        There is a residual voltage of 0.0044V always present in the MPU's PMT.
        The NI Unit should be initialised with a zero voltage output ... note that this means that the total Gain Voltage at the PMT will be equal to the residual voltage, but there's nothing we can do about that (we would need the NI Unit to output a negative voltage in order for the Gain Voltage at PMT to be truly zero!).
        """    
        self.dev_name = NI_DEV_NAME
        self.out_pin = GAIN_CONTROL_PIN_OUT
        self.number_of_samples = GAIN_CONTROL_N_SAMPLES
        self.sampling_frequency = GAIN_CONTROL_SAMP_FREQ
        self.vResidual = 0.0044
        self._set_up()
        self._start_output(0)

    def generate_voltage(self, vGain):
        """
        Generate the Gain Voltage as exactly requested by the user, and which would be found on measuring the gain voltage *at the MPU's PMT itself*.
        This voltage (vGain) = the residual voltage on the PMT (vResidual) + some required voltage output from the NI Unit (vOutput).
        First, set up the output task (_set_up) and then output vOutput (_start_output) through one of the NI Unit's analogue output (ao) pins.

        :param vGain: requested Gain Voltage

        :raises: :class:`.GainControlLogicError` if the requested Gain Voltage is outside the safe range for the MPU's PMT
        """
        if(vGain < 0.5 or vGain > 1.0):
            raise GainControlLogicError("Cannot set Gain Voltage - must be between 0.5 and 1.0V to avoid damage to the MPU's PMT")
        self._set_up()
        vOutput = vGain - self.vResidual
        try:
            self._start_output(vOutput)
            self.voltage = vOutput
        finally:
            self._stop_output()

    def _set_up(self):
        """
        Create the Gain Voltage task, and set up a generic voltage with a minimum and maximum value, and the analogue output channel X to be used.
        The channel string must be of the form `deviceName/analogueOutputPin`, i.e. `Dev1/ao0`.  /ao0 is used by default, but can be changed in config.py if required.
        This is a private function, indicated by the underscore before the name - do not change that!
        """
        self.taskHandle = functions.TaskHandle(0)
        functions.DAQmxCreateTask("",byref(self.taskHandle))
        self.vMin = 0.0
        self.vMax = 1.0
        functions.DAQmxCreateAOVoltageChan(self.taskHandle, self.dev_name + self.out_pin, "", self.vMin, self.vMax, constants.DAQmx_Val_Volts, None)
        functions.DAQmxCfgSampClkTiming(self.taskHandle, "", self.sampling_frequency, constants.DAQmx_Val_Rising, constants.DAQmx_Val_ContSamps, self.number_of_samples)

    def _start_output(self, voltage):
        """
        Start the Gain Voltage task using the parameters previously set up in the _set_up function, and a given output voltage
        This is a private function, indicated by the underscore before the name - do not change that!
        """
        data = np.zeros(3000, dtype = numpy.float64)
        for i in range(len(data)):
            data[i] = voltage
        functions.DAQmxWriteAnalogF64(self.taskHandle, 3000, 0, 10.0, constants, DAQmx_Val_GroupByChannel, data, None, None)
        functions.DAQmxStartTask(self.taskHandle)

    def _stop_output(self):
        """
        Stop the Gain Voltage task and clear the NI Unit's task memory
        This is a private function, indicated by the underscore before the name - do not change that!
        """
        functions.DAQmxStopTask(self.taskHandle)
        #data = np.zeros(3000, dtype = numpy.float64)
        #functions.DAQmxWriteAnalogF64(self.taskHandle, 3000, 0, 10.0, DAQmx_Val_GroupByChannel, data, None, None)
        functions.DAQmxClearTask(self.taskHandle)
    
    def current_state(self):
        """
        Return a formatted string with the current hardware settings
        """
        return """Output Voltage : {0}""".format(self.voltage)

    def go_safe(self):
        """
        Set the gain voltage to its safe value: 0V (i.e. the Gain Voltage at the PMT is = only the residual voltage)
        """
        self._start_output(0)
