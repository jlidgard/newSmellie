from smellie_config import SK_ADDRESS
from superk.SuperK import statusBitStructure, superKControlStructure, string_buffer, portOpen, port_close, getSuperKInfo

class SuperKHWError(Exception):
    """
    Thrown if an inconsistency is noticed *after* any hardware instruction is executed (i.e. a problem with the hardware itself)
    """
    pass

class SuperK(object):

    def __init__(self):
        self.COMPort = SK_ADDRESS

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
