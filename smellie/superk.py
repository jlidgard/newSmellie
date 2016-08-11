from smellie_config import SK_COM_PORT
from superk.SuperK import string_buffer, portOpen, port_close, getSuperKInfo#, statusBitStructure, superKControlStructure

class SuperKHWError(Exception):
    """
    Thrown if an inconsistency is noticed *after* any hardware instruction is executed (i.e. a problem with the hardware itself)
    """
    pass

class SuperK(object):

    def __init__(self):
        self.COMPort = SK_COM_PORT
        
        superKControlCluster = superKControlStructure()
        superKControlCluster.trigLevelSetpointmV = c_uint16(1000)
        superKControlCluster.displayBacklightPercent = c_uint8(0)
        superKControlCluster.trigMode = c_uint8(1)
        superKControlCluster.internalPulseFreqHz = c_uint16(0)
        superKControlCluster.burstPulses = c_uint16(1)
        superKControlCluster.watchdogIntervalSec = c_uint8(0)
        superKControlCluster.internalPulseFreqLimitHz = c_uint32(0)
        setSuperKControls(self.COMPort,superKControlCluster)
        
    def port_open(self):
        """
        undocumented
        """
        portOpen(self.COMPort)
        
    def port_close(self):
        """
        undocumented
        """
        portClose(self.COMPort)

    def go_ready(intensity, low_wavelength, high_wavelength):
        """
        undocumented
        """
        # turn the lock off then turn the emission on
        NDFilterSetpointPercentx10, SWFilterSetpointAngstrom, LPFilterSetpointAngstrom = getVariaControls(self.COMPort)
        if (intensity*10!=NDFilterSetpointPercentx10 and low_wavelength!=LPFilterSetpointAngstrom and high_wavelength!=SWFilterSetpointAngstrom):
            setVariaControls(self.COMPort,intensity,SWFilterSetpointAngstrom,LPFilterSetpointAngstrom)
        setSuperKControlInterlock(self.COMPort,1)
        setSuperKControlEmission(self.COMPort,1)
        
    def go_safe():
        """
        undocumented
        """
        # turn off emission then set lock on
        setSuperKControlEmission(self.COMPort,0)
        setSuperKControlInterlock(self.COMPort,0)

    def varia_go_safe():
        """
        undocumented
        """
        # set varia wavelengths to be beyond the 700nm filter (so light is filtered out)
        setVariaControls(self.COMPort,0,8000,7900)
        #logging.error( 'Error Setting SuperK Safe States. ErrorCode: {}'.format( errorCode ) )

    def get_identity(self):
        """
        undocumented
        """
        firmware, version_info, module_type, serial_number = getSuperKInfo(self.COMPort)
        return firmware, version_info, module_type, serial_number
        
    def current_state(self):
        """
        Returns a formatted string with the current hardware settings
        """
        firmware, version_info, module_type, serial_number = get_identity()
        return "SuperK Info. Firmware: {}, Version Info: {}, Module Type: {}, Serial Number: {}".format( firmware, version_info, module_type, serial_number )
