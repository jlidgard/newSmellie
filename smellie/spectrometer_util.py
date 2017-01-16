from time import sleep
from ctypes import OleDLL, create_string_buffer, c_double, c_int16, c_int32, byref, c_uint64
from smellie_config import SPEC_DLL_PATH, SPEC_STR_BUFFER_SIZE
from functools import wraps
import os

"""
Core functions for use in the Ocean Optics Spectrometer package - not intended for use outside.
"""

def string_buffer():
    """   
    :returns: ctype string buffer, the size of which is set in :mod:config
    """
    return create_string_buffer(SPEC_STR_BUFFER_SIZE)
    
class SpecDLLError(Exception):
    """
    Raised if an exception is flagged up *during* a call to the .dll
    """
    pass

class SpecLogicError(Exception):
    """
    Raised *before* any call to the .dll if function arguments are incorrect
    """
    pass

# Open the .dll on import
if not os.path.exists(SPEC_DLL_PATH):
    raise SpecLogicError("Cannot open dll on path {0}".format(SPEC_DLL_PATH))
try:
    dll = OleDLL(SPEC_DLL_PATH)
except Exception as e:
    raise SpecLogicError("Opening dll failed! : {0}".format(str(e))) 

# Error Handling and Decoding
def decode_error(COMPort, iErr):
    """
    Decodes an error code thrown by the hardware. 
    If the translation fails, this returns: unknown error code.

    :param iErr: .dll generated error code

    :returns: error message
    :type error message: string
    """
    str_buff = create_string_buffer(SPEC_STR_BUFFER_SIZE)
    try:
        #dll.OOUtil_DecodeError(COMPort, c_int32(iErr), str_buff, c_int32(SPEC_STR_BUFFER_SIZE) )
        return str_buff.value
    except WindowsError:
        return "Spec Library: unknown error code {0}".format(iErr)

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
            raise SpecDLLError(decode_error(e.winerror))
    return modified
    
@raise_on_error_code
def createWrapper():
    """   
    :undocumented
    """
    #uint64_t __cdecl Wrapper_Create(void);
    wrapper = dll.OOUtil_Wrapper_Create()
    return wrapper

def destroyWrapper(wrapper):
    """   
    :undocumented
    """
    #void __cdecl Wrapper_Destroy(uint64_t Wrapper);
    dll.OOUtil_Wrapper_Destroy(wrapper)

def openAllSpectrometers(wrapper):
    """   
    :undocumented
    """
    #void __cdecl Wrapper_openAllSpectrometers(uint64_t WrapperIn, int32_t *NumberOfSpectrometers);
    #wrapperIn = c_uint64(wrapper)
    numberOfSpectrometers = c_int32(-1)
    dll.OOUtil_Wrapper_openAllSpectrometers(wrapper, byref(numberOfSpectrometers) )
    return numberOfSpectrometers.value

def closeAllSpectrometers(wrapper):
    """   
    :undocumented
    """
    #void __cdecl Wrapper_closeAllSpectrometers(uint64_t WrapperIn);
    #wrapperIn = c_uint64(wrapper)
    dll.OOUtil_Wrapper_closeAllSpectrometers(wrapper)

def getFirmwareVersion(wrapper):
    """   
    :undocumented
    """
    #void __cdecl Wrapper_getFirmwareVersion(uint64_t Wrapper, int32_t Index, char Firmware[], int32_t len);
    #wrapperIn = c_uint64(wrapper)
    index = c_int32(0)
    message = string_buffer()
    dll.OOUtil_Wrapper_getFirmwareVersion(wrapper, index, message, c_int32(SPEC_STR_BUFFER_SIZE) )
    return message.value

def getName(wrapper):
    """   
    :undocumented
    """
    #void __cdecl Wrapper_getName(int32_t Index, uint64_t Wrapper, char SpectrometerName[], int32_t len);
    #wrapperIn = c_uint64(wrapper)
    index = c_int32(0)
    message = string_buffer()
    dll.OOUtil_Wrapper_getName(index, wrapper, message, c_int32(SPEC_STR_BUFFER_SIZE) )
    return message.value

def getSerialNumber(wrapper):
    """   
    :undocumented
    """
    #void __cdecl Wrapper_getSerialNumber(uint64_t Wrapper, int32_t Index, char SerialNumber[], int32_t len);
    #wrapperIn = c_uint64(wrapper)
    index = c_int32(0)
    message = string_buffer()
    dll.OOUtil_Wrapper_getSerialNumber( wrapper, index, message, c_int32(SPEC_STR_BUFFER_SIZE) )
    return message.value

