from time import sleep
from ctypes import Structure, OleDLL, create_string_buffer, c_char_p, c_double, c_int16, c_int32, c_uint16, c_uint32, c_uint8,byref
from smellie_config import SK_COM_PORT, SK_DLL_PATH, SK_STR_BUFFER_SIZE
from functools import wraps
import os

"""
Core functions for use in the SuperK package - not intended for use outside.
"""

class statusBitStructure(Structure):
        _fields_ = [("bit0", c_int16),("bit1", c_int16),("bit2", c_int16),("bit3", c_int16),("bit4", c_int16),("bit5", c_int16), ("bit6", c_int16),("bit7", c_int16),("bit8", c_int16),("bit9", c_int16),("bit10", c_int16),("bit11", c_int16),("bit12", c_int16),("bit13", c_int16),("bit14", c_int16),("bit15", c_int16)]

class superKControlStructure(Structure):
        _fields_ = [("trigLevelSetpointmV", c_uint16),("displayBacklightPercent", c_uint8),("trigMode", c_uint8),("internalPulseFreqHz", c_uint16),("burstPulses", c_uint16),("watchdogIntervalSec", c_uint8),("internalPulseFreqLimitHz", c_uint32)]

# for loading NI LV dll's see NI white paper http://www.ni.com/white-paper/8911/en/
# http://digital.ni.com/public.nsf/allkb/A3804F88FCDB1E6286257CE00043C1A7
# https://decibel.ni.com/content/docs/DOC-9076
# https://decibel.ni.com/content/docs/DOC-9079

def string_buffer():
    """   
    :returns: ctype string buffer, the size of which is set in :mod:config
    """
    return create_string_buffer(SK_STR_BUFFER_SIZE)

class SuperKDLLError(Exception):
    """
    Raised if an exception is flagged up *during* a call to the .dll
    """
    pass

class SuperKLogicError(Exception):
    """
    Raised *before* any call to the .dll if function arguments are incorrect
    """
    pass

# Open the .dll on import
if not os.path.exists(SK_DLL_PATH):
    raise SuperKLogicError("Cannot open dll on path {0}".format(SK_DLL_PATH))
try:
    dll = OleDLL(SK_DLL_PATH)
except Exception as e:
    raise SuperKLogicError("Opening dll failed! : {0}".format(str(e))) 

# Error Handling and Decoding
def decode_error(iErr):
    """
    Decodes an error code thrown by the hardware. 
    If the translation fails, this returns: unknown error code.

    :param iErr: .dll generated error code

    :returns: error message
    :type error message: string
    """
    str_buff = create_string_buffer(SK_STR_BUFFER_SIZE)
    try:
        #dll.DecodeError(c_int32(iErr), str_buff, c_int32(SK_STR_BUFFER_SIZE) )
        return str_buff.value
    except WindowsError:
        return "SuperK Library: unknown error code {0}".format(iErr)

def raise_on_error_code(in_function):
    """
    OleDll automatically detects a non-zero exit code and throws a WindowsException.
    This decorator produces a modified function that catches this, extracts and translates the error code, and throws a SuperKDLLError.

    :param in_function: the function to wrap

    :returns: a logically equivalent function that catches WindowsError exceptions thrown by ctypes, extracts and decodes the error code then re-throws as SepiaDLLError
    """
    @wraps(in_function)
    def modified(*args, **kwargs):
        try:
            return in_function(*args, **kwargs)
        except WindowsError as e:
            raise SuperKDLLError(decode_error(e.winerror))
    return modified

@raise_on_error_code
def portOpen(COMPort):
    """
    undocumented
    """
    dll.PortOpen(COMPort)

@raise_on_error_code
def portClose(COMPort):
    """
    undocumented
    """
    dll.PortClose(COMPort)

@raise_on_error_code
def getSuperKInfo(COMPort):
    """
    undocumented
    """
    serial = string_buffer()
    moduleType = c_int32(0)
    firmware = c_uint16(0)
    versionInfo = string_buffer()
    dll.GetSuperKInfo(COMPort, serial, SK_STR_BUFFER_SIZE, byref(moduleType), byref(firmware), versionInfo, SK_STR_BUFFER_SIZE)
    return firmware.value, versionInfo.value, format(moduleType.value,'02X'), serial.value

