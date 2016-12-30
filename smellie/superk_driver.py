from smellie_config import SK_COM_PORT
from varia_ndfilter import VariaNDFilter
from superk import string_buffer, portOpen, portClose, getSuperKInfo, getVariaInfo, getSuperKStatusBits, getVariaStatusBits, setSuperKControlEmission, setSuperKControlInterlock, setSuperKControls, setVariaControls, getVariaControls, statusBitStructure, superKControlStructure
from smellie.smellie_logger import SMELLIELogger

from ctypes import c_uint32, c_uint16, c_uint8

class SuperKDriverLogicError(Exception):
    """
    Thrown if an inconsistency is noticed *before* any instructions are sent to the hardware (i.e. a problem with code logic)
    """
    pass

class SuperKDriverHWError(Exception):
    """
    Thrown if an inconsistency is noticed *after* any hardware instruction is executed (i.e. a problem with the hardware itself)
    """
    pass

class SuperKDriver(object):

    def __init__(self):
        self.COMPort = SK_COM_PORT
        self.NDFilter = VariaNDFilter()
        self.isConnected = False
        
    def port_open(self):
        """
        undocumented
        """
        SMELLIELogger.debug('SNODROP DEBUG: SuperKDriver.port_open()')
        if not self.isConnected:
            portOpen(self.COMPort) #open SuperK
            self.NDFilter.port_open() #open varia ND filter arduino motor controller
            self.isConnected = True
            self.set_parameters() #load default settings
        else:
            raise SuperKDriverLogicError("Laser port already open.") 

    def port_close(self):
        """
        undocumented
        """
        SMELLIELogger.debug('SNODROP DEBUG: SuperKDriver.port_close()')
        if self.isConnected:
            portClose(self.COMPort) #close SuperK
            self.NDFilter.port_close() #close varia ND filter controller
            self.isConnected = False
        else:
            raise SuperKDriverLogicError("SuperK port not open.")

    def set_parameters(self):
        """
        undocumented
        """
        if self.isConnected:
            SMELLIELogger.debug('SNODROP DEBUG: SuperKDriver.set_parameters()')
            superKControls = superKControlStructure()
            superKControls.trigLevelSetpointmV = c_uint16(1000)
            superKControls.displayBacklightPercent = c_uint8(0)
            superKControls.trigMode = c_uint8(1)
            superKControls.internalPulseFreqHz = c_uint16(0)
            superKControls.burstPulses = c_uint16(1) 
            superKControls.watchdogIntervalSec = c_uint8(0)
            superKControls.internalPulseFreqLimitHz = c_uint32(0) 
            setSuperKControls(self.COMPort,superKControls)
        else:
            raise SuperKDriverLogicError("SuperK port not open.")
    
    def get_wavelengths(self):
        """
        undocumented
        """
        if self.isConnected:
            high_wavelength, low_wavelength = getVariaControls(self.COMPort)
            SMELLIELogger.debug('SNODROP DEBUG: SuperKDriver.get_wavelengths() = {}, {}'.format(low_wavelength, high_wavelength))
            return low_wavelength, high_wavelength
        else:
            raise SuperKDriverLogicError("SuperK port not open.")
            return 0
    
    def go_ready(self, intensity, low_wavelength, high_wavelength):
        """
        undocumented
        """
        if self.isConnected:
            # set the intensity, low and high wavelengths of the Varia (checking if the settings aren't already set)
            SMELLIELogger.debug('SNODROP DEBUG: SuperKDriver.go_ready({},{},{})'.format(intensity, low_wavelength, high_wavelength))
            SWFilterSetpointAngstrom, LPFilterSetpointAngstrom = self.get_wavelengths()
            if (low_wavelength!=LPFilterSetpointAngstrom or high_wavelength!=SWFilterSetpointAngstrom):
                setVariaControls(self.COMPort,high_wavelength,low_wavelength)
            
            # turn the lock off then turn the emission on (checking if the settings aren't already set)
            superKStatus = getSuperKStatusBits(self.COMPort)
            if superKStatus.bit1!=0:
                setSuperKControlInterlock(self.COMPort,1) #setting interlock to 1 unlocks laser (status bit shows 0 for interlock off)
            if superKStatus.bit0!=1:
                setSuperKControlEmission(self.COMPort,1)
        else:
            raise SuperKDriverLogicError("SuperK port not open.")
            
    def go_safe(self):
        """
        undocumented
        """
        if self.isConnected:
            SMELLIELogger.debug('SNODROP DEBUG: SuperKDriver.go_safe()')
        
            self.set_parameters()
            
            # turn off emission then set lock on (checking if the settings aren't already set)
            superKStatus = getSuperKStatusBits(self.COMPort)
            if superKStatus.bit0!=0:
                setSuperKControlEmission(self.COMPort,0) #emission before interlock when shutting down (or interlock warning)
            if superKStatus.bit1!=1:
                setSuperKControlInterlock(self.COMPort,0) #setting interlock to 0 locks laser (status bit shows 1 for interlock on)
        else:
            raise SuperKDriverLogicError("SuperK port not open.")

    def varia_go_safe(self):
        """
        undocumented
        """
        if self.isConnected:
            SMELLIELogger.debug('SNODROP DEBUG: SuperKDriver.go_safe()')
        
            # set varia wavelengths to be beyond the 700nm filter (so light is filtered out)
            low_wavelength, high_wavelength = getVariaControls(self.COMPort)
            if (low_wavelength!=7900 and high_wavelength!=8000):
                setVariaControls(self.COMPort,8000,7900)
            #logging.error( 'Error Setting SuperK Safe States. ErrorCode: {}'.format( errorCode ) )
        else:
            raise SuperKDriverLogicError("SuperK port not open.")

    def is_interlock_locked(self):
        """
        Check the status of the SMELLIE interlock.
        
        :returns: True if the interlock is Locked (Relay Open)
        """
        if self.isConnected:
            SMELLIELogger.debug('SNODROP DEBUG: SuperKDriver.is_laser_locked()')
            
            #interlock circuit
            superKStatus = getSuperKStatusBits(self.COMPort)
            if (superKStatus.bit3 == 0):
                interlock_locked = False
            elif (superKStatus.bit3 == 1):
                interlock_locked = True
            else:
                raise SuperKDriverLogicError("Unknown response for interlock value.")
                interlock_locked = None
        return interlock_locked
            
    def is_laser_locked(self):
        """
        Poll the SuperK driver for its lock status.
        
        :returns: True if the internal-lock is on.
        """
        if self.isConnected:
            SMELLIELogger.debug('SNODROP DEBUG: SuperKDriver.is_laser_locked()')
            
            #interlock circuit
            interlock_locked = self.is_interlock_locked()

            #internal interlock
            superKStatus = getSuperKStatusBits(self.COMPort)
            if (superKStatus.bit1 == 0):
                laser_locked = False
            elif (superKStatus.bit1 == 1):
                laser_locked = True
            else:
                raise SuperKDriverLogicError("Unknown response for interlock value.")
                interlock_locked = None

            #combination of interlock and laser interlocks
            if (laser_locked and interlock_locked):
                is_locked = True
            else:
                is_locked = False
            return is_locked
            
        else:
            raise SuperKDriverLogicError("SuperK port not open.") 
            return None
            
    def get_identity(self):
        """
        undocumented
        """
        if self.isConnected:
            firmware, version_info, module_type, serial_number = getSuperKInfo(self.COMPort)
            superK_info = "Firmware: {} Version Info: {} Module Type: {} Serial Number: {}".format( firmware, version_info, module_type, serial_number )
            firmware, version_info, module_type, serial_number = getVariaInfo(self.COMPort)
            varia_info = "Firmware: {} Version Info: {} Module Type: {} Serial Number: {}".format( firmware, version_info, module_type, serial_number )
            SMELLIELogger.debug('SNODROP DEBUG: SuperKDriver.get_identity() = {},{}'.format(superK_info, varia_info))
            return superK_info, varia_info
        else:
            raise SuperKDriverLogicError("SuperK port not open.")
            return 0
        
    def NDFilter_position(self):
        NDFilterPosition = self.NDFilter.get_position()
        SMELLIELogger.debug('SNODROP DEBUG: SuperKDriver.NDFilter_position() = {}'.format(NDFilterPosition))
        return NDFilterPosition
        
    def NDFilter_set_position(self, positionValue):
        SMELLIELogger.debug('SNODROP DEBUG: SuperKDriver.NDFilter_set_position({})'.format(positionValue))
        self.NDFilter.set_position(positionValue)
        
    def NDFilter_get_home_status(self):
        NDFilterHomeStatus = self.NDFilter.get_home_status()
        SMELLIELogger.debug('SNODROP DEBUG: SuperKDriver.NDFilter_get_home_status() = {}'.format(NDFilterHomeStatus))
        return NDFilterHomeStatus
        
    def NDFilter_set_reference(self):
        SMELLIELogger.debug('SNODROP DEBUG: SuperKDriver.NDFilter_set_reference()')
        self.NDFilter.set_reference_position()
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
        if self.isConnected:
            checkValue = getSuperKInfo(self.COMPort) #check superK Compact HW model ('74')
            checkValue2 = getVariaInfo(self.COMPort) #check superK Varia HW model ('68')
            checkValue3 = self.NDFilter.is_alive() #check variamotor controller
            if (checkValue[2] == '74' and checkValue2[2] == '68' and checkValue3 == True): isAlive = True
            else: isAlive = False
            return isAlive
        else:
            raise SuperKDriverLogicError("SuperK port not open.") 
            return 0 

    def system_state(self):
        """
        Returns a formatted string with the hardware info and constant settings.
        """
        if self.isConnected:
            superK_info, varia_info = self.get_identity()
            return "SuperK laser (settings):: Compact Info: {}, Varia Info: {}{}".format(superK_info, varia_info, self.NDFilter.system_state() )
        else:
            raise SuperKDriverLogicError("SuperK port not open.") 
            return 0

    def current_state(self):
        """
        Returns a formatted string with the current hardware settings
        """
        if self.isConnected:
            low_wavelength, high_wavelength = self.get_wavelengths()
            return "SuperK laser (settings):: NDFilter Step: {}, Low Wavelength: {}, High Wavelength: {}. {}".format(self.NDFilter.current_state(), low_wavelength, high_wavelength )
        else:
            raise SuperKDriverLogicError("SuperK port not open.") 
            return 0    
