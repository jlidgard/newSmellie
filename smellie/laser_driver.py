from sepia.usb import close_usb_device, open_usb_device
from sepia.fwr import free_module_map, get_module_map, get_fwr_version
from sepia.slm import set_intensity_fine_step, get_pulse_parameters, set_pulse_parameters
from sepia.com import get_module_type, decode_module_type
from config import LASER_DRIVER_DEV_ID, LASER_DRIVER_SLOT_ID

class LaserDriverLogicError(Exception):
    pass

class LaserDriverHWError(Exception):
    pass

class LaserDriver(object):
    def __init__(self):
        self.dev_id  = LASER_DRIVER_DEV_ID
        self.slot_id = LASER_DRIVER_SLOT_ID
    
    def open_connection(self):
        open_usb_device(self.dev_id)
        get_module_map(self.dev_id)
        
    def close_connection(self):
        free_module_map(self.dev_id)
        close_device(self.dev_id)

    def get_pulse_params(self):
        return get_pulse_parameters(self.dev_id, self.slot_id)

    def set_frequency_mode(self, freqency_mode):
        set_pulse_params(self.dev_id, self.slot_id, freqency_mode)

    def get_frequency_mode(self):        
        return self.get_pulse_params()[0]

    def get_pulse_mode(self):
        return self.get_pulse_params()[1]

    def get_head_type(self):
        return self.get_pulse_params()[2]
        
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

    def get_firmware_version(self):
        return get_fwr_version(self.dev_id)


    def current_state(self):
        """
        Returns a formatted string with the current harware settings
        """
        return """Soft Lock : {0}
Intensity : {1}/1000
Pulse Mode : {2}
Pulse Parameters : {3}
Frequency Mode : {4}
Firmware Version : {5}
""".format("On " if self.get_laser_soft_lock() else "Off",
           self.get_pulse_mode()
           ", ".join(srt(x) for x in self.get_pulse_params()),
           self.get_frequency_mode(),
           self.get_fwr_version()
           )
