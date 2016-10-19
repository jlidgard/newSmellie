from smellie_config import SK_COM_PORT
from superk.SuperK import string_buffer, portOpen, portClose, getSuperKInfo, getVariaInfo, getSuperKStatusBits, getVariaStatusBits, setSuperKControlEmission, setSuperKControlInterlock, setSuperKControls, setVariaControls, getVariaControls, statusBitStructure, superKControlStructure
from superk.variaMotor import VariaMotor

from ctypes import c_uint32, c_uint16, c_uint8

class SuperKHWError(Exception):
    """
    Thrown if an inconsistency is noticed *after* any hardware instruction is executed (i.e. a problem with the hardware itself)
    """
    pass

class SuperK(object):

    def __init__(self):
        self.COMPort = SK_COM_PORT
        self.NDfilter = VariaMotor()
        
    def port_open(self):
        """
        undocumented
        """
        #open superK
        portOpen(self.COMPort)
        
        superKControls = superKControlStructure()
        superKControls.trigLevelSetpointmV = c_uint16(1000) #c_uint16
        superKControls.displayBacklightPercent = c_uint8(0) #c_uint8
        superKControls.trigMode = c_uint8(1) #c_uint8
        superKControls.internalPulseFreqHz = c_uint16(0) #c_uint16
        superKControls.burstPulses = c_uint16(1) #c_uint16
        superKControls.watchdogIntervalSec = c_uint8(0) #c_uint8
        superKControls.internalPulseFreqLimitHz = c_uint32(0) #c_uint32
        setSuperKControls(self.COMPort,superKControls)
        
        #open varia ND filter arduino motor controller
        self.NDfilter.open_controller()

    def port_close(self):
        """
        undocumented
        """
        #open superK
        portClose(self.COMPort)
           
        #close varia ND filter arduino motor controller
        self.NDfilter.close_controller()

    def go_ready(self, intensity, low_wavelength, high_wavelength):
        """
        undocumented
        """
        # set the intensity, low and high wavelengths of the Varia (checking if the settings aren't already set)
        NDFilterSetpointPercentx10, SWFilterSetpointAngstrom, LPFilterSetpointAngstrom = getVariaControls(self.COMPort)
        if (intensity*10!=NDFilterSetpointPercentx10 or low_wavelength!=LPFilterSetpointAngstrom or high_wavelength!=SWFilterSetpointAngstrom):
            setVariaControls(self.COMPort,intensity,high_wavelength,low_wavelength)
        
        # turn the lock off then turn the emission on (checking if the settings aren't already set)
        superKStatus = getSuperKStatusBits(self.COMPort)
        if superKStatus.bit1!=0:
            setSuperKControlInterlock(self.COMPort,1) #setting interlock to 1 unlocks laser (status bit shows 0 for interlock off)
        if superKStatus.bit0!=1:
            setSuperKControlEmission(self.COMPort,1)
        
    def go_safe(self):
        """
        undocumented
        """
        
        superKControls = superKControlStructure()
        superKControls.trigLevelSetpointmV = c_uint16(1000) #c_uint16
        superKControls.displayBacklightPercent = c_uint8(0) #c_uint8
        superKControls.trigMode = c_uint8(1) #c_uint8
        superKControls.internalPulseFreqHz = c_uint16(0) #c_uint16
        superKControls.burstPulses = c_uint16(1) #c_uint16
        superKControls.watchdogIntervalSec = c_uint8(0) #c_uint8
        superKControls.internalPulseFreqLimitHz = c_uint32(0) #c_uint32
        setSuperKControls(self.COMPort,superKControls)
        
        # turn off emission then set lock on (checking if the settings aren't already set)
        superKStatus = getSuperKStatusBits(self.COMPort)
        if superKStatus.bit0!=0:
            setSuperKControlEmission(self.COMPort,0) #emission before interlock when shutting down (or interlock warning)
        if superKStatus.bit1!=1:
            setSuperKControlInterlock(self.COMPort,0) #setting interlock to 0 locks laser (status bit shows 1 for interlock on)


    def varia_go_safe(self):
        """
        undocumented
        """
        # set varia wavelengths to be beyond the 700nm filter (so light is filtered out)
        NDFilterSetpointPercentx10, SWFilterSetpointAngstrom, LPFilterSetpointAngstrom = getVariaControls(self.COMPort)
        if (intensity*10!=0 and low_wavelength!=7900 and high_wavelength!=8000):
            setVariaControls(self.COMPort,0,8000,7900)
        
        #logging.error( 'Error Setting SuperK Safe States. ErrorCode: {}'.format( errorCode ) )

    def get_identity(self):
        """
        undocumented
        """
        firmware, version_info, module_type, serial_number = getSuperKInfo(self.COMPort)
        superK_info = "Firmware: {} Version Info: {} Module Type: {} Serial Number: {}".format( firmware, version_info, module_type, serial_number )
        firmware, version_info, module_type, serial_number = getVariaInfo(self.COMPort)
        varia_info = "Firmware: {} Version Info: {} Module Type: {} Serial Number: {}".format( firmware, version_info, module_type, serial_number )
        return superK_info, varia_info
        
    def NDfilter_position(self):
        return self.NDfilter.get_position()
        
    def NDfilter_set_position(self, positionValue):
        self.NDfilter.set_position(positionValue)
        
    def NDfilter_get_home_status(self):
        return self.NDfilter.get_home_status()
        
    def NDfilter_set_reference(self):
        self.NDfilter.set_reference_position()
        
    def current_state(self):
        """
        Returns a formatted string with the current hardware settings
        """
        superK_info, varia_info = self.get_identity()
        return "SuperK Info: {}, Varia Info: {}".format(superK_info, varia_info)
        
