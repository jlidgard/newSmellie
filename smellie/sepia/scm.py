from sepia import dll, raise_on_error_code
"""
Device Operational Safety Controller Functions (SCM)
From the original C-API:

This module implements the safety features of the PQ Laser Device, as there are the thermal and voltage monitoring, the interlock (hard locking) and soft locking capabilities.
"""

@raise_on_error_code
def get_laser_soft_lock(dev_id, slot_id):
    """get_laser_soft_lock(dev_id, slot_id)
    Returns the contents of the soft lock register. Remember: a hard lock 
    overrides a soft lock, so this isnt nessecarily the state of the laser

    :param dev_id: the sepia device number (ordered from 0)
    
    :param slot_id: slot number, integer 000-989
    
    :returns: is_locked as bool
    """
    contents = ctypes.c_ubyte()
    _dll.SEPIA2_SCM_GetLaserSoftLock(dev_id, slot_id, contents)
    return bool(contents)

@raise_on_error_code
def set_laser_soft_lock(dev_id, slot_id, contents):
    """set_laser_soft_lock(dev_id, slot_id, contents)
    Sets the contents of the soft lock register. Remember: a hard lock 
    overrides a soft lock, so this isnt nessecarily the state of the laser
    
    :param dev_id: the sepia device number (ordered from 0)
    :type dev_id: int

    :param slot_id: slot number, integer 000-989
    :type dev_id: int

    :param is_locked: new soft lock register 1
    :type contents: bool

    :returns: None
    """
    _dll.SEPIA2_SCM_SetLaserSoftLock(dev_id, slot_id, 
                                     ctypes.c_ubyte(contents))
    

@raise_on_error_code
def get_laser_locked(dev_id, slot_id):
    """get_laser_locked(dev_id, slot_id)
    Get the state of the laser power line, will return 0 if the power is off,
    there has been a softlock, or a hardlock with the key. 

    :param dev_id: the sepia device number (ordered from 0)
    :type dev_id: int

    :param slot_id: slot number, integer 000-989
    :type dev_id: int

    :returns: power_state - is power line active? 
    :type power_state: bool    
    """
    state = ctypes.c_ubyte()
    _dll.SEPIA2_SCM_GetLaserLocked(dev_id, slot_id, state)
    return bool(state)
