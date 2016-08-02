from time import sleep
from ctypes import OleDLL, create_string_buffer, c_double, c_int16, c_int32, byref
from smellie_config import PM_DLL_PATH, PM_STR_BUFFER_SIZE
from functools import wraps
import os

"""
Core functions for use in the Power Meter package - not intended for use outside.
"""

class PMDLLError(Exception):
    """
    Raised if an exception is flagged up *during* a call to the .dll
    """
    pass

class PMLogicError(Exception):
    """
    Raised *before* any call to the .dll if function arguments are incorrect
    """
    pass

# Open the .dll on import
if not os.path.exists(PM_DLL_PATH):
    raise PMLogicError("Cannot open dll on path {0}".format(PM_DLL_PATH))
try:
    dll = OleDLL(PM_DLL_PATH)
except Exception as e:
    raise PMLogicError("Opening dll failed! : {0}".format(str(e)))

#dll = cdll.LoadLibrary("./powerMeterUtil.dll")   

# Error Handling and Decoding
def decode_error(COMPort, iErr):
    """
    Decodes an error code thrown by the hardware. 
    If the translation fails, this returns SEPIA Library: unknown error code.

    :param iErr: .dll generated error code

    :returns: error message
    :type error message: string
    """
    str_buff = create_string_buffer(PM_STR_BUFFER_SIZE)
    try:
        dll.DecodeError(COMPort, c_int32(iErr), str_buff, c_int32(PM_STR_BUFFER_SIZE) )
        return str_buff.value
    except WindowsError:
        return "PM Library: unknown error code {0}".format(iErr)

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
            return in_function(*args, **kwargs)
        except WindowsError as e:
            raise PMDLLError(decode_error(e.winerror))
    return modified
    
@raise_on_error_code
def getBeamDiameter(COMPort):
    """   
    :returns: ctype string buffer, the size of which is set in :mod:config
    """
    retValue = c_double(0)
    dll.GetBeamDiameter(COMPort, byref(retValue))
    return retValue.value
    
@raise_on_error_code
def getPower(COMPort):
    """   
    :returns: ctype string buffer, the size of which is set in :mod:config
    """
    retValue = c_double(0)
    dll.GetPower(COMPort, byref(retValue))
    return retValue.value

@raise_on_error_code
def getWavelength(COMPort):
    """   
    :returns: ctype string buffer, the size of which is set in :mod:config
    """
    retValue = c_double(0)
    dll.GetWavelength(COMPort, byref(retValue))
    return retValue.value
    
@raise_on_error_code
def setPowerRange(COMPort,setValue):
    """   
    :returns: ctype string buffer, the size of which is set in :mod:config
    """
    value = c_double(setValue)  
    dll.setPowerRange( COMPort, value )
    #if (errorCode==0):
    #    logging.info( 'Set Power Range: {}'.format(setValue) )
    #else:
    #    logging.error( 'Could not set power range. ErrorCode: {}'.format( errorCode ) )

@raise_on_error_code
def getDarkOffset(COMPort):
    """   
    :returns: ctype string buffer, the size of which is set in :mod:config
    """
    retValue = c_double(0)
    dll.GetDarkOffset(COMPort, byref(retValue))
    return retValue.value
    
@raise_on_error_code
def setDarkOffsetCancel(COMPort):
    """   
    :returns: ctype string buffer, the size of which is set in :mod:config
    """
    dll.SetDarkOffsetCancel(COMPort)
    
@raise_on_error_code
def setDarkOffset(COMPort):
    """   
    :returns: ctype string buffer, the size of which is set in :mod:config
    """
    dll.SetDarkOffset(COMPort)
    sleep(5)

@raise_on_error_code
def setWavelength(COMPort, setValue):
    """   
    :returns: ctype string buffer, the size of which is set in :mod:config
    """
    value = c_double(setValue)
    minValue = 300
    maxValue = 1000
    
    if (setValue>=minValue or setValue<=maxValue):
        dll.SetWavelength( COMPort, value )
        checkValue = getWavelength(COMPort)

        if (checkValue!=setValue):
            raise PMLogicError('Unable to Set Wavelength. Tried: {}, Current: {}'.format(setValue,checkValue) )
    else:
        raise PMLogicError('Unable to Set Wavelength. Tried: {}. Must be greater than {} and less than {}.'.format(value,minValue,maxValue) )  

@raise_on_error_code
def portOpen(COMPort):
    """   
    :returns: ctype string buffer, the size of which is set in :mod:config
    """
    selfTestResult = c_int16(0)
    message = create_string_buffer(PM_STR_BUFFER_SIZE)
    dll.Initialise(COMPort, byref(selfTestResult), message, c_int32(PM_STR_BUFFER_SIZE))
    return selfTestResult.value, message.value 

@raise_on_error_code
def portClose(COMPort):
    """   
    :returns: ctype string buffer, the size of which is set in :mod:config
    """
    dll.Shutdown(COMPort)

