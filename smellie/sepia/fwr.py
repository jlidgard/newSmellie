from sepia import dll, string_buffer, raise_on_error_code
import ctypes

"""
From the original C-API 'The functions of this group directly access low level structures from the firmware of the PQ Laser Device to initialize the dynamic data layer of the library. Right after opening a PQ Laser Device, any program utilizing this API has to perform a call to the GetModuleMap function, before it can access any module of the laser device'

These functions are direct wraps into python, with parameter outputs replaced
by return values
"""

@raise_on_error_code
def get_fwr_version(dev_id):
    '''get_fwr_version(dev_id)
    Returns the current firmware version, laser must be online
    
    :param dev_id: the sepia device number (ordered from 0)

    :returns: string containing the current version
    '''
    vers = string_buffer()
    dll.SEPIA2_FWR_GetVersion(dev_id, vers)
    return vers

@raise_on_error_code
def get_module_map(dev_id, do_soft_restart = True):
    '''get_module_map(dev_id, do_soft_restart = True)

    Fetch the firmware mapping for the dll, must be called before laser use
    if do_soft_restart is set to False, a power on/off is required to ensure
    an up to date mapping, consult Page 11 of docs.

    :param dev_id: the sepia device number (ordered from 0)

    :param do_soft_restart: automatically trigger a booting cycle to ensure a correct mapping with no reboot

    :returns: the current number of PQ Laser Device configurational elements
    '''
    check_channel(dev_id, "get_module_map")
    module_count = ctypes.c_int32()
    dll.SEPIA2_FWR_GetVersion(dev_id, 
                               bool(do_soft_restart),
                               module_count
                               )
    return module_count

@raise_on_error_code
def free_module_map(dev_id):
    """free_module_map(dev_id)

    Restitute the memory allocated for the module map, should be called
    at the end of any procedure calling :func:`get_module_map`

    :param dev_id: the sepia device number (ordered from 0)

    :returns: None
    """
    check_channel(dev_id, "free_module_map")
    dll.SEPIA2_FWR_FreeModuleMap(dev_id)

