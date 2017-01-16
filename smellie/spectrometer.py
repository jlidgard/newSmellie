from smellie.spectrometer_util import string_buffer, createWrapper, destroyWrapper, openAllSpectrometers, closeAllSpectrometers, getFirmwareVersion, getName, getSerialNumber, getIntegrationTime, setIntegrationTime, getScansToAverage, setScansToAverage, getSpectrum, getWavelengths, getFeatureControllerIrradianceCalibrationFactor, getFeatureControllerExternalTriggerDelay, getExternalTriggerMode, setExternalTriggerMode, setCorrectForElectricalDark, setCorrectForDetectorNonlinearity, getBoxcarWidth, setBoxcarWidth, getMaximumIntensity, getMaximumIntegrationTime, getMinimumIntegrationTime, getNumberOfDarkPixels, getNumberOfPixels, isSaturated, getLastException, destroyExternalTriggerDelay, getExternalTriggerDelayMaximum, getExternalTriggerDelayMinimum, setExternalTriggerDelay
from operator import itemgetter

class SpectrometerLogicError(Exception):
    """
    Thrown if an inconsistency is noticed *before* any instructions are sent to the hardware (i.e. a problem with code logic)
    """
    pass

class SpectrometerHWError(Exception):
    """
    Thrown if an inconsistency is noticed *after* any hardware instruction is executed (i.e. a problem with the hardware itself)
    """
    pass

class Spectrometer(object):

    def __init__(self):
        self.wrapper = createWrapper()
        self.isConnected = False

    def port_open(self):
        """   
        undocumented
        """
        if not self.isConnected:
            openAllSpectrometers(self.wrapper)
            self.isConnected = True
            
            #initialise external trigger delay
            self.extTrigDelay = getFeatureControllerExternalTriggerDelay(self.wrapper)
            setExternalTriggerDelay(self.extTrigDelay,1000)
            
            #set default parameters
            self.set_parameters()
        else:
            raise SpectrometerLogicError("Spectrometer port already open.") 

    def port_close(self):
        """   
        undocumented
        """
        if self.isConnected:
            closeAllSpectrometers(self.wrapper)
            destroyWrapper(self.wrapper)
            destroyExternalTriggerDelay()
            self.isConnected = False
        else:
            raise SpectrometerLogicError("Spectrometer port not open.") 
        
    def set_parameters(self, triggerMode=0, integrationTime=10000, scansToAverage=1):
        """   
        undocumented
        """
        if self.isConnected:
            #set acquisition parameters
            setExternalTriggerMode(self.wrapper,triggerMode)
            setBoxcarWidth(self.wrapper, 0)
            setCorrectForDetectorNonlinearity(self.wrapper,1)
            setCorrectForElectricalDark(self.wrapper,1)
            setIntegrationTime(self.wrapper,integrationTime)
            setScansToAverage(self.wrapper,scansToAverage)
        else:
            raise SpectrometerLogicError("Spectrometer port not open.")  
        
    def get_identity(self):
        """   
        undocumented
        """
        if self.isConnected:
            return getName(self.wrapper), getFirmwareVersion(self.wrapper), getSerialNumber(self.wrapper)
        else:
            raise SpectrometerLogicError("Spectrometer port not open.") 
            
    def get_spectrum(self):
        """   
        undocumented
        """
        if self.isConnected:
            return getSpectrum(self.wrapper)
        else:
            raise SpectrometerLogicError("Spectrometer port not open.")
            
    def get_wavelengths(self):
        """   
        undocumented
        """
        if self.isConnected:
            return getWavelengths(self.wrapper)
        else:
            raise SpectrometerLogicError("Spectrometer port not open.") 

    def write_spectrum(self,filePath,wavelengthData,spectrumData):
        """   
        :undocumented
        """
        fileOut = open(str(filePath), 'a')
        fileOut.write( 'Wavelength(nm),Intensity(arb)\n')
        for i,j in zip(wavelengthData,spectrumData):
            fileOut.write( '{},{}\n'.format( i,j ) )
        fileOut.closed

    def get_spectrum_maximum(self,wavelengthData,spectrumData):
        """   
        undocumented
        """
        index, maxSpec = max(enumerate(spectrumData), key=itemgetter(1))
        maxWave = wavelengthData[index]
        return maxWave, maxSpec
        
    def is_connected(self):
        """   
        Check if the connection to the device is open
        """
        return self.isConnected
        
    def is_alive(self):
        """
        Quick check alive or not.
        """
        if self.isConnected:
            if (self.get_identity()[0] == 'USB2000+'): isAlive = True #choose to check the HW model ('USB2000+')
            else: isAlive = False
            return isAlive
        else:
            raise SpectrometerLogicError("Spectrometer port not open.") 
        
    def system_state(self):
        """
        Returns a formatted string with the hardware info and constant settings.
        """
        if self.isConnected:
            return "Spectrometer (system):: Identity (name, Firmware, SerialNumber): {}".format( self.get_identity() )
        else:
            raise SpectrometerLogicError("Spectrometer port not open.") 
        
    def current_state(self):
        """
        Returns a formatted string with the current hardware settings
        """
        if self.isConnected:
            return "Spectrometer (settings):: ".format( )
        else:
            raise SpectrometerLogicError("Spectrometer port not open.") 
