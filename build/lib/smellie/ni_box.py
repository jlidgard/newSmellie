import daqmx.functions
import daqmx.constants
from config import NI_HIGH_TIME, NI_FREQUENCY, NI_MINIMUM_LOW_TIME
class TriggerGenerator(object):
    def __enter__(self):
        self.high_time = NI_HIGH_TIME
        self.frequency = NI_FREQUENCY
        self.low_time  = 1./self.frequency - self.high_time
        if self.low_time < NI_MINIMUM_LOW_TIME:
            self.low_time = NI_MINIMUM_LOW_TIME

        self.dev_name = "Dev1"
        self.trig_out_pin = "/Ctr0"

        self.task_handle = functions.TaskHandle(0)
        functions.DAQmxCreateTask("", byref(self.task_handle))
        fuctions.DAQmxCreateCOPulseChanTime(self.task_handle, 
                                            devName + self.trig_out_pin,
                                            "",
                                            constants.DAQmx_Val_seconds,
                                            constants.DAQmx_Val_Low,
                                            0.0,
                                            self.low_time,
                                            self.high_time
                                            )
    def __exit__(self):
        # second argument needs checking
        functions.DAQmxWaitUntillTaskDone(self.task_handle, -1)
        functions.DAQmxStopTask(self.task_handle)
        functions.DAQmxClearTask(self.task_handle)

    def generate(self, n_pulses):
        functions.DaqmxCdfImplicitTiming(taskHandle, 
                                         constants.DAQmx_Val_FiniteSamps,
                                         n_pulses
                                        )
        functions.DAQmxStartTask(self.task_handle)
                                        