def getIntegrationTime(wrapper):
    """   
    :undocumented
    """
    #int32_t __cdecl Wrapper_getIntegrationTime(uint64_t Wrapper, int32_t Index);
    #wrapperIn = c_uint64(wrapper)
    index = c_int32(0)
    retValue = dll.OOUtil_Wrapper_getIntegrationTime(wrapper, index)
    return retValue.value

def setIntegrationTime(wrapper,value):
    """   
    :undocumented
    """
    #void __cdecl Wrapper_setIntegrationTime(uint64_t WrapperIn, int32_t Index, int32_t IntegrationTime);
    #wrapperIn = c_uint64(wrapper)
    index = c_int32(0)
    integrationTime = c_int32(value)
    minIntegrationTime = getMinimumIntegrationTime(wrapper)
    maxIntegrationTime = getMaximumIntegrationTime(wrapper)
    
    if (value>=minIntegrationTime or value<=maxIntegrationTime):
        dll.OOUtil_Wrapper_setIntegrationTime(wrapper, index, integrationTime)
        #int32_t __cdecl Wrapper_getIntegrationTime(uint64_t Wrapper, int32_t Index);
        retValue = dll.OOUtil_Wrapper_getIntegrationTime(wrapper, index)
        if (retValue!=integrationTime.value):
            raise SpecDLLError( 'Unable to Set Integration Time. Tried: {}, Current: {}'.format(integrationTime.value,retValue) )
    else:
        raise SpecLogicError( 'Unable to Set Integration Time. Tried: {}. Must be greater than {} and less than {}.'.format(integrationTime.value,minIntegrationTime,maxIntegrationTime) )

def getScansToAverage(wrapper):
    """   
    :undocumented
    """
    #int32_t __cdecl Wrapper_getScansToAverage(uint64_t Wrapper, int32_t Index);
    #wrapperIn = c_uint64(wrapper)
    index = c_int32(0)
    retValue = dll.OOUtil_Wrapper_getScansToAverage(wrapper, index)
    return retValue

def setScansToAverage(wrapper,value):
    """   
    :undocumented
    """
    #void __cdecl Wrapper_setScansToAverage(uint64_t WrapperIn, int32_t Index, int32_t Average);
    #wrapperIn = c_uint64(wrapper)
    index = c_int32(0)
    average = c_int32(value)
    dll.OOUtil_Wrapper_setScansToAverage(wrapper, index, average)
    
    #int32_t __cdecl Wrapper_getScansToAverage(uint64_t Wrapper, int32_t Index);
    retValue = dll.OOUtil_Wrapper_getScansToAverage(wrapper, index)
    if (retValue!=average.value):
        raise SpecDLLError( 'Unable to Set Scans to Average. Tried: {}, Current: {}'.format(average.value,retValue) )

def getSpectrum(wrapper):
    """   
    :undocumented
    """
    #void __cdecl Wrapper_getSpectrum  (uint64_t Wrapper, int32_t Index, double SpectrumValues[], int32_t *Length, int32_t len);
    #wrapperIn = c_uint64(wrapper)
    index = c_int32(0)
    length = int(getNumberOfPixels(wrapper))
    spectrumLength = c_int32(-1)
    spectrumValues = (c_double*length)()
    dll.OOUtil_Wrapper_getSpectrum(wrapper, index, byref(spectrumValues), byref(spectrumLength), c_int32(length) )
    return list(spectrumValues)

def getWavelengths(wrapper):
    """   
    :undocumented
    """
    #void __cdecl Wrapper_getWavelengths(uint64_t Wrapper, int32_t Index, double WLValues[], int32_t *Length, int32_t len);
    #wrapperIn = c_uint64(wrapper)
    index = c_int32(0)
    length = int(getNumberOfPixels(wrapper))
    wavelengthLength = c_int32(-1)
    wavelengthValues = (c_double*length)()

    dll.OOUtil_Wrapper_getWavelengths(wrapper, index, byref(wavelengthValues), byref(wavelengthLength), c_int32(length) )
    #print "Get Wavelengths:"
    #print list(wavelengthValues)
    return list(wavelengthValues)

def getFeatureControllerIrradianceCalibrationFactor(wrapper):
    """   
    :undocumented
    """
    #uint64_t __cdecl Wrapper_getFeatureControllerIrradianceCalibrationFactor(uint64_t Wrapper, int32_t index);
    #wrapperIn = c_uint64(wrapper)
    index = c_int32(0)
    retValue = dll.OOUtil_Wrapper_getFeatureControllerIrradianceCalibrationFactor(wrapper, index)
    return retValue.value