@raise_on_error_code
def getVariaInfo(COMPort):
    """
    undocumented
    """
    serial = string_buffer()
    moduleType = c_int32(0)
    firmware = c_uint16(0)
    versionInfo = string_buffer()
    dll.GetVariaInfo(COMPort, serial, SK_STR_BUFFER_SIZE, byref(moduleType), byref(firmware), versionInfo, SK_STR_BUFFER_SIZE)
    return firmware.value, versionInfo.value, format(moduleType.value,'02X'), serial.value

@raise_on_error_code
def getVariaReadings(COMPort):
    """
    undocumented
    """
    monitorInput = c_double(0)
    dll.GetVariaReadings(COMPort, byref(monitorInput))
    return monitorInput.value

@raise_on_error_code
def getSuperKReadings(COMPort):
    """
    undocumented
    """
    opticalPulseFreqkHz = c_double(0)
    actualInternalTrigFreqkHz = c_double(0)
    powerReadoutPercent = c_uint8(0)
    heatSinkTempC = c_double(0)
    supplyVoltagemV = c_double(0)
    displayInfo = string_buffer()
    dll.GetSuperKReadings(COMPort, byref(opticalPulseFreqkHz), byref(actualInternalTrigFreqkHz), byref(powerReadoutPercent), byref(heatSinkTempC), byref(supplyVoltagemV), displayInfo, SK_STR_BUFFER_SIZE )
    return opticalPulseFreqkHz.value, actualInternalTrigFreqkHz.value, powerReadoutPercent.value, heatSinkTempC.value, supplyVoltagemV.value, displayInfo.value

@raise_on_error_code
def getVariaStatusBits(COMPort):
    """
    undocumented
    """
    bitMaskDecimal = c_int32(0)
    bitCluster = statusBitStructure()
    dll.GetVariaStatusBits(COMPort, byref(bitMaskDecimal), bitCluster)    
    return bitCluster

