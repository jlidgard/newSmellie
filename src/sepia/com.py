from _sepia import dll, string_buffer, raise_on_error_code
import ctypes
"""
Functions needed with any PQ Laser Device, independent from its product 
model type.
"""
    
@raise_on_error_code
def get_module_type(dev_id, slot_id, get_primary):
    """get_module_type(dev_id, slot_idm, get_primary)

    :param dev_id: the sepia device number (ordered from 0)
    
    :param slot_id: slot number, integer 000-989
    
    :param iGetPrimary: 1/0 for primary/secondary eg. laser driver/laser head

    :type iGetPrimary: bool

    :returns: module type (int)
    """
    check_channel(dev_id, "get_module_type")
    module_type = ctypes.c_int32()
    dll.SEPIA2_COM_GetModuleType(dev_id, slot_id, iGetPrimary, module_type)
    return module_type
    
@raise_on_error_code
def decode_module_type(module_type):
    """decode_module_type(module_type)

    Decode module type into human readable string

    :param module_type: Module type
    :type module_type: int

    :returns: module type string    
    """
    buff = string_buffer()
    dll.SEPIA2_COM_DecodeModuleType(module_type, buff)
    return buff

@raise_on_error_code
def get_serial_number(dev_id, slot_id, iGetPrimary):
    """get_serial_number(dev_id, slot_id, iGetPrimary)
    Get the serial number of a given module
        
    :param dev_id: the sepia device number (ordered from 0)
    
    :param slot_id: slot number, integer 000-989
    
    :param iGetPrimary: 1/0 for primary/secondary eg. laser driver/laser head
    :type iGetPrimary: bool
    
    :returns: Serial number as string
    """

    buff = string_buffer()
    dll.SEPIA2_COM_GetSerialNumber(dev_id, slot_id, iGetPrimary, buff)
    return buff

@raise_on_error_code
def has_secondary_module(dev_id, slot_id):
    """has_secondary_module(dev_id, slot_id)
    Does this module have a secondary?

    :param dev_id: the sepia device number (ordered from 0)
    
    :param slot_id: slot number, integer 000-989

    :returns: Has secondary bool
    """
    has_secondary = ctypes.c_int32()
    dll.SEPIA2_COM_HasSecondaryModule(dev_id, slot_id, has_secondary)
    return bool(has_secondary)
    
