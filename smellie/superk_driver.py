from smellie_config import SK_COM_PORT
from smellie.superk import string_buffer, portOpen, portClose, getSuperKInfo, getVariaInfo, getSuperKStatusBits, getVariaStatusBits, setSuperKControlEmission, setSuperKControlInterlock, setSuperKControls, setVariaControls, getVariaControls, statusBitStructure, superKControlStructure
from smellie.varia_motor import VariaMotor

from ctypes import c_uint32, c_uint16, c_uint8

class SuperKHWError(Exception):
    """
    Thrown if an inconsistency is noticed *after* any hardware instruction is executed (i.e. a problem with the hardware itself)
    """
    pass

class SuperKDriver(object):

    def __init__(self):
        self.COMPort = SK_COM_PORT
        self.NDfilter = VariaMotor()
        self.isConnected = None
        
    def port_open(self):
        """
        undocumented
        """
        #open superK
        portOpen(self.COMPort)
        self.default_settings()
        #open varia ND filter arduino motor controller
        self.NDfilter.port_open()
        self.isConnected = True
        return 0

    def port_close(self):
        """
        undocumented
        """
        #open superK
        portClose(self.COMPort)
        #close varia ND filter arduino motor controller
        self.NDfilter.port_close()
        self.isConnected = False
        return 0
        
    def default_settings(self):
        superKControls = superKControlStructure()
        superKControls.trigLevelSetpointmV = c_uint16(1000) #c_uint16
        superKControls.displayBacklightPercent = c_uint8(0) #c_uint8
        superKControls.trigMode = c_uint8(1) #c_uint8
        superKControls.internalPulseFreqHz = c_uint16(0) #c_uint16
        superKControls.burstPulses = c_uint16(1) #c_uint16
        superKControls.watchdogIntervalSec = c_uint8(0) #c_uint8
        superKControls.internalPulseFreqLimitHz = c_uint32(0) #c_uint32
        setSuperKControls(self.COMPort,superKControls)
        return 0
    
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
        return 0
        
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
        return 0

    def varia_go_safe(self):
        """
        undocumented
        """
        # set varia wavelengths to be beyond the 700nm filter (so light is filtered out)
        NDFilterSetpointPercentx10, SWFilterSetpointAngstrom, LPFilterSetpointAngstrom = getVariaControls(self.COMPort)
        if (intensity*10!=0 and low_wavelength!=7900 and high_wavelength!=8000):
            setVariaControls(self.COMPort,0,8000,7900)
        #logging.error( 'Error Setting SuperK Safe States. ErrorCode: {}'.format( errorCode ) )
        return 0
        
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
        return 0
        
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
            checkValue = getSuperKInfo(self.COMPort) #check superK Compact HW model ('74')
            checkValue2 = getVariaInfo(self.COMPort) #check superK Varia HW model ('68')
            checkValue3 = self.NDfilter.is_alive() #check variamotor controller
            
        else: 
            self.port_open()
            checkValue = getSuperKInfo(self.COMPort)
            checkValue2 = getVariaInfo(self.COMPort)
            checkValue3 = self.NDfilter.is_alive()
            self.port_close()   
        if (checkValue[2] == '74' and checkValue2[2] == '68' and checkValue3 == True): isAlive = True
        else: isAlive = False
        return isAlive

    def current_state(self):
        """
        Returns a formatted string with the current hardware settings
        """
        superK_info, varia_info = self.get_identity()
        return "SuperK Info: {}, Varia Info: {}".format(superK_info, varia_info)
        
