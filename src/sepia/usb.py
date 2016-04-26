from exceptions import decode_exceptions
from _sepia import string_buffer, dll
import ctypes

"""
Device Communication Functions (USB)
The functions of the USB group handle the PQ Laser Device as an USB device. Besides opening and closing, they provide information on the device and help to identify the desired instance if there is more than one PQ Laser Device connected to the PC.
"""

@decode_exceptions
def get_dll_version():
    '''get_dll_version()

    String representation of current dll version. 
    
    :returns: DLL version
    '''
    str_buff = string_buffer()
    dll.SEPIA2_LIB_GetVersion(str_buff)
    return str_buff

@decode_exceptions    
def open_usb_device(dev_id):
    '''open_usb_device(dev_id)
    Open exclusive access to the device on USB channel dev_id

    :param dev_id: the sepia device number (ordered from 0)

    :returns: the product model and serial number
    '''
    check_channel(dev_id, "open_device")
    product_model = string_buffer()
    serial_number = string_buffer()
    dll.SEPIA2_USB_OpenDevice(dev_id, 
                              product_model, serial_number)
    return product_model, serial_number

@decode_exceptions    
def close_usb_device(dev_id):
    '''close_usb_device(dev_id)
    Terminate exclusive access to device on dev_id
    
    :param dev_id: the sepia device number (ordered from 0)
    '''    
    check_channel(dev_id, "close_device")
    dll.SEPIA2_USB_CloseDevice(dev_id)

@decode_exceptions
def get_state_descriptor(dev_id):
    '''get_state_descriptor(dev_id)
    :param dev_id: the sepia device number (ordered from 0)

    :returns: concatenated string descriptors of USB device
    '''
    check_channel(dev_id, "get_state_descriptor")
    desc = string_buffer()
    dll.SEPIA2_USB_GetStrDescriptor(dev_id, desc)
    return desc
