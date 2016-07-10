from sepia import dll, string_buffer, raise_on_error_code
import ctypes

"""
Functions needed with any PicoQuant Laser Device, independent from its product/model type.
"""
    
@raise_on_error_code
def get_module_type(dev_id, slot_id, get_primary):
    """
    Return the module type

    :param dev_id: the SEPIA device number, ordered from 0
    :type dev_id: int

    :param slot_id: the slot number, between 000 and 989
    :type slot_id: int

    :param iGetPrimary: 1/0 for primary/secondary, i.e. laser driver/laser head
    :type iGetPrimary: bool

    :returns: module type
    :type module type: int
    """
    check_channel(dev_id, "get_module_type")
    module_type = ctypes.c_int32()
    dll.SEPIA2_COM_GetModuleType(dev_id, slot_id, iGetPrimary, module_type)
    return module_type

@raise_on_error_code
def decode_module_type(module_type):
    """
    Decode the module type into human-readable string

    :param module_type: module type
    :type module_type: int

    :returns: module
    :type module: string    
    """
    buff = string_buffer()
    dll.SEPIA2_COM_DecodeModuleType(module_type, buff)
    return buff

@raise_on_error_code
def get_serial_number(dev_id, slot_id, iGetPrimary):
    """
    Get the serial number of a given module

    :param dev_id: the SEPIA device number, ordered from 0
    :type dev_id: int

    :param slot_id: the slot number, between 000 and 989
    :type slot_id: int

    :param iGetPrimary: 1/0 for primary/secondary, i.e. laser driver/laser head
    :type iGetPrimary: bool

    :returns: serial number
    :type serial number: string
    """
    buff = string_buffer()
    dll.SEPIA2_COM_GetSerialNumber(dev_id, slot_id, iGetPrimary, buff)
    return buff

@raise_on_error_code
def has_secondary_module(dev_id, slot_id):
    """
    Check if a given primary module has a secondary

    :param dev_id: the SEPIA device number, ordered from 0
    :type dev_id: int

    :param slot_id: the slot number, between 000 and 989
    :type slot_id: int

    :returns: has secondary
    :type has secondary: bool
    """
    has_secondary = ctypes.c_int32()
    dll.SEPIA2_COM_HasSecondaryModule(dev_id, slot_id, has_secondary)
    return bool(has_secondary)
