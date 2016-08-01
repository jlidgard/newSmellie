from sepia import dll, raise_on_error_code
from ctypes import c_int32

"""
Basic Oscillator Functions (SOM)
The following list represents the API of the basic oscillator module SOM 828.
"""

@raise_on_error_code
def get_freq_trig_mode(dev_id, slot_id):
    """
    Get the current frequency setting for the reference source of the given SOM

    :param dev_id: the SEPIA device number, ordered from 0
    :type dev_id: int

    :param slot_id: the slot number, between 000 and 989
    :type slot_id: int

    :returns: freq_trig_mode
    :type freq_trig_mode: int
    """
    mode = c_int32()
    dll.SEPIA2_SOM_GetTrigMode(dev_id, slot_id, mode)
    return mode.value