def getFeatureControllerExternalTriggerDelay(wrapper):
    """   
    :undocumented
    """
    #uint64_t __cdecl Wrapper_getFeatureControllerExternalTriggerDelay(uint64_t Wrapper, int32_t Index);
    #wrapperIn = c_uint64(wrapper)
    index = c_int32(0)
    retValue = dll.OOUtil_Wrapper_getFeatureControllerExternalTriggerDelay(wrapper, index)
    return retValue

def getExternalTriggerMode(wrapper):
    """   
    :undocumented
    """
    #int32_t __cdecl Wrapper_getExternalTriggerMode(uint64_t Wrapper, int32_t Index);
    #wrapperIn = c_uint64(wrapper)
    index = c_int32(0)
    retValue = dll.OOUtil_Wrapper_getExternalTriggerMode(wrapper, index)
    return retValue.value

def setExternalTriggerMode(wrapper,value):
    """   
    :undocumented
    """
    #void __cdecl Wrapper_setExternalTriggerMode(uint64_t WrapperIn, int32_t Index, int32_t TriggerMode);
    #wrapperIn = c_uint64(wrapper)
    index = c_int32(0)
    triggerMode = c_int32(value)
    dll.OOUtil_Wrapper_setExternalTriggerMode(wrapper, index, triggerMode)

    #int32_t __cdecl Wrapper_getExternalTriggerMode(uint64_t Wrapper, int32_t Index);
    retValue = dll.OOUtil_Wrapper_getExternalTriggerMode(wrapper, index)
    if (retValue!=triggerMode.value):
        raise SpecDLLError( 'Unable to Set External Trigger Mode. Tried: {}, Current: {}'.format(triggerMode.value,retValue) )

def setCorrectForElectricalDark(wrapper,value):
    """   
    :undocumented
    """
    #void __cdecl Wrapper_setCorrectForElectricalDark(uint64_t WrapperIn, int32_t Index, int32_t OnOff);
    wrapperIn = c_uint64(wrapper)
    index = c_int32(0)
    flag = c_int32(value)
    if (flag.value==0 or flag.value==1):
        dll.OOUtil_Wrapper_setCorrectForElectricalDark(wrapper, index, flag)
    else:
        raise SpecLogicError( 'Unable to Set Correct For Electrical Dark. Tried: {}. Note: must be 0 or 1.'.format(flag.value) )

def setCorrectForDetectorNonlinearity(wrapper,value):
    """   
    :undocumented
    """
    #void __cdecl Wrapper_setCorrectForDetectorNonlinearity(uint64_t WrapperIn, int32_t Index, int32_t OnOff);
    #wrapperIn = c_uint64(wrapper)
    index = c_int32(0)
    flag = c_int32(value)
    if (flag.value==0 or flag.value==1):
        dll.OOUtil_Wrapper_setCorrectForDetectorNonlinearity(wrapper, index, flag)
    else:
        raise SpecLogicError( 'Unable to Set Correct For Detector Nonlinearity. Tried: {}. Note: must be 0 or 1.'.format(flag.value) )

def getBoxcarWidth(wrapper):
    """   
    :undocumented
    """
    #int32_t __cdecl Wrapper_getBoxcarWidth(uint64_t Wrapper, int32_t Index);
    #wrapperIn = c_uint64(wrapper)
    index = c_int32(0)
    retValue = dll.OOUtil_Wrapper_getBoxcarWidth(wrapper, index)
    return retValue.value

def setBoxcarWidth(wrapper,value):
    """   
    :undocumented
    """
    #void __cdecl Wrapper_setBoxcarWidth(uint64_t WrapperIn, int32_t Index, int32_t BoxcarWidth);
    #wrapperIn = c_uint64(wrapper)
    index = c_int32(0)
    boxcarWidth = c_int32(value)
    dll.OOUtil_Wrapper_setBoxcarWidth(wrapper, index, boxcarWidth)

    #int32_t __cdecl Wrapper_getBoxcarWidth(uint64_t Wrapper, int32_t Index);
    retValue = dll.OOUtil_Wrapper_getBoxcarWidth(wrapper, index)
    if (retValue!=boxcarWidth.value):
        raise SpecDLLError( 'Unable to Set Boxcar Width. Tried: {}, Current: {}'.format(boxcarWidth.value,retValue) )

def getMaximumIntensity(wrapper):
    """   
    :undocumented
    """
    #int32_t __cdecl Wrapper_getMaximumIntensity(uint64_t Wrapper, int32_t Index);
    #wrapperIn = c_uint64(wrapper)
    index = c_int32(0)
    retValue = dll.OOUtil_Wrapper_getMaximumIntensity(wrapper, index)
    return retValue

