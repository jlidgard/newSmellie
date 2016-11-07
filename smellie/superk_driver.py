from smellie_config import SK_COM_PORT
from varia_motor import VariaMotor
from superk import string_buffer, portOpen, portClose, getSuperKInfo, getVariaInfo, getSuperKStatusBits, getVariaStatusBits, setSuperKControlEmission, setSuperKControlInterlock, setSuperKControls, setVariaControls, getVariaControls, statusBitStructure, superKControlStructure


from ctypes import c_uint32, c_uint16, c_uint8

class SuperkDriverLogicError(Exception):
    """
    Thrown if an inconsistency is noticed *before* any instructions are sent to the hardware (i.e. a problem with code logic)
    """
    pass

class SuperkDriverHWError(Exception):
    """
    Thrown if an inconsistency is noticed *after* any hardware instruction is executed (i.e. a problem with the hardware itself)
    """
    pass

class SuperkDriver(object):

    def __init__(self):
        self.COMPort = SK_COM_PORT
        self.NDfilter = VariaMotor()
        self.isConnected = False
        self.superkisConnected = False
        self.NDfilterisConnected = False
        
    def port_open(self):
        """
        undocumented
        """
        if not self.isConnected:
            portOpen(self.COMPort) #open superK
            self.NDfilter.port_open() #open varia ND filter arduino motor controller
            self.isConnected = True
            self.set_parameters() #load default settings
        else:
            raise SuperkDriverLogicError("Laser port already open.") 

    def port_close(self):
        """
        undocumented
        """
        #open superK
        portClose(self.COMPort)
        #close varia ND filter arduino motor controller
        self.NDfilter.port_close()
        self.isConnected = False

    def set_parameters(self):
        """
        undocumented
        """
        if self.isConnected:
            superKControls = superKControlStructure()
            superKControls.trigLevelSetpointmV = c_uint16(1000) #c_uint16
            superKControls.displayBacklightPercent = c_uint8(0) #c_uint8
            superKControls.trigMode = c_uint8(1) #c_uint8
            superKControls.internalPulseFreqHz = c_uint16(0) #c_uint16
            superKControls.burstPulses = c_uint16(1) #c_uint16
            superKControls.watchdogIntervalSec = c_uint8(0) #c_uint8
            superKControls.internalPulseFreqLimitHz = c_uint32(0) #c_uint32
            setSuperKControls(self.COMPort,superKControls)
        else:
            raise SuperkDriverLogicError("Laser port not open.")
    
    def get_wavelengths(self):
        """
        undocumented
        """
        if self.isConnected:
            high_wavelength, low_wavelength = getVariaControls(self.COMPort)
            return low_wavelength, high_wavelength
        else:
            raise SuperkDriverLogicError("Laser port not open.")
            return 0
    
    def go_ready(self, intensity, low_wavelength, high_wavelength):
        """
        undocumented
        """
        if self.isConnected:
            # set the intensity, low and high wavelengths of the Varia (checking if the settings aren't already set)
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
            raise SuperkDriverLogicError("Laser port not open.")
            
    def go_safe(self):
        """
        undocumented
        """
        if self.isConnected:
            self.set_parameters()
            
            # turn off emission then set lock on (checking if the settings aren't already set)
            superKStatus = getSuperKStatusBits(self.COMPort)
            if superKStatus.bit0!=0:
                setSuperKControlEmission(self.COMPort,0) #emission before interlock when shutting down (or interlock warning)
            if superKStatus.bit1!=1:
                setSuperKControlInterlock(self.COMPort,0) #setting interlock to 0 locks laser (status bit shows 1 for interlock on)
        else:
            raise SuperkDriverLogicError("Laser port not open.")

    def varia_go_safe(self):
        """
        undocumented
        """
        if self.isConnected:
            # set varia wavelengths to be beyond the 700nm filter (so light is filtered out)
            low_wavelength, high_wavelength = getVariaControls(self.COMPort)
            if (low_wavelength!=7900 and high_wavelength!=8000):
                setVariaControls(self.COMPort,8000,7900)
            #logging.error( 'Error Setting SuperK Safe States. ErrorCode: {}'.format( errorCode ) )
        else:
            raise SuperkDriverLogicError("Laser port not open.")
            
    def get_identity(self):
        """
        undocumented
        """
        if self.isConnected:
            firmware, version_info, module_type, serial_number = getSuperKInfo(self.COMPort)
            superK_info = "Firmware: {} Version Info: {} Module Type: {} Serial Number: {}".format( firmware, version_info, module_type, serial_number )
            firmware, version_info, module_type, serial_number = getVariaInfo(self.COMPort)
            varia_info = "Firmware: {} Version Info: {} Module Type: {} Serial Number: {}".format( firmware, version_info, module_type, serial_number )
            return superK_info, varia_info
        else:
            raise SuperkDriverLogicError("Laser port not open.")
            return 0
        
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
        if self.isConnected:
            checkValue = getSuperKInfo(self.COMPort) #check superK Compact HW model ('74')
            checkValue2 = getVariaInfo(self.COMPort) #check superK Varia HW model ('68')
            checkValue3 = self.NDfilter.is_alive() #check variamotor controller
            if (checkValue[2] == '74' and checkValue2[2] == '68' and checkValue3 == True): isAlive = True
            else: isAlive = False
            return isAlive
        else:
            raise SuperkDriverLogicError("Laser port not open.") 
            return 0 

    def system_state(self):
        """
        Returns a formatted string with the hardware info and constant settings.
        """
        if self.isConnected:
            superK_info, varia_info = self.get_identity()
            return "Superk laser (settings):: Compact Info: {}, Varia Info: {}{}".format(superK_info, varia_info, self.NDfilter.system_state() )
        else:
            raise SuperkDriverLogicError("Laser port not open.") 
            return 0

    def current_state(self):
        """
        Returns a formatted string with the current hardware settings
        """
        if self.isConnected:
            low_wavelength, high_wavelength = self.get_wavelengths()
            return "Superk laser (settings):: Low Wavelength: {}, High Wavelength: {}. {}".format(low_wavelength, high_wavelength, self.NDfilter.current_state() )
        else:
            raise SuperkDriverLogicError("Laser port not open.") 
            return 0    
