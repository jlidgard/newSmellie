import daqmx.functions
import daqmx.constants
from smellie_config import NI_DEV_NAME, TRIG_GEN_PIN_OUT_SUPERK, TRIG_GEN_PIN_OUT_PQ, TRIG_GEN_HIGH_TIME, TRIG_GEN_FREQUENCY, TRIG_GEN_MINIMUM_LOW_TIME
from ctypes import byref

"""
Generation of the SEPIA and SuperK trigger signals using the National Instruments (NI) Unit
"""

class NITriggerGeneratorError(Exception):
    """
    Thrown if an inconsistency is noticed *before* any instructions are sent to the hardware (i.e. a problem with code logic)
    """
    pass

class TriggerGenerator(object):
    """
    Controls the SEPIA and SuperK trigger signals, as produced by the NI Unit via commands sent down a USB port.
    """
    
    def __init__(self, trigger_channel):
        """
        Select and initiate which channel to send triggers
        
        : takes either "SUPERK" or "PQ" (string) and initiates appropriate channel as set in smellie_config.py
        """
        if (trigger_channel=="SUPERK" or trigger_channel=="PQ"): self.trigger_channel = trigger_channel
        else:
            raise NITriggerGeneratorError("Must select either 'SUPERK' or 'PQ' to initiate trigger channel")

        self._setup()
        
    
    def _setup(self):
        """
        Set up the single-pulse parameters - the high time and the low time, and the digital output channel X to be used.
        The channel string must be of the form `deviceName/digitalOutputPin`, i.e. `Dev1/Ctr0`.  /Ctr0 is used by default, but can be changed in smellie_config.py if required.
        """
        self.taskHandle = daqmx.functions.TaskHandle(0)
        self.high_time = TRIG_GEN_HIGH_TIME
        self.frequency = TRIG_GEN_FREQUENCY
        self.low_time = (1.0 / self.frequency) - self.high_time
        if (self.low_time < TRIG_GEN_MINIMUM_LOW_TIME): self.low_time = TRIG_GEN_MINIMUM_LOW_TIME
        self.dev_name = NI_DEV_NAME
        if (self.trigger_channel=="SUPERK"): self.out_pin = TRIG_GEN_PIN_OUT_SUPERK
        elif (self.trigger_channel=="PQ"): self.out_pin = TRIG_GEN_PIN_OUT_PQ
        
        daqmx.functions.DAQmxCreateTask("", byref(self.taskHandle))
        daqmx.functions.DAQmxCreateCOPulseChanTime(self.taskHandle, self.dev_name + self.out_pin, "", daqmx.constants.DAQmx_Val_Seconds, daqmx.constants.DAQmx_Val_Low, 0.0, self.low_time, self.high_time)

    def _cleanup(self):
        """
        Wait until all n trigger pulses have been sent, and then stop the Trigger Generation task and clear the NI Unit's task memory.
        Timeout set to (number of pulses + 0.1%) / frequency 
        """
        timeout = (self.n_pulses*1.001)/self.frequency
        daqmx.functions.DAQmxWaitUntilTaskDone(self.taskHandle, timeout)
        daqmx.functions.DAQmxStopTask(self.taskHandle)
        daqmx.functions.DAQmxClearTask(self.taskHandle)

    def generate_triggers(self, n_pulses):
        """
        Start the Trigger Generation task using the single-pulse parameters previously set up in the __enter__ function, and the requested number of pulses

        :param n_pulses:
        """
        try:
            self.n_pulses = n_pulses
            daqmx.functions.DAQmxCfgImplicitTiming(self.taskHandle, daqmx.constants.DAQmx_Val_FiniteSamps, self.n_pulses)
            daqmx.functions.DAQmxStartTask(self.taskHandle)

        finally:
            self._cleanup()
