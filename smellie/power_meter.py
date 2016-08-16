from smellie_config import PM_ADDRESS
from powermeter.powerMeterUtil import selfTest, identificationQuery, setPowerUnit, getPowerUnit, getPowerReference, getPowerReferenceState, getPowerAutorangeMode, getSensorInformation, getCalibrationMessage, getAttenuation, getDarkAdjustmentState, getPhotodiodeResponsivity, getThermopileResponsivity, getPyrosensorResponsivity, setDisplayContrast, setDisplayBrightness, getBeamDiameter, measurePower, getAverageCount, setAverageCount, getWavelength, getPowerRange, getDarkOffset, startDarkOffsetAdjustment, cancelDarkOffsetAdjustment, setWavelength, portOpen, portClose

class PowerMeterHWError(Exception):
    """
    Thrown if an inconsistency is noticed *after* any hardware instruction is executed (i.e. a problem with the hardware itself)
    """
    pass

class PowerMeter(object):

    def __init__(self):
        self.COMPort = PM_ADDRESS
        self.taskHandle = None
        self.attributeValue = 0

    def get_beam_diameter(self):
        """   
        undocumented
        """
        return getBeamDiameter(self.taskHandle, self.attributeValue)
        
    def get_power(self):
        """   
        :returns: ctype string buffer, the size of which is set in :mod:config
        """
        return measurePower(self.taskHandle)
        
    def get_wavelength(self):
        """   
        :returns: ctype string buffer, the size of which is set in :mod:config
        """
        return getWavelength(self.taskHandle, self.attributeValue)
        
    def get_power_range(self):
        """   
        :returns: ctype string buffer, the size of which is set in :mod:config
        """
        return getPowerRange(self.taskHandle, self.attributeValue)
        
    def get_dark_offset(self):
        """   
        :returns: ctype string buffer, the size of which is set in :mod:config
        """
        return getDarkOffset(self.taskHandle)
        
    def set_dark_offset_cancel(self):
        """   
        :returns: ctype string buffer, the size of which is set in :mod:config
        """
        cancelDarkOffsetAdjustment(self.taskHandle)
        
    def set_dark_offset(self):
        """   
        :returns: ctype string buffer, the size of which is set in :mod:config
        """
        startDarkOffsetAdjustment(self.taskHandle)

    def set_wavelength(self, setValue):
        """   
        :returns: ctype string buffer, the size of which is set in :mod:config
        """
        setWavelength(self.taskHandle, setValue)
        return 0
        
    def set_average_count(self, setValue):
        """   
        :returns: ctype string buffer, the size of which is set in :mod:config
        """
        setAverageCount(self.taskHandle, setValue)
        return 0
        
    def get_average_count(self):
        """   
        :returns: ctype string buffer, the size of which is set in :mod:config
        """
        return getAverageCount(self.taskHandle)
        
    def port_open(self, iDQueryDoQuery=1, resetDevice=1):
        """   
        :returns: ctype string buffer, the size of which is set in :mod:config
        """
        self.taskHandle = portOpen(self.COMPort, iDQueryDoQuery, resetDevice)
        selfTestResult, selfTestMessage = selfTest(self.taskHandle)
        if selfTestResult != 0:
            raise PowerMeterHWError("Self test of device failed. {}".format(message))
        return 0

    def port_close(self):
        """   
        :returns: ctype string buffer, the size of which is set in :mod:config
        """
        portClose(self.taskHandle)

    def default_settings(self):
        """   
        :returns: ctype string buffer, the size of which is set in :mod:config
        """
        self.set_average_count(100)
        self.set_wavelength(400)
        ##PM100DSetAttenuation
        #PM100DSetBeamDiameter
        #PM100DSetDateAndTime
        setDisplayBrightness(self.taskHandle,0)
        setDisplayContrast(self.taskHandle,0.5)
        #PM100DSetLineFrequency
        ##PM100DSetPhotodiodeInputFilterState
        ##PM100DSetPhotodiodeResponsivity
        #PM100DSetPowerAutorangeMode
        ##PM100DSetPowerReferenceState
        ##PM100DSetPowerReference
        setPowerUnit(self.taskHandle,0)
        ##PM100DSetPyrosensorResponsivity
        ##PM100DSetThermopileResponsivity
        
        #add more here

    def current_state(self):
        """
        Returns a formatted string with the current hardware settings
        """
        return "ID: {}, SelfTest: {}, PowerUnit: {}(0=W,1=dB), PowerReference: {}, ReferenceState:{}, AutorangeMode: {}, SensorInformation: {}\
        , PhotodiodeFilterState:{}, CalibrationMessage:{}, Attenuation: {}, DarkAdjustmentState: {}, DarkOffset: {}, PhotodiodeResponsivity: {}, ThermopileResponsivity: {}, PyrosensorResponsivity: {}, \
        BeamDiameter: {}, Wavelength: {}".format(
           identificationQuery(self.taskHandle),
           selfTest(self.taskHandle),
           getPowerUnit(self.taskHandle),
           getPowerReference(self.taskHandle, self.attributeValue),
           getPowerReferenceState(self.taskHandle),
           getPowerAutorangeMode(self.taskHandle),
           getSensorInformation(self.taskHandle),
           getPhotodiodeInputFilterState(self.taskHandle),
           getCalibrationMessage(self.taskHandle),
           getAttenuation(self.taskHandle, self.attributeValue),
           getDarkAdjustmentState(self.taskHandle),
           self.get_dark_offset(),
           getPhotodiodeResponsivity(self.taskHandle, self.attributeValue),
           getThermopileResponsivity(self.taskHandle, self.attributeValue),
           getPyrosensorResponsivity(self.taskHandle, self.attributeValue),
           self.get_beam_diameter(), 
           self.get_wavelength())
