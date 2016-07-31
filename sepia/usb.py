from sepia import check_channel, string_buffer, dll, raise_on_error_code
from ctypes import *

"""
Device Communication Functions (USB)
The functions of the USB group handle the PicoQuant Laser Device as an USB device. Besides opening and closing, they provide information on the device and help to identify the desired instance if there is more than one PQ Laser Device connected to the PC.
"""

#@raise_on_error_code
def get_dll_version():
    """
    String representation of the current .dll version. 

    :returns: .dll version
    """
    #str_buff = string_buffer()
    string_buff = int(20)
    return_string = (c_char_p*string_buff)()
    dll.SEPIA2_LIB_GetVersion( byref(return_string) )
    return return_string

#@raise_on_error_code    
def open_usb_device(dev_id):
    """
    Open exclusive access to the device connected to USB channel dev_id

    :param dev_id: the SEPIA device number, ordered from 0
    :type dev_id: int

    :returns: the product model and serial number
    """
    check_channel(dev_id, "open_device")
    #product_model = string_buffer()
    #serial_number = string_buffer()
    
    product_model_buff = int(20)
    product_model = (c_char_p*product_model_buff)()
    serial_number_buff = int(20)
    serial_number = (c_char_p*serial_number_buff)()
    
    dll.SEPIA2_USB_OpenDevice( dev_id, byref(product_model), byref(serial_number) )
    return str(cast(product_model,c_char_p).value), str(cast(serial_number,c_char_p).value)

#@raise_on_error_code    
def close_usb_device(dev_id):
    """
    Terminate exclusive access to the device connected to USB channel dev_id

    :param dev_id: the SEPIA device number, ordered from 0
    :type dev_id: int
    """
    check_channel(dev_id, "close_device")
    dll.SEPIA2_USB_CloseDevice(dev_id)

#@raise_on_error_code
def get_state_descriptor(dev_id):
    """
    Get a description message of the device connected to USB channel dev_id

    :param dev_id: the SEPIA device number, ordered from 0
    :type dev_id: int

    :returns: concatenated string descriptors of the USB device
    """
    check_channel(dev_id, "get_state_descriptor")
    #desc = string_buffer()
    string_buff = int(20)
    return_string = (ctypes.c_char_p*string_buff)()
    dll.SEPIA2_USB_GetStrDescriptor(dev_id, ctypes.byref(return_string) )
    return str(ctypes.cast(return_string,ctypes.c_char_p).value)