@raise_on_error_code
def printVariaStatusBits(bitCluster,option="ALL"):
    """
    undocumented
    """
    print "Varia Bit Status:"
    if (option=="ALL"):
        if (bitCluster.bit1 == 0): print "\tbit 1: OFF (Interlock Off)" 
        elif (bitCluster.bit1 == 1): print "\tbit 1: ON (Interlock Off)" 
        else: print "\tbit 1: OutOfRange (Interlock On)"
        
        if (bitCluster.bit2 == 0): print "\tbit 2: OFF (InterlockLoopIn)" 
        elif (bitCluster.bit2 == 1): print "\tbit 2: ON (InterlockLoopIn)" 
        else: print "\tbit 2: OutOfRange (InterlockLoopIn)"
        
        if (bitCluster.bit3 == 0): print "\tbit 3: OFF (InterlockLoopOut)" 
        elif (bitCluster.bit3 == 1): print "\tbit 3: ON (InterlockLoopOut)" 
        else: print "\tbit 3: OutOfRange (InterlockLoopOut)"
        
        if (bitCluster.bit5 == 0): print "\tbit 5: OFF (SupplyVoltageLow)" 
        elif (bitCluster.bit5 == 1): "\tbit 5: ON (SupplyVoltageLow)" 
        else: print "\tbit 5: OutOfRange (SupplyVoltageLow)"
        
        if (bitCluster.bit6 == 0): print "\tbit 6: OFF (ModuleTempRange)" 
        elif (bitCluster.bit6 == 1): print "\tbit 6: ON (ModuleTempRange)" 
        else: print "\tbit 6: OutOfRange (ModuleTempRange)"
        
        if (bitCluster.bit8 == 0): print "\tbit 8: OFF (ShutterSensor1)" 
        elif (bitCluster.bit8 == 1): print "\tbit 8: ON (ShutterSensor1)" 
        else: print "\tbit 8: OutOfRange (ShutterSensor1)"
        
        if (bitCluster.bit9 == 0): print "\tbit 9: OFF (ShutterSensor2)" 
        elif (bitCluster.bit9 == 1): print "\tbit 9: ON (ShutterSensor2)" 
        else: print "\tbit 9: OutOfRange (ShutterSensor2)"
        
        if (bitCluster.bit12 == 0): print "\tbit 12: OFF (Filter1Moving)" 
        elif (bitCluster.bit12 == 1): print "\tbit 12: ON (Filter1Moving)" 
        else: print "\tbit 12: OutOfRange (Filter1Moving)"
        
        if (bitCluster.bit13 == 0): print "\tbit 13: OFF (Filter2Moving)" 
        elif (bitCluster.bit13 == 1): print "\tbit 13: ON (Filter2Moving)" 
        else: print "\tbit 13: OutOfRange (Filter2Moving)"
        
        if (bitCluster.bit14 == 0): print "\tbit 14: OFF (Filter3Moving)" 
        elif (bitCluster.bit14 == 1): print "\tbit 14: ON (Filter3Moving)" 
        else: print "\tbit 14: OutOfRange (Filter3Moving)"
        
        if (bitCluster.bit15 == 0): print "\tbit 15: OFF (ErrorCodePresent)" 
        elif (bitCluster.bit15 == 1): print "\tbit 15: ON (ErrorCodePresent)" 
        else: print "\tbit 15: OutOfRange (ErrorCodePresent)"
    if (option=="ON"):
        if (bitCluster.bit1 == 0): pass
        elif (bitCluster.bit1 == 1): print "\tbit 1: ON (Interlock Off)" 
        else: print "\tbit 1: OutOfRange (Interlock On)"
        
        if (bitCluster.bit2 == 0): pass 
        elif (bitCluster.bit2 == 1): print "\tbit 2: ON (InterlockLoopIn)" 
        else: print "\tbit 2: OutOfRange (InterlockLoopIn)"
        
        if (bitCluster.bit3 == 0): pass
        elif (bitCluster.bit3 == 1): print "\tbit 3: ON (InterlockLoopOut)" 
        else: print "\tbit 3: OutOfRange (InterlockLoopOut)"
        
        if (bitCluster.bit5 == 0): pass
        elif (bitCluster.bit5 == 1): "\tbit 5: ON (SupplyVoltageLow)" 
        else: print "\tbit 5: OutOfRange (SupplyVoltageLow)"
        
        if (bitCluster.bit6 == 0): pass
        elif (bitCluster.bit6 == 1): print "\tbit 6: ON (ModuleTempRange)" 
        else: print "\tbit 6: OutOfRange (ModuleTempRange)"
        
        if (bitCluster.bit8 == 0): pass
        elif (bitCluster.bit8 == 1): print "\tbit 8: ON (ShutterSensor1)" 
        else: print "\tbit 8: OutOfRange (ShutterSensor1)"
        
        if (bitCluster.bit9 == 0): pass
        elif (bitCluster.bit9 == 1): print "\tbit 9: ON (ShutterSensor2)" 
        else: print "\tbit 9: OutOfRange (ShutterSensor2)"
        
        if (bitCluster.bit12 == 0): pass
        elif (bitCluster.bit12 == 1): print "\tbit 12: ON (Filter1Moving)" 
        else: print "\tbit 12: OutOfRange (Filter1Moving)"
        
        if (bitCluster.bit13 == 0): pass
        elif (bitCluster.bit13 == 1): print "\tbit 13: ON (Filter2Moving)" 
        else: print "\tbit 13: OutOfRange (Filter2Moving)"
        
        if (bitCluster.bit14 == 0): pass
        elif (bitCluster.bit14 == 1): print "\tbit 14: ON (Filter3Moving)" 
        else: print "\tbit 14: OutOfRange (Filter3Moving)"
        
        if (bitCluster.bit15 == 0): pass
        elif (bitCluster.bit15 == 1): print "\tbit 15: ON (ErrorCodePresent)" 
        else: print "\tbit 15: OutOfRange (ErrorCodePresent)"

@raise_on_error_code
def getSuperKStatusBits(COMPort):
    """
    undocumented
    """
    bitMaskDecimal = c_int32(0)
    bitCluster = statusBitStructure()
    dll.GetSuperKStatusBits(COMPort, byref(bitMaskDecimal), bitCluster)
    return bitCluster

