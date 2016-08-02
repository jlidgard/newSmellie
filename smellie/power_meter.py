from smellie_config import PM_ADDRESS
from powermeter.powerMeterUtil import getBeamDiameter, getPower, getWavelength, setPowerRange, getDarkOffset, setDarkOffsetCancel, setDarkOffset, setWavelength, portOpen, portClose

class PowerMeterHWError(Exception):
    """
    Thrown if an inconsistency is noticed *after* any hardware instruction is executed (i.e. a problem with the hardware itself)
    """
    pass

class PowerMeter(object):

    def __init__(self):
        self.COMPort = PM_ADDRESS

    def get_beam_diameter(self):
        """   
        :returns: ctype string buffer, the size of which is set in :mod:config
        """
        return getBeamDiameter(self.COMPort)
        
    def get_power(self):
        """   
        :returns: ctype string buffer, the size of which is set in :mod:config
        """
        return getPower(self.COMPort)
        
    def get_wavelength(self):
        """   
        :returns: ctype string buffer, the size of which is set in :mod:config
        """
        return getWavelength(self.COMPort)
        
    def set_power_range(self,setValue):
        """   
        :returns: ctype string buffer, the size of which is set in :mod:config
        """
        setPowerRange(self.COMPort, setValue)
        
    def get_dark_offset(self):
        """   
        :returns: ctype string buffer, the size of which is set in :mod:config
        """
        return getDarkOffset(self.COMPort)
        
    def set_dark_offset_cancel(self):
        """   
        :returns: ctype string buffer, the size of which is set in :mod:config
        """
        setDarkOffsetCancel(self.COMPort)
        
    def set_dark_offset(self):
        """   
        :returns: ctype string buffer, the size of which is set in :mod:config
        """
        setDarkOffset(self.COMPort)

    def set_wavelength(self, setValue):
        """   
        :returns: ctype string buffer, the size of which is set in :mod:config
        """
        setWavelength(self.COMPort, setValue)
        
    def port_open(self):
        """   
        :returns: ctype string buffer, the size of which is set in :mod:config
        """
        selfTestResult, message = portOpen(self.COMPort)
        if selfTestResult != 0:
            raise PowerMeterHWError("Self test of device failed. {}".format(message))

    def port_close(self):
        """   
        :returns: ctype string buffer, the size of which is set in :mod:config
        """
        message = portClose(self.COMPort)
        
    def current_state(self):
        """
        Returns a formatted string with the current hardware settings
        """
        return "Get Power: {1}, Get Beam Diameter: {0}, Get Wavelength: {2}, Get Dark Offset: {3}".format(self.get_beam_diameter(), 
           self.get_power(), 
           self.get_wavelength(),
           self.get_dark_offset())
