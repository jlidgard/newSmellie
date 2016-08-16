from time import sleep
from ctypes import OleDLL, create_string_buffer, c_int, c_double, c_uint, c_int16, c_int32, byref
from smellie_config import PM_ADDRESS, PM_DLL_PATH, PM_STR_BUFFER_SIZE
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

# Error Handling and Decoding
def decode_error(iErr):
    """
    Decodes an error code thrown by the hardware. 
    If the translation fails, this returns Power meter DLL: unknown error code.

    :param iErr: .dll generated error code

    :returns: error message
    :type error message: string
    """
    taskHandle = GetTaskHandle()
    str_buff = create_string_buffer(PM_STR_BUFFER_SIZE)
    try:
        dll.PM100DErrorMessage(byref(taskHandle), c_int32(iErr), None, str_buff, c_int32(PM_STR_BUFFER_SIZE) )
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
def GetTaskHandle():
    """   
    :undocumented
    """
    taskHandle = c_uint(0)
    dll.GetTaskHandle( PM_ADDRESS, byref(taskHandle) )
    if (taskHandle.value == 0):
        raise PMDLLError("Task handle not found.")
    return taskHandle

@raise_on_error_code
def getAttenuation(taskHandle, attributeSetValue):
    """   
    :undocumented
    """
    retValue = c_double()
    attributeSetValue = c_int16(attributeSetValue)
    dll.PM100DGetAttenuation(byref(taskHandle), attributeSetValue, None, byref(retValue))
    return retValue.value

@raise_on_error_code
def getDarkAdjustmentState(taskHandle):
    """   
    :undocumented
    """
    retValue = c_int16()
    dll.PM100DGetDarkAdjustmentState(byref(taskHandle), None, byref(retValue))
    return retValue.value

@raise_on_error_code
def getDarkOffset(taskHandle):
    """
    :undocumented
    """
    retValue = c_double()
    dll.PM100DGetDarkOffset(byref(taskHandle), None, byref(retValue))
    return retValue.value

@raise_on_error_code
def startDarkOffsetAdjustment(taskHandle):
    """
    :undocumented
    """
    dll.PM100DStartDarkOffsetAdjustment(byref(taskHandle), None)
    return 0

@raise_on_error_code
def cancelDarkOffsetAdjustment(taskHandle):
    """
    :undocumented
    """
    dll.PM100DCancelDarkAdjustment(byref(taskHandle), None)
    return 0

@raise_on_error_code
def getBeamDiameter(taskHandle, attributeSetValue):
    """
    :undocumented
    """
    retValue = c_double()
    attributeSetValue = c_int16(attributeSetValue)
    dll.PM100DGetBeamDiameter(byref(taskHandle), attributeSetValue, None, byref(retValue))
    return retValue.value

@raise_on_error_code
def getWavelength(taskHandle, attributeSetValue):
    """
    :undocumented
    """
    retValue = c_double()
    attributeSetValue = c_int16(attributeSetValue)
    dll.PM100DGetWavelength(byref(taskHandle), attributeSetValue, None, byref(retValue))
    return retValue.value

@raise_on_error_code
def setWavelength(taskHandle, setValue):
    """
    :undocumented
    """
    setValue = c_double(setValue)
    dll.PM100DSetWavelength(byref(taskHandle), setValue, None)
    return 0

@raise_on_error_code
def getPhotodiodeResponsivity(taskHandle, attributeSetValue):
    """
    :undocumented
    """
    retValue = c_double()
    attributeSetValue = c_int16(attributeSetValue)
    dll.PM100DGetPhotodiodeResponsivity(byref(taskHandle), attributeSetValue, None, byref(retValue))
    return retValue.value

@raise_on_error_code
def getThermopileResponsivity(taskHandle, attributeSetValue):
    """
    :undocumented
    """
    retValue = c_double()
    attributeSetValue = c_int16(attributeSetValue)
    dll.PM100DGetThermopileResponsivity(byref(taskHandle), attributeSetValue, None, byref(retValue))
    return retValue.value

@raise_on_error_code   
def getPyrosensorResponsivity(taskHandle, attributeSetValue):
    """
    :undocumented
    """
    retValue = c_double()
    attributeSetValue = c_int16(attributeSetValue)
    dll.PM100DGetPyrosensorResponsivity(byref(taskHandle), attributeSetValue, None, byref(retValue))
    return retValue.value

@raise_on_error_code
def getAverageCount(taskHandle):
    """
    :undocumented
    """
    retValue = c_int16()
    dll.PM100DGetAverageCount(byref(taskHandle), None, byref(retValue))
    return retValue.value

@raise_on_error_code
def setAverageCount(taskHandle, setValue):
    """
    :undocumented
    """
    setValue = c_int16(setValue)
    dll.PM100DSetAverageCount(byref(taskHandle), setValue, None)
    return 0

@raise_on_error_code
def getCalibrationMessage(taskHandle):
    """
    :undocumented
    """
    retValue = c_double()
    message = create_string_buffer(PM_STR_BUFFER_SIZE)
    dll.PM100DGetCalibrationMessage(byref(taskHandle), None, message, PM_STR_BUFFER_SIZE)
    return message.value

