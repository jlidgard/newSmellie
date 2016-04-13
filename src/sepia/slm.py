from _sepia import string_buffer, dll, raise_on_error_code, SepiaLogicError
import ctypes

"""
Laser Driver Functions (SLM)
From the original C-API: SLM 828 modules can interface the huge families of pulsed laser diode heads (LDH series) and pulsed LED heads (PLS series) from PicoQuant. These functions let the application control their working modes and intensity.
"""

@raise_on_error_code
def get_pulse_parameters(dev_id, slot_id):
    """get_pulse_parameters(dev_id, slot_id, iFreq)
    Get the pulse paramters for the SLM module

    :param dev_id: the sepia device number (ordered from 0)
    :type dev_id:  int

    :param slot_id: slot number, integer 000-989
    :type slot_id:  int
    
    :returns freq: the frequency mode of the module
    :type freq: int
    
    :returns pulse_mode: In pulse mode? Otherwise continous (disabled)
    :type pulse_mode: bool
    
    :returns head_type: 
    :type head_type: int
    """
    freq = ctypes.c_int32()
    pulse_mode = ctypes.c_ubyte()
    head_type = ctypes.c_int32()
    dll.SEPIA2_SLM_GetPulseParameters(dev_id, slot_id, freq, 
                                       pulse_mode, head_type)

    return freq, pulse_mode, head_type

@raise_on_error_code
def set_pulse_parameters(dev_id, slot_id, freq_mode):
    """set_pulse_parameters(dev_id, slot_id, freq_mode)
    Set the pulse paramters for the SLM module
    the original C-API has a parameter 
    bPulseMode = (1 for pulsing, 0 for continous light).
    mode zero can cause damage to the laser heads and so bPulseMode 
    is hard coded to 1 here.    

    :param dev_id: the sepia device number (ordered from 0)
    :type dev_id:  int

    :param slot_id: slot number, integer 000-989
    :type slot_id:  int
    
    :param freq_mode: index into list of frequencies/trigger modi 0 - 7
    :type freq_mode: int

    :returns: None
    """
    if not freq_mode in xrange(8):
        raise SepiaLogicError("decode_freq_trig_mode: trigger mode must be 0-7")

    # last parameter is the pulse mode! DO NOT CHANGE (see above)
    dll.SetPulseParamters(dev_id, slot_id, freq_mode, c_ubyte(1))

@raise_on_error_code
def decode_freq_trig_mode(freq_mode):
    """decode_freq_trig_mode(freq_mode)
    Translate the frequency response trigger mode to a string for any SLM
    module
    
    :param freq_mode: must be 0-7
    :type freq_mode: int
    
    :returns mode_sring:
    :type mode_string: string
    """
    
    if not freq_mode in xrange(8):
        raise SepiaLogicError("decode_freq_trig_mode: trigger mode must be 0-7")
    
    buff = string_buffer()
    dll.SEPIA2_SLM_DecodeFreqTrigMode(freq_mode, buff)
    return buff

@raise_on_error_code
def get_intensity_fine_step(dev_id, slot_id):
    """get_intensity_fine_step(dev_if, slot_id)
    Get the current intensity value of a fiven SLM driver module in 
    per mille of the laser head controlling voltage

    :param dev_id: the sepia device number (ordered from 0)
    :type dev_id:  int

    :param slot_id: slot number, integer 000-989
    :type slot_id:  int
    
    :returns intensity: 
    :type intensity: int
    """
    intensity = ctypes.c_ushort()
    dll.SEPIA2_SLM_GetIntensityFineStep(dev_id, slot_id, intensity)
    return intensity
    
    
@raise_on_error_code
def set_intensity_fine_step(dev_id, slot_id, intensity):
    """set_intensity_fine_step(dev_id, slot_id, intensity)
    Set the intensity value of a given SLM driver module, in per mille
    of laser head controlling voltage

    :param dev_id: the sepia device number (ordered from 0)
    :type dev_id:  int

    :param slot_id: slot number, integer 000-989
    :type slot_id:  int
    
    :param intensity: 
    :type intensity: int

    :returns: None
    """
    if not intensity in xrange(int(1e3)):
        raise SepiaLogicError("set_intensity_fine_step: fine step is in per mille - must be 0 - 1000")
    dll.SEPIA2_SLM_SetIntensityFineStep(dev_id, slot_id, intensity)


@raise_on_error_code
def decode_head_type(head_type_code):
    """decode_head_type(head_type)
    Returns the head type string at list position head_type for any SLM 
    module
    
    :param head_type_code: must be 0-3
    :type head_type_code: int

    :returns head_type:
    :type head_type: string    
    """
    if not head_type_code in xrange(4):
        raise SepiaLogicError("decode_head_type:: head_type must be 0-3")

    type = string_buffer()
    dll.SEPIA2_SLM_DecodeHeadType(head_type_code, type)
    return type
