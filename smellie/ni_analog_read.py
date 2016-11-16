import daqmx.functions
import daqmx.constants
from smellie_config import NI_DEV_NAME, MPU_SAMPLE_N_SAMPLES, MPU_SAMPLE_SAMP_FREQ, MPU_SAMPLE_PIN_IN
import ctypes,numpy,time

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
    Reads an analog input channel on the NI Unit.
    """
    def __init__(self, vMin=0, vMax=5, in_pin='/ai1'):
        """
        undocumented
        """
        self.dev_name = NI_DEV_NAME
        self._set_up(vMin, vMax, in_pin)

    def __del__(self):
        """
        undocumented
        """
        daqmx.functions.DAQmxClearTask(self.taskHandle)

    def read_voltage_mean(self, number_of_samples=100000, sampling_frequency=100000):
        """
        Generate the Gain Voltage as exactly requested by the user, and which would be found on measuring the gain voltage *at the MPU's PMT itself*.
        This voltage (vGain) = the residual voltage on the PMT (vResidual) + some required voltage output from the NI Unit (vOutput).
        First, set up the output task (_set_up) and then output vOutput (_start_read) through one of the NI Unit's analogue output (ao) pins.

        :param vGain: requested Gain Voltage

        :raises: :class:`.AnalogReadLogicError` if the requested Gain Voltage is outside the safe range for the MPU's PMT
        """
        voltages = self._start_read(number_of_samples, sampling_frequency)
        voltages_max = numpy.amax(voltages)
        voltages_high = voltages[ numpy.where( voltages > voltages_max*0.7 ) ]
        voltages_mean = numpy.mean(voltages_high)
        voltages_sd = numpy.std(voltages_high)
        return voltages_mean, voltages_sd

    def read_voltage(self, number_of_samples=100000, sampling_frequency=100000):
        """
        Generate the Gain Voltage as exactly requested by the user, and which would be found on measuring the gain voltage *at the MPU's PMT itself*.
        This voltage (vGain) = the residual voltage on the PMT (vResidual) + some required voltage output from the NI Unit (vOutput).
        First, set up the output task (_set_up) and then output vOutput (_start_read) through one of the NI Unit's analogue output (ao) pins.

        :param vGain: requested Gain Voltage

        :raises: :class:`.AnalogReadLogicError` if the requested Gain Voltage is outside the safe range for the MPU's PMT
        """
        voltages = self._start_read(number_of_samples, sampling_frequency)
        return voltages

    def _set_up(self, vMin, vMax, in_pin):
        """
        Create the Gain Voltage task, the channel minimum and maximum parameters, the physical output channel.
        """
        self.taskHandle = daqmx.functions.TaskHandle(0)
        daqmx.functions.DAQmxCreateTask("",ctypes.byref(self.taskHandle))
        
        daqmx.functions.DAQmxCreateAIVoltageChan(self.taskHandle, self.dev_name + in_pin, "", daqmx.constants.DAQmx_Val_Diff, ctypes.c_double(vMin), ctypes.c_double(vMax), daqmx.constants.DAQmx_Val_Volts, None)

    def _start_read(self, number_of_samples, sampling_frequency):
        """
        Start the Gain Voltage task using the parameters previously set up in the _set_up function, and a given output voltage
        This is a private function, indicated by the underscore before the name - do not change that!
        """

        daqmx.functions.DAQmxCfgSampClkTiming(self.taskHandle, "", sampling_frequency, daqmx.constants.DAQmx_Val_Rising,daqmx.constants.DAQmx_Val_FiniteSamps, number_of_samples)
        
        samples_read_n = ctypes.c_int()
        samples_read = numpy.zeros((number_of_samples,), dtype=numpy.float64)
        timeout = (number_of_samples/sampling_frequency)*1.1 #timeout 10% more than the nsamples/sample rate
        
        daqmx.functions.DAQmxStartTask(self.taskHandle)
        time.sleep(0.5) #wait for task to start (otherwise errors)

        daqmx.functions.DAQmxReadAnalogF64(self.taskHandle, ctypes.c_int(number_of_samples), ctypes.c_double(timeout), daqmx.constants.DAQmx_Val_GroupByChannel, samples_read, ctypes.c_uint(number_of_samples), ctypes.byref(samples_read_n), None)
        
        daqmx.functions.DAQmxWaitUntilTaskDone(self.taskHandle,timeout) #not sure if the second argument in here is correct ?
        
        daqmx.functions.DAQmxStopTask(self.taskHandle)
        
        if (samples_read_n.value!=number_of_samples):
            raise AnalogReadLogicError("Could not read the specified number of samples from NI AI channel.")

        return samples_read
