'''
Core functions for use in the sepia package, not intended for use outside.
'''
from config import SEPIA_DLL_PATH, SEPIA_STR_BUFFER_SIZE
from functools import wraps
import ctypes
import os

def string_buffer():
    '''    
    :returns: ctype friendly string buffer, size set in :mod:config
    '''
    return ctypes.create_string_buffer(SEPIA_STR_BUFFER_SIZE)

class SepiaDLLError(Exception):
    """
    Raised if an exception is flagged up *during* a dll call
    """
    pass

class SepiaLogicError(Exception):
    """
    Raised *before* any call to the dll if arguments are incorrect
    """
    pass


# Open the dll on import
#if not os.path.exists(SEPIA_DLL_PATH):
 #   raise SepiaLogicError("Cannot open dll on path {0}".format(SEPIA_DLL_PATH))
# try:
#     dll = ctypes.OleDLL(dll_path)
# except:
#     raise SepiaLogicError("Opening dll failed!")
dll = None
'''
The dll itself
'''

def string_buffer():
    '''    
    :returns: ctype friendly string buffer, size set in :mod:config
    '''
    return ctypes.create_string_buffer(SEPIA_STR_BUFFER_SIZE)

def check_channel(chan, name):
    '''
    The sepia box is physically limited to channels 0-7

    :param chan: channel number

    :param name: Name of calling function 

    :raises: SepiaHWError if channel is invalid
    '''
    if not chan in xrange(8):
        raise SepiaLogicError("Can't call {0} with channel {1}, must be 0-7".format(name, chan))


# handle and decode errors
def decode_error(iErr):
    '''
    Decodes an error code thrown by the hardware. 
    If the translation fails returns 
    LIB:unknown error code
        
    :param iErr: dll generated error code

    :returns: human readable error string
    '''
    str_buff = string_buffer()
    try:
        dll.SEPIA2_LIB_DecodeError(iErr, str_buff)
        return str_buff
    except WindowsError:
        return "Sepia Lib: unknown error code"

def raise_on_error_code(in_function):
    '''
    OleDll automatically detects a non-zero exit code and throws a 
    WindowsException. This decorator produces a modified function 
    that catches this, extracts and translates the error code, and throws
    a SepiaDLLError

    :param in_function: the function to wrap

    :returns: a logically equivilent function that 
              catches WindowsError exceptions thrown by ctypes, extracts
              and decodes the error code then rethrows as sepia error
    '''
    @wraps(in_function)
    def modified(*args, **kwargs):
        try:
            return in_function(args, kwargs)
        except WindowsError as e:
            raise SepiaDLLError(decode_error(e.winerr))
    return modified


