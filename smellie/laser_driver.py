from sepia.usb import close_usb_device, open_usb_device
from sepia.fwr import free_module_map, get_module_map, get_fwr_version
from sepia.slm import set_intensity_fine_step, get_intensity_fine_step,get_pulse_parameters, set_pulse_parameters, decode_freq_trig_mode
from sepia.com import get_module_type, decode_module_type
from sepia.scm import get_laser_locked, get_laser_soft_lock, set_laser_soft_lock
from smellie_config import LASER_DRIVER_SLOT_ID, LASER_DRIVER_DEV_ID, LASER_SLOT_ID
import ctypes
"""
Control of the SEPIA II Laser Driver hardware
"""

class LaserDriverLogicError(Exception):
    """
    Thrown if an inconsistency is noticed *before* any instructions are sent to the hardware (i.e. a problem with code logic)
    """
    pass

class LaserDriverHWError(Exception):
    """
    Thrown if an inconsistency is noticed *after* any hardware instruction is executed (i.e. a problem with the hardware itself)
    """
    pass

class LaserDriver(object):
    """
    Controls the Laser Driver via commands sent down a USB port.
    """
    def __init__(self):
        self.dev_id  = LASER_DRIVER_DEV_ID
        self.driver_slot_id = LASER_DRIVER_SLOT_ID
        self.laser_slot_id = LASER_SLOT_ID
        self.isConnected = False

    def port_open(self):
        """
        Open the USB connection to SEPIA
        """
        open_usb_device(self.dev_id)
        get_module_map(self.dev_id)
        # Sets the laser into pulse mode, with the frequency mode = rising edge of the external trigger pulse.
        # Do not change this for Detector Safety reasons!
        set_pulse_parameters(self.dev_id, self.laser_slot_id)
        
        self.check_pulse_mode()
        self.check_trig_mode()
        self.isConnected = True

    def port_close(self):
        """
        (Cleanly!) close the USB connection to SEPIA
        """
        free_module_map(self.dev_id)
        close_usb_device(self.dev_id)
        self.isConnected = False

    def get_pulse_params(self):
        """
        Poll SEPIA for a summary of the current device parameters: frequency mode, pulse mode and head type

        :returns: frequency_mode
        :returns: pulse_mode 
        :returns: head_type
        :rtype: (int, bool, int) tuple
        """
        return get_pulse_parameters(self.dev_id, self.laser_slot_id)

    def get_frequency_mode(self):
        """
        Poll SEPIA for the currently set frequency mode: 0 (80MHz), 1 (40MHz), 2 (20MHz), 3 (10MHz), 4 (5MHz), 5 (2.5MHz), 6 (external pulse, rising edge), 7 (external pulse, falling edge)

        :returns: frequency_mode
        :rtype:
        """
        return decode_freq_trig_mode(self.get_pulse_params()[0])

    def get_pulse_mode(self):
        """
        Poll SEPIA for the currently set pulse mode: 0 (continuous), 1 (pulsed)

        :returns: pulse_mode
        :rtype: int
        """
        return bool(self.get_pulse_params()[1])

    def get_head_type(self):
        """
        Poll SEPIA for the currently set head type

        :returns: head_type
        :rtype: int
        """
        return self.get_pulse_params()[2]
        
    def check_pulse_mode(self):
        """
        Check which pulse mode is set in SEPIA - it must *always* be used in *pulsed* mode (1), and never in continuous mode (0)

        :raises: :class:`.LaserDriverHWError` if pulsed mode is not set
        """
        if not self.get_pulse_params()[1] == 1:
            raise LaserDriverHWError("Laser Driver is not in pulsed mode!!")

    def check_trig_mode(self):
        if not self.get_pulse_params()[0] == 6:
            raise LaserDriverHWError("Laser Driver is not in external trigger  (rising edge) mode!")

    def get_intensity(self):
        """
        Poll SEPIA for the currently set laser head intensity: a percentage between 0 and 100, in increments of 0.1%

        :returns: intensity
        :rtype: int
        """
        return get_intensity_fine_step(self.dev_id, self.laser_slot_id)

    def set_intensity(self, intensity):
        """
        Set the laser head intensity: a percentage between 0 and 100, in increments of 0.1%

        :param intensity: requested laser head intensity
        :type intensity: double

        :raises: :class:`.LaserDriverHWError` if the command is unsuccessful
        """
        set_intensity_fine_step(self.dev_id, self.laser_slot_id, intensity)
        if not self.get_intensity() == intensity:
            raise LaserDriverHWError("Cannot set Laser head intensity!")

    def is_laser_locked(self):
        """
        Poll SEPIA for the lock status.
        
        :returns: True if the power is off, the soft-lock is on or the sepia key is locked
        """
        
        return get_laser_locked(self.dev_id, self.driver_slot_id)

    def is_soft_lock_on(self):
        """
        Poll SEPIA for the status of the soft-lock
        
        :returns: True if the soft lock is on
        """
        return get_laser_soft_lock(self.dev_id, self.driver_slot_id)

    def set_soft_lock(self, is_locked = True):
        """
        Set the SEPIA soft-lock to on
        """
        if is_locked != self.is_soft_lock_on(): 
            set_laser_soft_lock(self.dev_id, self.driver_slot_id, is_locked)

    def go_safe(self):
        """
        Set SEPIA into its safe state: soft-lock = on, intensity = 0%
        """
        self.set_soft_lock(is_locked = True)
        self.set_intensity(0)
        set_pulse_parameters(self.dev_id, self.laser_slot_id)

    def get_firmware_version(self):
        """
        Get the current SEPIA firmware version as a string
        """
        return get_fwr_version(self.dev_id)
        
    def is_connected(self):
        """   
        Check if the connection to the device is open
        """
        return self.isConnected
        
    def is_alive(self):
        """
        Quick check alive or not.
        """
        isAlive = None
        if self.isConnected:
            checkValue = self.get_firmware_version() #choose to check the firmware version:
        else: 
            self.port_open()
            checkValue = self.get_firmware_version()
            self.port_close()
        if (checkValue == '1.05.419'): isAlive = True #current firmware version 1.05.419
        else: isAlive = False
        return isAlive

    def current_state(self):
        """
        Returns a formatted string with the current hardware settings
        """
        return "Laser Locked : {0}, Soft Lock : {1}, Intensity : {2}/1000, Pulse Mode : {3}, Pulse Parameters : ({4}), Frequency Mode : {5}, Firmware Version : {6}".format("Unlocked" if (self.is_laser_locked()==1) else "Locked", 
           "On " if self.is_soft_lock_on() else "Off", 
           self.get_intensity(), 
           self.get_pulse_mode(), 
           ", ".join(str(x) for x in self.get_pulse_params()),
           self.get_frequency_mode(), 
           self.get_firmware_version())