@raise_on_error_code
def getSensorInformation(taskHandle):
    """
    :undocumented
    """
    
    sensorFlags = c_int16()
    sensorSubtype = c_int16()
    sensorType = c_int16()
    sensorCalibrationMessage = create_string_buffer(PM_STR_BUFFER_SIZE)
    sensorName = create_string_buffer(PM_STR_BUFFER_SIZE)
    sensorSerialNumber = create_string_buffer(PM_STR_BUFFER_SIZE)
    
    dll.PM100DGetSensorInformation(byref(taskHandle), byref(sensorFlags), byref(sensorSubtype), byref(sensorType), sensorCalibrationMessage, None, sensorName, sensorSerialNumber, PM_STR_BUFFER_SIZE, PM_STR_BUFFER_SIZE, PM_STR_BUFFER_SIZE)
    return sensorFlags.value, sensorSubtype.value, sensorType.value, sensorCalibrationMessage.value, sensorName.value, sensorSerialNumber.value

@raise_on_error_code
def measurePower(taskHandle):
    """
    :undocumented
    """
    retValue = c_double()
    dll.PM100DMeasurePower(byref(taskHandle), None, byref(retValue))
    return retValue.value

@raise_on_error_code
def getPowerAutorangeMode(taskHandle):
    """
    :undocumented
    """
    retValue = c_int()
    dll.PM100DGetPowerAutorangeMode(byref(taskHandle), None, byref(retValue))
    return retValue.value

@raise_on_error_code
def getPowerRange(taskHandle, attributeSetValue):
    """
    :undocumented
    """
    retValue = c_double()
    attributeSetValue = c_int16(attributeSetValue)
    dll.PM100DGetPowerRange(byref(taskHandle), attributeSetValue, None, byref(retValue))
    return retValue.value

@raise_on_error_code
def getPowerReferenceState(taskHandle):
    """
    :undocumented
    """
    retValue = c_int()
    dll.PM100DGetPowerReferenceState(byref(taskHandle), None, byref(retValue))
    return retValue.value

@raise_on_error_code
def getPhotodiodeInputFilterState(taskHandle):
    """
    :undocumented
    """
    retValue = c_int()
    dll.PM100DGetPhotodiodeInputFilterState(byref(taskHandle), None, byref(retValue))
    return retValue.value
    
@raise_on_error_code
def getPowerReference(taskHandle, attributeSetValue):
    """
    :undocumented
    """
    retValue = c_double()
    attributeSetValue = c_int16(attributeSetValue)
    dll.PM100DGetPowerReference(byref(taskHandle), attributeSetValue, None, byref(retValue))
    return retValue.value

@raise_on_error_code
def getPowerUnit(taskHandle):
    """
    :undocumented
    """
    retValue = c_int16()
    dll.PM100DGetPowerUnit(byref(taskHandle), None, byref(retValue))
    return retValue.value

@raise_on_error_code
def setPowerUnit(taskHandle, setValue):
    """
    :undocumented
    """
    setValue = c_int16(setValue)
    dll.PM100DSetPowerUnit(byref(taskHandle), setValue, None)
    return 0
    
@raise_on_error_code
def getDisplayContrast(taskHandle):
    """
    :undocumented
    """
    retValue = c_double()
    dll.PM100DGetDisplayContrast(byref(taskHandle), None, byref(retValue))
    return retValue.value

@raise_on_error_code
def setDisplayContrast(taskHandle, setValue):
    """
    :undocumented
    """
    setValue = c_double(setValue)
    dll.PM100DSetDisplayContrast(byref(taskHandle), setValue, None)
    return 0
    
@raise_on_error_code
def getDisplayBrightness(taskHandle):
    """
    :undocumented
    """
    retValue = c_double()
    dll.PM100DGetDisplayBrightness(byref(taskHandle), None, byref(retValue))
    return retValue.value
    
@raise_on_error_code
def setDisplayBrightness(taskHandle, setValue):
    """
    :undocumented
    """
    setValue = c_double(setValue)
    dll.PM100DSetDisplayBrightness(byref(taskHandle), setValue, None)
    return 0
    
@raise_on_error_code
def identificationQuery(taskHandle):
    """
    :undocumented
    """
    firmwareRevision = create_string_buffer(PM_STR_BUFFER_SIZE)
    serialNumber = create_string_buffer(PM_STR_BUFFER_SIZE)
    manufacturerName = create_string_buffer(PM_STR_BUFFER_SIZE)
    deviceName = create_string_buffer(PM_STR_BUFFER_SIZE)
    dll.PM100DIdentificationQuery(byref(taskHandle), firmwareRevision, serialNumber, None, manufacturerName, deviceName, c_int32(PM_STR_BUFFER_SIZE), c_int32(PM_STR_BUFFER_SIZE), c_int32(PM_STR_BUFFER_SIZE), c_int32(PM_STR_BUFFER_SIZE) )
    return firmwareRevision.value, serialNumber.value, manufacturerName.value, deviceName.value

@raise_on_error_code
def selfTest(taskHandle):
    """
    :undocumented
    """
    selfTestMessage = create_string_buffer(PM_STR_BUFFER_SIZE)
    selfTestResult = c_int16()
    dll.PM100DSelfTest(byref(taskHandle), None, selfTestResult, selfTestMessage, c_int32(PM_STR_BUFFER_SIZE) )
    return selfTestResult.value, selfTestMessage.value

@raise_on_error_code
def portOpen(COMPort, iDQueryDoQuery, resetDevice):
    """
    :returns: ctype string buffer, the size of which is set in :mod:config
    """
    iDQueryDoQuery = c_int16(iDQueryDoQuery)
    resetDevice = c_int16(resetDevice)
    taskHandle = c_uint()
    dll.Initialise(COMPort, iDQueryDoQuery, resetDevice, byref(taskHandle) )
    return taskHandle

@raise_on_error_code
def portClose(taskHandle):
    """   
    :returns: ctype string buffer, the size of which is set in :mod:config
    """
    dll.PM100DClose( byref(taskHandle) )

