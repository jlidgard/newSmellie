from sepia import check_channel, string_buffer, dll, raise_on_error_code

"""
Device Communication Functions (USB)
The functions of the USB group handle the PicoQuant Laser Device as an USB device. Besides opening and closing, they provide information on the device and help to identify the desired instance if there is more than one PQ Laser Device connected to the PC.
"""

@raise_on_error_code
def get_dll_version():
    """
    String representation of the current .dll version. 

    :returns: .dll version
    """
    return_string = string_buffer()
    dll.SEPIA2_LIB_GetVersion( return_string )
    return return_string.value

@raise_on_error_code    
def open_usb_device(dev_id):
    """
    Open exclusive access to the device connected to USB channel dev_id

    :param dev_id: the SEPIA device number, ordered from 0
    :type dev_id: int

    :returns: the product model and serial number
    """
    check_channel(dev_id, "open_device")
    product_model = string_buffer()
    serial_number = string_buffer()
    
    dll.SEPIA2_USB_OpenDevice( dev_id, product_model, serial_number)
    return product_model.value, serial_number.value

@raise_on_error_code    
def close_usb_device(dev_id):
    """
    Terminate exclusive access to the device connected to USB channel dev_id

    :param dev_id: the SEPIA device number, ordered from 0
    :type dev_id: int
    """
    check_channel(dev_id, "close_device")
    dll.SEPIA2_USB_CloseDevice(dev_id)

@raise_on_error_code
def get_state_descriptor(dev_id):
    """
    Get a description message of the device connected to USB channel dev_id

    :param dev_id: the SEPIA device number, ordered from 0
    :type dev_id: int

    :returns: concatenated string descriptors of the USB device
    """
    check_channel(dev_id, "get_state_descriptor")
    return_string = string_buffer()
    dll.SEPIA2_USB_GetStrDescriptor(dev_id, return_string )
    return return_string.value