@raise_on_error_code
def printSuperKStatusBits(bitCluster,option="ALL"):
    """
    undocumented
    """
    print "SuperK Bit Status:"
    if (option=="ALL"):
        if (bitCluster.bit0 == 0): print "\tbit 0: OFF (Emission)" 
        elif (bitCluster.bit0 == 1): print "\tbit 0: ON (Emission)" 
        else: print "\tbit 0: OutOfRange (Emission unknown)" 
        
        if (bitCluster.bit1 == 0): print "\tbit 1: OFF (Interlock off)" 
        elif (bitCluster.bit1 == 1): print "\tbit 1: ON (Interlock ON)"
        else: print "\tbit 1: OutOfRange (Interlock unknown)"
        
        if (bitCluster.bit2 == 0): print "\tbit 2: OFF (Interlock power failure)" 
        elif (bitCluster.bit2 == 1): print "\tbit 2: ON (Interlock power failure)" 
        else: print "\tbit 2: OutOfRange (Interlock power unknown)"
        
        if (bitCluster.bit3 == 0): print "\tbit 3: OFF (Interlock loop off)" 
        elif (bitCluster.bit3 == 1): print "\tbit 3: ON (Interlock loop off)" 
        else: print "\tbit 3: OutOfRange (Interlock loop unknown)"
        
        if (bitCluster.bit5 == 0): print "\tbit 5: OFF (Supply voltage low)" 
        elif (bitCluster.bit5 == 1): print "\tbit 5: ON (Supply voltage low)" 
        else: print "\tbit 5: OutOfRange (Supply voltage unknown)"
        
        if (bitCluster.bit6 == 0): print "\tbit 6: OFF (Module temp range)" 
        elif(bitCluster.bit6 == 1): print "\tbit 6: ON (Module temp range)" 
        else: print "\tbit 6: OutOfRange (Module temp range unknown)"
        
        if (bitCluster.bit7 == 0): print "\tbit 7: OFF (Pump temp high)" 
        elif (bitCluster.bit7 == 1): print "\tbit 7: ON (Pump temp high)" 
        else: print "\tbit 7: OutOfRange (Pump temp unknown)"
        
        if (bitCluster.bit8 == 0): print "\tbit 8: OFF (Pulse overrun)" 
        elif (bitCluster.bit8 == 1): print "\tbit 8: ON (Pulse overrun)" 
        else: print "\tbit 8: OutOfRange (Pulse overrun unknown)"
        
        if (bitCluster.bit9 == 0): print "\tbit 9: OFF (Trig signal level)" 
        elif (bitCluster.bit9 == 1): print "\tbit 9: ON (Trig signal level)" 
        else: print "\tbit 9: OutOfRange (Trig signal level unknown)"
        
        if (bitCluster.bit10 == 0): print "\tbit 10: OFF (Trig edge)" 
        elif (bitCluster.bit10 == 1): print "\tbit 10: ON (Trig edge)" 
        else: print "\tbit 10: OutOfRange (Trig edge unknown)"
        
        if (bitCluster.bit15 == 0): print "\tbit 15: OFF (Error code present)" 
        elif (bitCluster.bit15 == 1): print "\tbit 15: ON (Error code present)" 
        else: print "\tbit 15: OutOfRange (Error code present unknown)"
    if (option=="ON"):
        if (bitCluster.bit0 == 0): pass
        elif (bitCluster.bit0 == 1): print "\tbit 0: ON (Emission)" 
        else: print "\tbit 0: OutOfRange (Emission)" 
        
        if (bitCluster.bit1 == 0): pass
        elif (bitCluster.bit1 == 1): print "\tbit 1: ON (Interlock off)"
        else: print "\tbit 1: OutOfRange (Interlock unknown)"
        
        if (bitCluster.bit2 == 0): pass
        elif (bitCluster.bit2 == 1): print "\tbit 2: ON (Interlock power failure)" 
        else: print "\tbit 2: OutOfRange (Interlock power unknown)"
        
        if (bitCluster.bit3 == 0): pass
        elif (bitCluster.bit3 == 1): print "\tbit 3: ON (Interlock loop off)" 
        else: print "\tbit 3: OutOfRange (Interlock loop unknown)"
        
        if (bitCluster.bit5 == 0): pass
        elif (bitCluster.bit5 == 1): print "\tbit 5: ON (Supply voltage low)" 
        else: print "\tbit 5: OutOfRange (Supply voltage unknown)"
        
        if (bitCluster.bit6 == 0): pass
        elif(bitCluster.bit6 == 1): print "\tbit 6: ON (Module temp range)" 
        else: print "\tbit 6: OutOfRange (Module temp range unknown)"
        
        if (bitCluster.bit7 == 0): pass
        elif (bitCluster.bit7 == 1): print "\tbit 7: ON (Pump temp high)" 
        else: print "\tbit 7: OutOfRange (Pump temp unknown)"
        
        if (bitCluster.bit8 == 0): pass
        elif (bitCluster.bit8 == 1): print "\tbit 8: ON (Pulse overrun)" 
        else: print "\tbit 8: OutOfRange (Pulse overrun unknown)"
        
        if (bitCluster.bit9 == 0): pass
        elif (bitCluster.bit9 == 1): print "\tbit 9: ON (Trig signal level)" 
        else: print "\tbit 9: OutOfRange (Trig signal level unknown)"
        
        if (bitCluster.bit10 == 0): pass
        elif (bitCluster.bit10 == 1): print "\tbit 10: ON (Trig edge)" 
        else: print "\tbit 10: OutOfRange (Trig edge unknown)"
        
        if (bitCluster.bit15 == 0): pass
        elif (bitCluster.bit15 == 1): print "\tbit 15: ON (Error code present)" 
        else: print "\tbit 15: OutOfRange (Error code present unknown)"

