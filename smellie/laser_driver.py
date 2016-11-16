from sepia.usb import close_usb_device, open_usb_device
from sepia.fwr import free_module_map, get_module_map, get_fwr_version
from sepia.slm import set_intensity_fine_step, get_intensity_fine_step,get_pulse_parameters, set_pulse_parameters, decode_freq_trig_mode
from sepia.com import get_module_type, decode_module_type
from sepia.scm import get_laser_locked, get_laser_soft_lock, set_laser_soft_lock
from smellie_config import LASER_DRIVER_SLOT_ID, LASER_DRIVER_DEV_ID, LASER_SLOT_ID
import time
from smellie.smellie_logger import SMELLIELogger

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
        SMELLIELogger.debug('SNODROP DEBUG: LaserDriver.port_open()')
        if not self.isConnected:
            open_usb_device(self.dev_id)
            time.sleep(5)
            get_module_map(self.dev_id)
            time.sleep(5)
            self.isConnected = True
            
            # Sets the laser into pulse mode, with the frequency mode = rising edge of the external trigger pulse.
            # Do not change this for Detector Safety reasons!
            set_pulse_parameters(self.dev_id, self.laser_slot_id)
            time.sleep(5)
            self.check_pulse_mode()
            self.check_trig_mode()
            time.sleep(1)
        else:
            raise LaserDriverLogicError("Laser port already open.") 

    def port_close(self):
        """
        (Cleanly!) close the USB connection to SEPIA
        """
        SMELLIELogger.debug('SNODROP DEBUG: LaserDriver.port_close()')
        free_module_map(self.dev_id)
        time.sleep(5)
        close_usb_device(self.dev_id)
        self.isConnected = False
        time.sleep(5) #give this some time, otherwise run into USB device errors on next open.

    def get_pulse_params(self):
        """
        Poll SEPIA for a summary of the current device parameters: frequency mode, pulse mode and head type

        :returns: frequency_mode
        :returns: pulse_mode 
        :returns: head_type
        :rtype: (int, bool, int) tuple
        """
        if self.isConnected:
            params = get_pulse_parameters(self.dev_id, self.laser_slot_id)
            SMELLIELogger.debug('SNODROP DEBUG: LaserDriver.get_pulse_params() = {}'.format(params))
            return params
        else:
            raise LaserDriverLogicError("Laser port not open.") 
            return 0

    def get_frequency_mode(self):
        """
        Poll SEPIA for the currently set frequency mode: 0 (80MHz), 1 (40MHz), 2 (20MHz), 3 (10MHz), 4 (5MHz), 5 (2.5MHz), 6 (external pulse, rising edge), 7 (external pulse, falling edge)

        :returns: frequency_mode
        :rtype:
        """
        if self.isConnected:
            mode = decode_freq_trig_mode(self.get_pulse_params()[0])
            SMELLIELogger.debug('SNODROP DEBUG: LaserDriver.get_frequency_mode() = {}'.format(mode))
            return mode
        else:
            raise LaserDriverLogicError("Laser port not open.") 
            return 0

    def get_pulse_mode(self):
        """
        Poll SEPIA for the currently set pulse mode: 0 (continuous), 1 (pulsed)

        :returns: pulse_mode
        :rtype: int
        """
        if self.isConnected:
            pulse_mode = bool(self.get_pulse_params()[1])
            SMELLIELogger.debug('SNODROP DEBUG: LaserDriver.get_pulse_mode() = {}'.format(pulse_mode))
            return pulse_mode
        else:
            raise LaserDriverLogicError("Laser port not open.") 
            return 0

    def get_head_type(self):
        """
        Poll SEPIA for the currently set head type

        :returns: head_type
        :rtype: int
        """
        if self.isConnected:
            head_type = self.get_pulse_params()[2]
            SMELLIELogger.debug('SNODROP DEBUG: LaserDriver.get_head_type() = {}'.format(head_type))
            return head_type
        else:
            raise LaserDriverLogicError("Laser port not open.") 
            return 0
        
    def check_pulse_mode(self):
        """
        Check which pulse mode is set in SEPIA - it must *always* be used in *pulsed* mode (1), and never in continuous mode (0)

        :raises: :class:`.LaserDriverHWError` if pulsed mode is not set
        """
        if self.isConnected:
            SMELLIELogger.debug('SNODROP DEBUG: LaserDriver.check_pulse_mode()')
            if not self.get_pulse_params()[1] == 1:
                raise LaserDriverHWError("Laser Driver is not in pulsed mode!!")
        else:
            raise LaserDriverLogicError("Laser port not open.") 

    def check_trig_mode(self):
        """
        Check which trigger mode is set in SEPIA

        :raises: :class:`.LaserDriverHWError` if pulsed mode is not set
        """
        if self.isConnected:
            SMELLIELogger.debug('SNODROP DEBUG: LaserDriver.check_trig_mode()')
            if not self.get_pulse_params()[0] == 6:
                raise LaserDriverHWError("Laser Driver is not in external trigger (rising edge) mode!")
        else:
            raise LaserDriverLogicError("Laser port not open.") 

    def get_intensity(self):
        """
        Poll SEPIA for the currently set laser head intensity: a percentage between 0 and 100, in increments of 0.1%

        :returns: intensity
        :rtype: int
        """
        if self.isConnected:
            intensity = get_intensity_fine_step(self.dev_id, self.laser_slot_id)
            SMELLIELogger.debug('SNODROP DEBUG: LaserDriver.get_intensity() = {}'.format(intensity))
            return intensity
        else:
            raise LaserDriverLogicError("Laser port not open.") 
            return 0

    def set_intensity(self, intensity):
        """
        Set the laser head intensity: a percentage between 0 and 100, in increments of 0.1%

        :param intensity: requested laser head intensity
        :type intensity: double

        :raises: :class:`.LaserDriverHWError` if the command is unsuccessful
        """
        if self.isConnected:
            SMELLIELogger.debug('SNODROP DEBUG: LaserDriver.set_intensity({})'.format(intensity))
            set_intensity_fine_step(self.dev_id, self.laser_slot_id, intensity)
            if not self.get_intensity() == intensity:
                raise LaserDriverHWError("Cannot set Laser head intensity!")
        else:
            raise LaserDriverLogicError("Laser port not open.") 

    def is_laser_locked(self):
        """
        Poll SEPIA for the lock status.
        
        :returns: True if the power is off, the soft-lock is on or the sepia key is locked
        """
        if self.isConnected:
            locked_status = get_laser_locked(self.dev_id, self.driver_slot_id)
            SMELLIELogger.debug('SNODROP DEBUG: LaserDriver.is_laser_locked() = {}'.format(locked_status))
            return locked_status
        else:
            raise LaserDriverLogicError("Laser port not open.") 
            return 0

    def is_soft_lock_on(self):
        """
        Poll SEPIA for the status of the soft-lock
        
        :returns: True if the soft lock is on
        """
        if self.isConnected:
            locked_status = get_laser_soft_lock(self.dev_id, self.driver_slot_id)
            SMELLIELogger.debug('SNODROP DEBUG: LaserDriver.is_soft_lock_on() = {}'.format(locked_status))
            return locked_status
        else:
            raise LaserDriverLogicError("Laser port not open.") 
            return 0

    def set_soft_lock(self, is_locked = True):
        """
        Set the SEPIA soft-lock to on
        """
        if self.isConnected:
            SMELLIELogger.debug('SNODROP DEBUG: LaserDriver.set_soft_lock({})'.format(is_locked))
            if is_locked != self.is_soft_lock_on(): 
                set_laser_soft_lock(self.dev_id, self.driver_slot_id, is_locked)
        else:
            raise LaserDriverLogicError("Laser port not open.") 

    def go_safe(self):
        """
        Set SEPIA into its safe state: soft-lock = on, intensity = 0%
        """
        if self.isConnected:
            SMELLIELogger.debug('SNODROP DEBUG: LaserDriver.go_safe()')
            self.set_soft_lock(is_locked = True)
            self.set_intensity(0)
            set_pulse_parameters(self.dev_id, self.laser_slot_id)
        else:
            raise LaserDriverLogicError("Laser port not open.") 

    def go_ready(self, intensity):
        """
        Set SEPIA into its ready state, given intensity, sets soft-lock = off
        """
        if self.isConnected:
            SMELLIELogger.debug('SNODROP DEBUG: LaserDriver.go_ready()')
            self.set_intensity(intensity)
            self.set_soft_lock(False)
        else:
            raise LaserDriverLogicError("Laser port not open.") 
        
    def get_firmware_version(self):
        """
        Get the current SEPIA firmware version as a string
        """
        if self.isConnected:
            fwr_ver = get_fwr_version(self.dev_id)
            SMELLIELogger.debug('SNODROP DEBUG: LaserDriver.get_firmware_version() = {}'.format(fwr_ver))
            return fwr_ver
        else:
            raise LaserDriverLogicError("Laser port not open.") 
            return 0
        
    def is_connected(self):
        """   
        Check if the connection to the device is open
        """
        return self.isConnected
        
    def is_alive(self):
        """
        Quick check alive or not.
        """
        if self.isConnected:
            checkValue = self.is_soft_lock_on() #choose to check the softlock:
            if (checkValue == True or checkValue == False): isAlive = True
            else: isAlive = False
            return isAlive
        else:
            raise LaserDriverLogicError("Laser port not open.") 
            return 0 

    def system_state(self):
        """
        Returns a formatted string with the hardware info and constant settings.
        """
        if self.isConnected:
            return "PQ laser (system):: Firmware Version : {}, Pulse Mode : {}, Pulse Parameters : ({})".format(self.get_firmware_version(),self.get_pulse_mode(), ", ".join(str(x) for x in self.get_pulse_params()), self.get_frequency_mode())
        else:
            raise LaserDriverLogicError("Laser port not open.") 
            return 0

    def current_state(self):
        """
        Returns a formatted string with the current hardware settings
        """
        if self.isConnected:
            return "PQ laser (settings):: Laser Locked : {}, Soft Lock : {}, Intensity : {}/1000, Frequency Mode : {}".format("Locked" if self.is_laser_locked() else "Unlocked", 
               "On " if self.is_soft_lock_on() else "Off", 
               self.get_intensity(), self.get_frequency_mode())
        else:
            raise LaserDriverLogicError("Laser port not open.") 
            return 0
