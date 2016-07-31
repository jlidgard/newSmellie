from sepia import check_channel, dll, string_buffer, raise_on_error_code
import ctypes

"""
From the original C-API: `The functions of this group directly access low level structures from the firmware of the PQ Laser Device to initialize the dynamic data layer of the library. Right after opening a PQ Laser Device, any program utilizing this API has to perform a call to the GetModuleMap function, before it can access any module of the laser device`.

These functions are direct wraps into Python, with parameter outputs replaced
by return values.
"""

#@raise_on_error_code
def get_fwr_version(dev_id):
    """
    Return the current firmware version - the laser head must be online

    :param dev_id: the SEPIA device number, ordered from 0
    :type dev_id: int

    :returns: current version
    :type current version: string
    """
    string_buff = int(20)
    return_string = (ctypes.c_char_p*string_buff)()
    dll.SEPIA2_FWR_GetVersion(dev_id, ctypes.byref(return_string) )
    return str(ctypes.cast(return_string,ctypes.c_char_p).value)

#@raise_on_error_code
def get_module_map(dev_id, do_soft_restart = True):
    """
    Fetch the firmware mapping for the .dll - this must be called before using the laser head
    If 'do_soft_restart' is set to False, a power on/off is required to ensure an up to date mapping (consult page 11 of documentation).

    :param dev_id: the SEPIA device number, ordered from 0
    :type dev_id: int

    :param do_soft_restart: automatically trigger a power cycle to ensure a correct mapping with no reboot required
    :type do_soft_restart: True/False

    :returns: module count the current number of PicoQuant Laser Device configurational elements
    :type module count: int
    """
    check_channel(dev_id, "get_module_map")
    module_count = ctypes.c_int32()
    dll.SEPIA2_FWR_GetModuleMap(dev_id, bool(do_soft_restart), ctypes.byref(module_count) )
    return module_count.value

@raise_on_error_code
def free_module_map(dev_id):
    """
    Reinstitute the memory allocated for the module map - this should be called at the end of any procedure calling :func:`get_module_map`

    :param dev_id: the SEPIA device number, ordered from 0
    :type dev_id: int
    """
    check_channel(dev_id, "free_module_map")
    dll.SEPIA2_FWR_FreeModuleMap(dev_id)
