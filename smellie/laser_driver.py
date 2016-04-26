from sepia.usb import close_usb_device, open_usb_device
from sepia.fwr import free_module_map, get_module_map
from sepia.slm import set_intensity_fine_step, get_pulse_parameters, set_pulse_parameters
from sepia.scm import set_laser_soft_lock, get_laser_soft_lock
from sepia.com import get_module_type, decode_module_type

class LaserDriverLogicError(Exception):
    pass

class LaserDriverHWError(Exception):
    pass

class LaserDriver(object):
    def __init__(self, dev_id, slot_id):
        self.dev_id   = dev_id
        self.slot_id  = slot_id
        self.mod_type = decode_module_type(get_module_type(self.dev_id, 
                                                           self.slot_id))
    def __enter__(self):
        open_usb_device(self.dev_id)
        self.mod_map = get_module_map(self.dev_id)
        self.go_safe()
        self.check_pulse_mode()
        self.set_soft_lock(is_locked = False)

    def __exit__(self):
        self.go_safe()
        free_module_map(self.dev_id)
        close_device(self.dev_id)

    def get_pulse_params(self):
        return get_pulse_parameters(self.dev_id, self.slot_id)

    def set_frequency_mode(self, freqency_mode):
        set_pulse_params(self.dev_id, self.slot_id, freqency_mode)
        
    def check_pulse_mode(self):
        if not self.get_pulse_parameters()[1] == 1:
            raise LaserDriverHWError("LaserDriver pulsemode != 1 !!")

    def get_intensity(self):
        return get_intensity_fine_step(self.dev_id, self.slot_id, intensity)

    def set_intensity(self, intensity):
        set_intensity_fine_step(self.dev_id, self.slot_id, intensity)
        if not self.get_intensity() == intensity:
            raise LaserDriverHWError("set_intensity failed!")

    def is_soft_lock_on(self):
        return get_laser_soft_lock(self.dev_id, self.slot_id)

    def set_soft_lock(self, is_locked = True):
        set_laser_soft_lock(self.dev_id, self.slot_id, is_locked)

    def go_safe(self):
        self.set_soft_lock(is_locked = True)
        self.set_frequency(6)
        self.set_intensity(0)
