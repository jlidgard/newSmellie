from config import SEPIA_DLL_PATH, SEPIA_STR_BUFFER_SIZE
from functools import wraps
import ctypes
import os

"""
Core functions for use in the SEPIA package - not intended for use outside.
"""

def string_buffer():
    """   
    :returns: ctype string buffer, the size of which is set in :mod:config
    """
    return ctypes.create_string_buffer(SEPIA_STR_BUFFER_SIZE)

class SepiaDLLError(Exception):
    """
    Raised if an exception is flagged up *during* a call to the .dll
    """
    pass

class SepiaLogicError(Exception):
    """
    Raised *before* any call to the .dll if function arguments are incorrect
    """
    pass

# Open the .dll on import
#if not os.path.exists(SEPIA_DLL_PATH):
#  raise SepiaLogicError("Cannot open dll on path {0}".format(SEPIA_DLL_PATH))
#try:
#  dll = ctypes.OleDLL(dll_path)
#except:
#  raise SepiaLogicError("Opening dll failed!")

dll = None

"""
The ..dll itself
"""

def check_channel(chan, name):
    """
    The SEPIA Unit is physically limited to channels 0 to 7

    :param chan: channel number
    :type chan: int

    :param name: Name of calling function
    :type name: string

    :raises: :class:`.SepiaLogicError` if the channel is invalid, i.e. not between 0 and 7
    """
    if not chan in xrange(8):
        raise SepiaLogicError("Cannot call {0} with channel {1}, must be between 0 and 7".format(name, chan))

# Error Handling and Decoding
def decode_error(iErr):
    """
    Decodes an error code thrown by the hardware. 
    If the translation fails, this returns SEPIA Library: unknown error code.

    :param iErr: .dll generated error code

    :returns: error message
    :type error message: string
    """
    str_buff = string_buffer()
    try:
        dll.SEPIA2_LIB_DecodeError(iErr, str_buff)
        return str_buff
    except WindowsError:
        return "SEPIA Library: unknown error code"

def raise_on_error_code(in_function):
    """
    OleDll automatically detects a non-zero exit code and throws a WindowsException.
    This decorator produces a modified function that catches this, extracts and translates the error code, and throws a SepiaDLLError.

    :param in_function: the function to wrap

    :returns: a logically equivalent function that catches WindowsError exceptions thrown by ctypes, extracts and decodes the error code then re-throws as SepiaDLLError
    """
    @wraps(in_function)
    def modified(*args, **kwargs):
        try:
            return in_function(args, kwargs)
        except WindowsError as e:
            raise SepiaDLLError(decode_error(e.winerr))
    return modified