@raise_on_error_code
def getSuperKControls(COMPort):
    """
    undocumented
    """
    controlCluster = superKControlStructure()
    dll.GetSuperKControls(COMPort, controlCluster)
    return controlCluster

@raise_on_error_code
def getVariaControls(COMPort):
    """
    undocumented
    """
    NDFilterSetpointPercentx10 = c_uint16(0) #not used
    SWFilterSetpointAngstrom = c_uint16(0)
    LPFilterSetpointAngstrom = c_uint16(0)
    dll.GetVariaControls(COMPort, byref(NDFilterSetpointPercentx10), byref(SWFilterSetpointAngstrom), byref(LPFilterSetpointAngstrom))
    return SWFilterSetpointAngstrom.value, LPFilterSetpointAngstrom.value

@raise_on_error_code
def setSuperKControls(COMPort,controlCluster):
    """
    undocumented
    """
    dll.SetSuperKControls(COMPort, controlCluster)

@raise_on_error_code
def setSuperKControlEmission(COMPort,state):
    """
    undocumented
    """
    waitTime = 3 #wait time for emission to switch (can take a few seconds)
    superKBitCluster = getSuperKStatusBits(COMPort)
    variaBitCluster = getVariaStatusBits(COMPort)
    
    if (state == 0):
        dll.SetSuperKControlEmission(COMPort, c_uint8(0) )
        sleep(waitTime) #wait for emission to switch
        #logging.debug( 'Setting SuperK emission to: {}'.format(c_uint8(0).value) )
        superKBitCluster = getSuperKStatusBits(COMPort)
        #if (superKBitCluster.bit0 == 1):
            #logging.error( 'Setting SuperK emission: ERROR! Emission set to zero but EMISSION IS ON.')
        #elif (superKBitCluster.bit0 == 0):
            #logging.info( 'Setting SuperK emission: Emission set to zero. Emission is OFF.')
        #else:
            #logging.error( 'Setting SuperK emission: ERROR! Emission set to zero but EMISSION STATE IS UNKNOWN: {}'.format(superKBitCluster.bit0) )
    
    elif (state == 1):
        if (superKBitCluster.bit15 == 1) or (variaBitCluster.bit15 == 1):
            dll.SetSuperKControlEmission(COMPort, 0 )
            #logging.debug( 'Setting SuperK emission to: {}'.format(c_uint8(0).value) )
            sleep(waitTime)
            superKBitCluster = getSuperKStatusBits(COMPort)
            #if (superKBitCluster.bit0 == 1):
                #logging.error( 'Setting SuperK emission: ERROR present. Emission set to zero. Check system. WARNING EMISSION IS ON.')
            #elif (superKBitCluster.bit0 == 0):
                #logging.error( 'Setting SuperK emission: ERROR present. Emission set to zero. Emission is OFF.')
            #else:
                #logging.error( 'Setting SuperK emission: ERROR present. Emission set to zero. Check system. WARNING EMISSION IS UNKNOWN.')
            
        elif (superKBitCluster.bit15 == 0) and (variaBitCluster.bit15 == 0):
            if (variaBitCluster.bit12 == 0) and (variaBitCluster.bit13 == 0) and (variaBitCluster.bit14 == 0):
                dll.SetSuperKControlEmission(COMPort, c_uint8(state) )
                #logging.debug( 'Setting SuperK emission to: {}'.format(c_uint8(state).value) )
                sleep(waitTime)
                superKBitCluster = getSuperKStatusBits(COMPort)
                #if (superKBitCluster.bit0 == 1):
                    #logging.info( 'Setting SuperK emission: {}, Emission is ON.'.format(state) )
                #elif (superKBitCluster.bit0 == 0):
                    #logging.error( 'Setting SuperK emission: ERROR, emission set to {} but emission is OFF. Check system.'.format(superKBitCluster.bit0) )
                #else:
                    #logging.error( 'Setting SuperK emission: ERROR, state UNKNOWN: {}. Check system.'.format(superKBitCluster.bit0) )
            else:
                dll.SetSuperKControlEmission(COMPort, 0 )
                #logging.debug( 'Setting SuperK emission to: {}'.format(c_uint8(0).value) )
                sleep(waitTime)
                superKBitCluster = getSuperKStatusBits(COMPort)
                #if (superKBitCluster.bit0 == 1):
                    #logging.error( 'Setting SuperK emission: Unable to set while Varia filters moving. WARNING Emission is ON.' )
                #elif (superKBitCluster.bit0 == 0):
                    #logging.error( 'Setting SuperK emission: Unable to set while Varia filters moving. Emission set to zero.' )
                #else:
                    #logging.error( 'Setting SuperK emission: Unable to set while Varia filters moving. ERROR: Emission set to UNKNOWN state: {}'.format(superKBitCluster.bit0) )