def getMaximumIntegrationTime(wrapper):
    """   
    :undocumented
    """
    #int32_t __cdecl Wrapper_getMaximumIntegrationTime(uint64_t Wrapper, int32_t Index);
    #wrapperIn = c_uint64(wrapper)
    index = c_int32(0)
    retValue = dll.OOUtil_Wrapper_getMaximumIntegrationTime(wrapper, index)
    return retValue

def getMinimumIntegrationTime(wrapper):
    """   
    :undocumented
    """
    #int32_t __cdecl Wrapper_getMinimumIntegrationTime(uint64_t Wrapper, int32_t Index);
    #wrapperIn = c_uint64(wrapper)
    index = c_int32(0)
    retValue = dll.OOUtil_Wrapper_getMinimumIntegrationTime(wrapper, index)
    return retValue

def getNumberOfDarkPixels(wrapper):
    """   
    :undocumented
    """
    #int32_t __cdecl Wrapper_getNumberOfDarkPixels(uint64_t Wrapper, int32_t Index);
    #wrapperIn = c_uint64(wrapper)
    index = c_int32(0)
    retValue = dll.OOUtil_Wrapper_getNumberOfDarkPixels(wrapper, index)
    return retValue

def getNumberOfPixels(wrapper):
    """   
    :undocumented
    """
    #int32_t __cdecl Wrapper_getNumberOfPixels(uint64_t Wrapper, int32_t Index);
    #wrapperIn = c_uint64(wrapper)
    index = c_int32(0)
    retValue = dll.OOUtil_Wrapper_getNumberOfPixels(wrapper, index)
    return retValue

def isSaturated(wrapper):
    """   
    :undocumented
    """
    #uint8_t __cdecl Wrapper_isSaturated(uint64_t Wrapper, int32_t Index);
    #wrapperIn = c_uint64(wrapper)
    index = c_int32(0)
    retValue = dll.OOUtil_Wrapper_isSaturated(wrapper, index)
    return retValue

def getLastException(wrapper):
    """   
    :undocumented
    """
    #void __cdecl Wrapper_getLastException(uint64_t Wrapper, char LastException[], int32_t len);
    #wrapperIn = c_uint64(wrapper)
    message = string_buffer()
    dll.OOUtil_Wrapper_getLastException(wrapper, message, c_int32(SPEC_STR_BUFFER_SIZE) )
    return message.value

def destroyExternalTriggerDelay():
    """   
    :undocumented
    """
    #void __cdecl ExternalTriggerDelay_Destroy(void);
    dll.OOUtil_ExternalTriggerDelay_Destroy()

def getExternalTriggerDelayMaximum(externalTriggerDelay):
    """   
    :undocumented
    """
    #int32_t __cdecl ExternalTriggerDelay_getExternalTriggerDelayMaximum(uint64_t ExternalTriggerDelay);
    externalTriggerDelayIn = c_uint64(externalTriggerDelay)
    retValue = dll.OOUtil_ExternalTriggerDelay_getExternalTriggerDelayMaximum(externalTriggerDelayIn)
    return retValue

def getExternalTriggerDelayMinimum(externalTriggerDelay):
    """   
    :undocumented
    """
    #int32_t __cdecl ExternalTriggerDelay_getExternalTriggerDelayMinimum(uint32_t ExternalTriggerDelay);
    externalTriggerDelayIn = c_uint64(externalTriggerDelay)
    retValue = dll.OOUtil_ExternalTriggerDelay_getExternalTriggerDelayMinimum(externalTriggerDelayIn)
    return retValue

def setExternalTriggerDelay(externalTriggerDelay,value):
    """   
    :undocumented
    """
    #void __cdecl ExternalTriggerDelay_setExternalTriggerDelay(uint64_t ExternalTriggerDelayIn, int32_t microseconds);
    externalTriggerDelayIn = c_uint64(externalTriggerDelay)
    delayTime = c_int32(value)
    minTime = getExternalTriggerDelayMinimum(externalTriggerDelay)
    maxTime = getExternalTriggerDelayMaximum(externalTriggerDelay)
    if (value>=minTime or value<=maxTime):
        dll.OOUtil_ExternalTriggerDelay_setExternalTriggerDelay(externalTriggerDelayIn, delayTime)
    else:
        raise SpecLogicError( 'Unable to Set External Trigger Delay. Tried: {}. Must be greater than {} and less than {}.'.format(delayTime.value,minTime,maxTime) )
