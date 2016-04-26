from _sepia import dll, raise_on_error_code
import ctypes
"""
Basic Oscillator Functions (SOM)
The following list represents the API of the basic oscillator module SOM 828.
"""
@raise_on_error_code
def get_freq_trig_mode(dev_id, slot_id):
    """get_freq_trig_mode(dev_id, slot_id)
    Current frequency setting for the reference source of given SOM

    :param dev_id: the sepia device number (ordered from 0)
    :type dev_id: int

    :param slot_id: slot number, integer 000-989
    :type dev_id: int

    :returns: freq_trig_mode of this module
    :type freq_trig_mode: int
    """
    mode = ctypes.c_int32()
    dll.SEPIA2_SOM_GetTrigMode(dev_id, slot_id, mode)
    return mode
