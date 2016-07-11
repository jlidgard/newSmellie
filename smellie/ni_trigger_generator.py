import daqmx.functions
import daqmx.constants
from config import NI_DEV_NAME, TRIG_GEN_PIN_OUT, TRIG_GEN_HIGH_TIME, TRIG_GEN_FREQUENCY, TRIG_GEN_MINIMUM_LOW_TIME

"""
Generation of the SEPIA and SuperK trigger signals using the National Instruments (NI) Unit
"""

class TriggerGenerator(object):
    """
    Controls the SEPIA and SuperK trigger signals, as produced by the NI Unit via commands sent down a USB port.
    """
    def __enter__(self):
        """
        Set up the single-pulse parameters - the high time and the low time, and the digital output channel X to be used.
        The channel string must be of the form `deviceName/digitalOutputPin`, i.e. `Dev1/Ctr0`.  /Ctr0 is used by default, but can be changed in config.py if required.
        """
        self.high_time = NI_HIGH_TIME
        self.frequency = NI_FREQUENCY
        self.low_time = (1.0 / self.frequency) - self.high_time
        if self.low_time < NI_MINIMUM_LOW_TIME:
            self.low_time = NI_MINIMUM_LOW_TIME
        self.dev_name = NI_DEV_NAME
        self.out_pin = TRIG_GEN_PIN_OUT

        self.taskHandle = functions.TaskHandle(0)
        functions.DAQmxCreateTask("", byref(self.taskHandle))
        functions.DAQmxCreateCOPulseChanTime(self.taskHandle, devName + self.trig_out_pin, "", constants.DAQmx_Val_seconds, constants.DAQmx_Val_Low, 0.0, self.low_time, self.high_time)

    def __exit__(self):
        """
        Wait until all n trigger pulses have been sent, and then stop the Trigger Generation task and clear the NI Unit's task memory.
        """
        functions.DAQmxWaitUntillTaskDone(self.taskHandle, -1) # second argument needs checking
        functions.DAQmxStopTask(self.taskHandle)
        functions.DAQmxClearTask(self.taskHandle)

    def generate_triggers(self, n_pulses):
        """
        Start the Trigger Generation task using the single-pulse parameters previously set up in the __enter__ function, and the requested number of pulses
        """
        functions.DaqmxCdfImplicitTiming(taskHandle, constants.DAQmx_Val_FiniteSamps, n_pulses)
        functions.DAQmxStartTask(self.taskHandle)
