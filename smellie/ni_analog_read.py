import daqmx.functions
import daqmx.constants
from smellie_config import NI_DEV_NAME, MPU_SAMPLE_N_SAMPLES, MPU_SAMPLE_SAMP_FREQ, MPU_SAMPLE_PIN_IN
import ctypes
import numpy

"""
Generation of the MPU Gain Voltage using the National Instruments (NI) Unit
"""

class AnalogReadLogicError(Exception):
    """
    Thrown if an inconsistency is noticed *before* any instructions are sent to the hardware (i.e. a problem with code logic)
    """
    pass

class AnalogRead(object):
    """
    Controls the Gain Voltage of the MPU's PMT, as produced by the NI Unit via commands sent down a USB port.
    """
    def __init__(self):
        """
        There is a residual voltage of 0.0044V always present in the MPU's PMT.
        The NI Unit should be initialised with a zero voltage output ... note that this means that the total Gain Voltage at the PMT will be equal to the residual voltage, but there's nothing we can do about that (we would need the NI Unit to output a negative voltage in order for the Gain Voltage at PMT to be truly zero!).
        """
        self.dev_name = NI_DEV_NAME
        self.in_pin = MPU_SAMPLE_PIN_IN
        self.number_of_samples = MPU_SAMPLE_N_SAMPLES
        self.sampling_frequency = MPU_SAMPLE_SAMP_FREQ
        self._set_up()
        self._start_read()

    def read_voltage(self):
        """
        Generate the Gain Voltage as exactly requested by the user, and which would be found on measuring the gain voltage *at the MPU's PMT itself*.
        This voltage (vGain) = the residual voltage on the PMT (vResidual) + some required voltage output from the NI Unit (vOutput).
        First, set up the output task (_set_up) and then output vOutput (_start_read) through one of the NI Unit's analogue output (ao) pins.

        :param vGain: requested Gain Voltage

        :raises: :class:`.AnalogReadLogicError` if the requested Gain Voltage is outside the safe range for the MPU's PMT
        """
        self._set_up()
        voltages = self._start_read()
        voltages_max = numpy.amax(voltages)
        voltages_high = voltages[ numpy.where( voltages > voltages_max*0.7 ) ]
        voltages_mean = numpy.mean(voltages_high)
        voltages_sd = numpy.std(voltages_high)
        print voltages_max, voltages_mean, voltages_sd
        return voltages_mean, voltages_sd

    def _set_up(self):
        """
        Create the Gain Voltage task, the channel minimum (0V) and maximum parameters (5V) , the physical output channel and set the internal timing trigger.
        """
        self.taskHandle = daqmx.functions.TaskHandle(0)
        daqmx.functions.DAQmxCreateTask("",ctypes.byref(self.taskHandle))
        
        self.vMin = ctypes.c_double(0.0)
        self.vMax = ctypes.c_double(5.0)
        
        daqmx.functions.DAQmxCreateAIVoltageChan(self.taskHandle, self.dev_name + self.in_pin, "", daqmx.constants.DAQmx_Val_Diff, self.vMin, self.vMax, daqmx.constants.DAQmx_Val_Volts, None)
        daqmx.functions.DAQmxCfgSampClkTiming(self.taskHandle, "", self.sampling_frequency, daqmx.constants.DAQmx_Val_Rising,daqmx.constants.DAQmx_Val_FiniteSamps, self.number_of_samples)

    def _start_read(self):
        """
        Start the Gain Voltage task using the parameters previously set up in the _set_up function, and a given output voltage
        This is a private function, indicated by the underscore before the name - do not change that!
        """
        samples_read_n = ctypes.c_int()
        samples_read = numpy.zeros((self.number_of_samples,), dtype=numpy.float64)
        timeout = (self.number_of_samples/self.sampling_frequency)*1.1 #timeout 10% more than the nsamples/sample rate
        daqmx.functions.DAQmxStartTask(self.taskHandle)

        daqmx.functions.DAQmxReadAnalogF64(self.taskHandle, ctypes.c_int(self.number_of_samples), ctypes.c_double(timeout), daqmx.constants.DAQmx_Val_GroupByChannel, samples_read, ctypes.c_uint(self.number_of_samples), ctypes.byref(samples_read_n), None)
        daqmx.functions.DAQmxStopTask(self.taskHandle)
        
        if (samples_read_n.value!=self.number_of_samples):
            raise AnalogReadLogicError("Could not read the specified number of samples from NI AI channel.")

        return samples_read

    def go_safe(self):
        """
        Set the gain voltage to its safe value: 0V (i.e. the Gain Voltage at the PMT is = only the residual voltage)
        """
        self._start_read()
