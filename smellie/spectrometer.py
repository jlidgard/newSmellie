from spec.OOUtil import string_buffer, createWrapper, destroyWrapper, openAllSpectrometers, closeAllSpectrometers, getFirmwareVersion, getName, getSerialNumber, getIntegrationTime, setIntegrationTime, getScansToAverage, setScansToAverage, getSpectrum, getWavelengths, writeSpectrum, getFeatureControllerIrradianceCalibrationFactor, getFeatureControllerExternalTriggerDelay, getExternalTriggerMode, setExternalTriggerMode, setCorrectForElectricalDark, setCorrectForDetectorNonlinearity, getBoxcarWidth, setBoxcarWidth, getMaximumIntensity, getMaximumIntegrationTime, getMinimumIntegrationTime, getNumberOfDarkPixels, getNumberOfPixels, isSaturated, getLastException, destroyExternalTriggerDelay, getExternalTriggerDelayMaximum, getExternalTriggerDelayMinimum, setExternalTriggerDelay, initialise, shutdown

class SpectrometerHWError(Exception):
    """
    Thrown if an inconsistency is noticed *after* any hardware instruction is executed (i.e. a problem with the hardware itself)
    """
    pass

class Spectrometer(object):

    def __init__(self):
        self.wrapper = createWrapper()

    def open_spectrometer(self):
        """   
        undocumented
        """
        openAllSpectrometers(self.wrapper)
        
    def close_spectrometer(self):
        """   
        undocumented
        """
        closeAllSpectrometers(self.wrapper)
        destroyWrapper(self.wrapper)
        
    def get_identity(self):
        """   
        undocumented
        """
        return getName(self.wrapper), getFirmwareVersion(self.wrapper), getSerialNumber(self.wrapper)
        
    def current_state(self):
        """
        Returns a formatted string with the current hardware settings
        """
        return "Spectrometer Identity (name, Firmware, SerialNumber): {}".format( self.get_identity() )