@raise_on_error_code
def setSuperKControlInterlock(COMPort,state):
    """
    undocumented
    setting interlock to 1 unlocks laser (status bit shows 0 for interlock off)
    setting interlock to 0 unlocks laser (status bit shows 1 for interlock on)
    """
    dll.SetSuperKControlInterlock(COMPort, c_uint8(state) )
    sleep(1)
    bitCluster = getSuperKStatusBits(COMPort)

    # if (state == 1):
        # if (bitCluster.bit15 == 1):
            # if (bitCluster.bit1 == 0):
                # #logging.error( 'Setting SuperK Control Interlock to {}: ERROR present. Interlock ON. Check system.'.format(state) )
            # elif (bitCluster.bit1 == 1):
                # #logging.error( 'Setting SuperK Control Interlock to {}: ERROR present. Interlock Off. Check system.'.format(state) )
            # else:
                # #logging.error( 'Setting SuperK Control Interlock to {}: ERROR present. Interlock state UNKNOWN. Check system.'.format(state) )
        # elif (bitCluster.bit15 == 0):
            # if (bitCluster.bit1 == 0):
                # #logging.error( 'Setting SuperK Control Interlock to {}: ERROR present. Interlock ON. Check system.'.format(state) )
            # elif (bitCluster.bit1 == 1):
                # #logging.info( 'Setting SuperK Control Interlock to {}: Success. Interlock Off.'.format(state) )
            # else:
                # #logging.error( 'Setting SuperK Control Interlock to {}: ERROR present. Interlock state UNKNOWN. Check system.'.format(state) )
    # elif (state == 0):
        # if (bitCluster.bit15 == 1):
            # if (bitCluster.bit1 == 0):
                # #logging.error( 'Setting SuperK Control Interlock to {}: ERROR present. Interlock ON. Check system.'.format(state) )
            # elif (bitCluster.bit1 == 1):
                # #logging.error( 'Setting SuperK Control Interlock to {}: ERROR present. Interlock Off. Check system.'.format(state) )
            # else:
                # #logging.error( 'Setting SuperK Control Interlock to {}: ERROR present. Interlock state UNKNOWN. Check system.'.format(state) )
        # elif (bitCluster.bit15 == 0):
            # if (bitCluster.bit1 == 0):
                # #logging.info( 'Setting SuperK Control Interlock to {}: Success. Interlock ON.'.format(state) )
            # elif (bitCluster.bit1 == 1):
                # #logging.error( 'Setting SuperK Control Interlock to {}: ERROR present. Interlock Off. Check system.'.format(state) )
            # else:
                # #logging.error( 'Setting SuperK Control Interlock to {}: ERROR present. Interlock state UNKNOWN. Check system.'.format(state) )

