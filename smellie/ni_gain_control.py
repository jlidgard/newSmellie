import daqmx.functions
import daqmx.constants
from smellie_config import NI_DEV_NAME, GAIN_CONTROL_N_SAMPLES, GAIN_CONTROL_SAMP_FREQ, GAIN_CONTROL_PIN_OUT, GAIN_CONTROL_VOLTAGE_OFFSET
import ctypes
import numpy

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
        self.vResidual = GAIN_CONTROL_VOLTAGE_OFFSET
        self._set_up()
        self._start_output(0) # why is the gain always changed? why don't we leave it where it is?
        self.voltage = None

    def generate_voltage(self, vGain):
        """
        Generate the Gain Voltage as exactly requested by the user, and which would be found on measuring the gain voltage *at the MPU's PMT itself*.
        This voltage (vGain) = the residual voltage on the PMT (vResidual) + some required voltage output from the NI Unit (vOutput).
        First, set up the output task (_set_up) and then output vOutput (_start_output) through one of the NI Unit's analogue output (ao) pins.

        :param vGain: requested Gain Voltage

        :raises: :class:`.GainControlLogicError` if the requested Gain Voltage is outside the safe range for the MPU's PMT
        """
        if(vGain < 0.0 or vGain > 1.0):
            raise GainControlLogicError("Cannot set Gain Voltage - must be between 0.5 and 1.0V to avoid damage to the MPU's PMT")
        self._set_up()
        vOutput = vGain - self.vResidual
        self._start_output(vOutput)
        self.voltage = vOutput

    def _set_up(self):
        """
        Create the Gain Voltage task, and set up a generic voltage with a minimum and maximum value, and the analogue output channel X to be used.
        The channel string must be of the form `deviceName/analogueOutputPin`, i.e. `Dev1/ao0`.  /ao0 is used by default, but can be changed in config.py if required.
        This is a private function, indicated by the underscore before the name - do not change that!
        """
        self.taskHandle = daqmx.functions.TaskHandle(0)
        daqmx.functions.DAQmxCreateTask("",ctypes.byref(self.taskHandle)) #write task
        
        self.vMin = ctypes.c_double(0.0)
        self.vMax = ctypes.c_double(1.0)
        
        #int32 DAQmxCreateAOVoltageChan(TaskHandle taskHandle, const char physicalChannel[], const char nameToAssignToChannel[], float64 minVal, float64 maxVal, int32 units, const char customScaleName[]);
        daqmx.functions.DAQmxCreateAOVoltageChan(self.taskHandle, self.dev_name + self.out_pin, "", self.vMin, self.vMax, daqmx.constants.DAQmx_Val_Volts, None)

    def _start_output(self, voltage):
        """
        Start the Gain Voltage task using the parameters previously set up in the _set_up function, and a given output voltage
        This is a private function, indicated by the underscore before the name - do not change that!
        """
        data = numpy.array([[float(voltage)]],numpy.float64)
        samples_written = ctypes.c_int(-1)
        daqmx.functions.DAQmxStartTask(self.taskHandle)
        #DAQmx.h: int32 DAQmxWriteAnalogF64(TaskHandle taskHandle, int32 numSampsPerChan, bool32 autoStart, float64 timeout, bool32 dataLayout, float64 writeArray[], int32 *samsPerChanWritten, bool32 *reserved);
        daqmx.functions.DAQmxWriteAnalogF64(self.taskHandle, ctypes.c_int(1), ctypes.c_uint(0), ctypes.c_double(0.001), daqmx.constants.DAQmx_Val_GroupByChannel, data, ctypes.byref(samples_written), None)
        daqmx.functions.DAQmxStopTask(self.taskHandle)
        
        if (samples_written.value!=1):
            raise GainControlLogicError("Could not write gain voltage to NI AO channel.")

    def __del__(self):
        """
        Stop the Gain Voltage task and clear the NI Unit's task memory
        This is a private function, indicated by the underscore before the name - do not change that!
        """
        #self._start_output(0)
        #daqmx.functions.DAQmxClearTask(self.taskHandle)
        pass
        
    def check_voltage(self):
        """
        Read the voltage on the DAQ pin to see if it has been correctly set.
        """
        self.taskHandle2 = daqmx.functions.TaskHandle(0) #read handle
        daqmx.functions.DAQmxCreateTask("",ctypes.byref(self.taskHandle2))  #read task
        
        data = numpy.ndarray(shape=(self.number_of_samples),dtype=numpy.float64)
        samples_read = ctypes.c_int32(-1)
        
        #tried to move these functions to _setup but was getting many task related errors.
        daqmx.functions.DAQmxCreateAIVoltageChan(self.taskHandle2, self.dev_name + "/_ao0_vs_aognd", "", daqmx.constants.DAQmx_Val_Diff, self.vMin, self.vMax, daqmx.constants.DAQmx_Val_Volts, None)
        daqmx.functions.DAQmxCfgSampClkTiming(self.taskHandle2,"",ctypes.c_double(self.sampling_frequency),daqmx.constants.DAQmx_Val_Rising,daqmx.constants.DAQmx_Val_FiniteSamps,ctypes.c_uint64(self.number_of_samples) )

        daqmx.functions.DAQmxStartTask(self.taskHandle2)
        #int32 DAQmxReadAnalogF64(TaskHandle taskHandle, int32 numSampsPerChan, float64 timeout, bool32 fillMode, float64 readArray[], uInt32 arraySizeInSampl,s int32 *sampsPerChanRead *reserved);
        daqmx.functions.DAQmxReadAnalogF64(self.taskHandle2, ctypes.c_int(self.number_of_samples), ctypes.c_double((self.number_of_samples*1.001)/self.sampling_frequency), daqmx.constants.DAQmx_Val_GroupByChannel, data, ctypes.c_uint32(self.number_of_samples),ctypes.byref(samples_read), None)
        daqmx.functions.DAQmxWaitUntilTaskDone(self.taskHandle2, 1)
        daqmx.functions.DAQmxStopTask(self.taskHandle2)
        daqmx.functions.DAQmxClearTask(self.taskHandle2)

        data_mean = data.mean()
        if (samples_read.value!=self.number_of_samples): raise GainControlLogicError("Could not correctly check gain voltage, failed reading NI AO channel.")
        if (samples_read.value>=data_mean*0.9999 and samples_read.value<=data_mean*1.0001): raise GainControlLogicError("Gain voltage not correctly set to specified value.")  
        
    def current_state(self):
        """
        Return a formatted string with the current hardware settings
        """
        return "NI gain control (settings):: Output Voltage : {}".format(self.voltage)

    def go_safe(self):
        """
        Set the gain voltage to its safe value: 0V (i.e. the Gain Voltage at the PMT is = only the residual voltage)
        """
        self._start_output(0)
