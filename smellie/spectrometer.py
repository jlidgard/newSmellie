from smellie.spectrometer_util import string_buffer, createWrapper, destroyWrapper, openAllSpectrometers, closeAllSpectrometers, getFirmwareVersion, getName, getSerialNumber, getIntegrationTime, setIntegrationTime, getScansToAverage, setScansToAverage, getSpectrum, getWavelengths, writeSpectrum, getFeatureControllerIrradianceCalibrationFactor, getFeatureControllerExternalTriggerDelay, getExternalTriggerMode, setExternalTriggerMode, setCorrectForElectricalDark, setCorrectForDetectorNonlinearity, getBoxcarWidth, setBoxcarWidth, getMaximumIntensity, getMaximumIntegrationTime, getMinimumIntegrationTime, getNumberOfDarkPixels, getNumberOfPixels, isSaturated, getLastException, destroyExternalTriggerDelay, getExternalTriggerDelayMaximum, getExternalTriggerDelayMinimum, setExternalTriggerDelay, initialise, shutdown

class SpectrometerHWError(Exception):
    """
    Thrown if an inconsistency is noticed *after* any hardware instruction is executed (i.e. a problem with the hardware itself)
    """
    pass

class Spectrometer(object):

    def __init__(self):
        self.wrapper = createWrapper()
        self.isConnected = None

    def port_open(self):
        """   
        undocumented
        """
        openAllSpectrometers(self.wrapper)
        self.isConnected = True
        
    def port_close(self):
        """   
        undocumented
        """
        closeAllSpectrometers(self.wrapper)
        destroyWrapper(self.wrapper)
        self.isConnected = False
        
    def get_identity(self):
        """   
        undocumented
        """
        return getName(self.wrapper), getFirmwareVersion(self.wrapper), getSerialNumber(self.wrapper)
        
    def is_connected(self):
        """   
        Check if the connection to the device is open
        """
        return self.isConnected
        
    def is_alive(self):
        """
        Quick check alive or not.
        """
        isAlive = None
        if self.isConnected:
            checkValue = self.get_identity() #choose to check the firmware version ('1.05.419')
        else: 
            self.port_open()
            checkValue = self.get_identity()
            print checkValue
            self.port_close()
        if (checkValue[0] == '1.05.419'): isAlive = True
        else: isAlive = False
        return checkValue
        
    def current_state(self):
        """
        Returns a formatted string with the current hardware settings
        """
        return "Spectrometer Identity (name, Firmware, SerialNumber): {}".format( self.get_identity() )
