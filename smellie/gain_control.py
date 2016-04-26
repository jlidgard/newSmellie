import daqmx.fuctions
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
        aoDetails = str(devName + analogueOutputPin)
        #not in use below\ for testing purposes. Forced with "Dev1/ao1" argument.
        vMin = 0.0
        vMax = 1.0
        vRes = 0.0044 # Residual voltage on MPU
        if(vGain > 1.0 or vGain < 0.0124):
            raise  GainControlLogicError("Gain voltage must be set between 0.1V and 1.0V to avoid damage to MPU")

        DAQmxCreateAOVoltageChan(taskHandle,"Dev1/ao0","",vMin,vMax,D\
AQmx_Val_Volts,None)
        DAQmxCfgSampClkTiming(taskHandle,"",sampling_frequency,DAQmx_\
Val_Rising,DAQmx_Val_ContSamps,self.number_of_samples)

    def set_voltage(self):
        #Creating and shaping the data buffer:
        self.data = np.zeros(3000, dtype = numpy.float64)
        data_length = self.data.shape[0]

        for i in range(0, data_length):
            self.data[i]= vGain - vRes
        DAQmxWriteAnalogF64(self.taskHandle,3000,0,10.0,DAQmx_Val_Gro\
upByChannel,data,None,None)

        DAQmxStartTask(self.taskHandle)

    def __exit__(self):
        DAQmxStopTask(self.taskHandle)
        data = np.zeros(3000, dtype = numpy.float64)
        data_length = data.shape[0]
        for i in range(0, data_length):
            data[i]= 0.0
        DAQmxWriteAnalogF64(self.taskHandle,3000,0,10.0,DAQmx_Val_Gro\
                                upByChannel,data,None,None)

        DAQmxClearTask(self.taskHandle)