@raise_on_error_code
def setVariaControls(COMPort, SWFilterSetpointAngstrom, LPFilterSetpointAngstrom):
    NDFilterSetpointPercentx10 = c_uint16(0)
    SWFilterSetpointAngstrom = c_uint16(SWFilterSetpointAngstrom)
    LPFilterSetpointAngstrom = c_uint16(LPFilterSetpointAngstrom)
    
    variaBitCluster = getVariaStatusBits(COMPort)
    superKBitCluster = getSuperKStatusBits(COMPort)

    if (superKBitCluster.bit0 == 0 or superKBitCluster.bit0 == 1 ): #if emmission OFF, (OR ON, this needs discussing)
        if (variaBitCluster.bit15 == 0): #if no other errors,
            if (SWFilterSetpointAngstrom.value > LPFilterSetpointAngstrom.value): #if high > low wavelength
                if ((SWFilterSetpointAngstrom.value - LPFilterSetpointAngstrom.value) >= 100 and (SWFilterSetpointAngstrom.value - LPFilterSetpointAngstrom.value) <= 1000): # check wavelength difference is >0.1nm and <100nm
                    dll.SetVariaControls(COMPort, NDFilterSetpointPercentx10, SWFilterSetpointAngstrom, LPFilterSetpointAngstrom)
                    variaBitCluster = getVariaStatusBits(COMPort)
                    
                    for x in range(60): #test to see if filters are moving, 30sec is about the time for the largest possible move
                        if (variaBitCluster.bit12 == 1 or variaBitCluster.bit13 == 1 or variaBitCluster.bit14 == 1):
                            sleep(0.5)
                            variaBitCluster = getVariaStatusBits(COMPort)
                            #print( 'Warning (setVariaControls): Filters moving. Waiting.' )
                            if (variaBitCluster.bit12 == 0 and variaBitCluster.bit13 == 0 and variaBitCluster.bit14 == 0):
                                #print ( 'Warning (setVariaControls): Ok filters stopped moving.' )
                                break
                        #if (x == 60):
                            #print( 'ERROR (setVariaControls): Filters have not stopped moving. Check system.')
                    
                    #if (variaBitCluster.bit12 == 0) and (variaBitCluster.bit13 == 0) and (variaBitCluster.bit14 == 0):
                        #print( 'Setting Varia Filters to: {} and {} : Success.'.format(LPFilterSetpointAngstrom.value,SWFilterSetpointAngstrom.value) )
                else:
                    print( 'ERROR (setVariaControls): Minimum bandwidth is 10nm. Maximum bandwidth is 100nm. SP & LP filters must differ by at least 10nm and no more than 100nm.')
            else:
                print( 'ERROR (setVariaControls): SWP filter value must be larger than LPP filter value')
        elif (variaBitCluster.bit15 == 0):
            print( 'Setting Varia Filters: ERROR present. Filters not set. Check system.')
    elif (superKBitCluster.bit0 == 1):
        print( 'Setting Varia Filters: ERROR: Emission is ON. Cannot adjust wavelength without turning off emission.')
    return 0
