from laser_driver import LaserDriver
from laser_switch import LaserSwitch
from fibre_switch import FibreSwitch
from superk_driver import SuperkDriver
from power_meter import PowerMeter
from ni_trigger_generator import TriggerGenerator
from ni_gain_control import GainVoltageGenerator
from spectrometer import Spectrometer
import system_state
import smellie_config
from time import sleep

class SmellieController(object):
    def __init__(self):
        """
        Open the SMELLIE Controller, with all hardware in deactivated mode
        """
        self.fibre_switch = FibreSwitch()
        self.laser_switch = LaserSwitch()
        self.gain_voltage = GainVoltageGenerator()
        self.trig_signals = TriggerGenerator()
        self.laser_driver = LaserDriver()
        self.spectrometer = Spectrometer()
        self.superk_driver = SuperkDriver()
        #self.power_meter = PowerMeter()
        self.laser_driver.port_open()
        self.superk_driver.port_open()
        self.fibre_switch.port_open()
        #self.power_meter.port_open()
        
        self.deactivate()

    def __exit__(self, type, value, traceback):
        """
        Clean up code goes here - it is guaranteed to get called even if an exception is thrown during one of the other functions
        """
        self.deactivate()
        self.superk_driver.varia_go_safe()
        self.laser_driver.port_close()
        self.superk_driver.port_close()
        self.fibre_switch.port_close()
        #self.power_meter.port_close()

    def go_safe(self):
        """
        Send the entire SMELLIE system into `safe mode` - SEPIA soft-lock = on, SEPIA intensity = 0%
        """
        self.laser_driver.go_safe()
        self.superk_driver.go_safe()
        return 0

    def deactivate(self):
        """
        Send the entire SMELLIE system into `deactivated mode` - SEPIA soft-lock = on, SEPIA intensity = 0%, NI gain voltage = 0V, active Laser Switch channel = 0 (no laser head attached to this channel), Fibre Switch input channel = 5 and output channel = 14 (no detector fibre attached to this output channel, just power meter)
        """
        self.go_safe()
        self.gain_voltage.go_safe()
        
        #switch laser switch only if not already set
        if (self.laser_switch.get_active_channel() != 0): 
            self.laser_driver.port_close() #close before LaserSwitch d/c
            self.laser_switch.set_active_channel(0)
            self.laser_driver.port_open()
            
        self.fibre_switch.set_io_channel_numbers(5, 14)
        return 0

    def laserheads_master_mode(self, ls_chan, intensity, rep_rate, fs_input_chan, fs_output_chan, n_pulses):
        """
        Run the SMELLIE system in Master Mode (NI Unit provides the trigger signal for both the lasers and the detector) using the PicoQuant Laser Heads
        
        :param ls_chan: the laser switch channel
        
        :param intensity: the laser intensity in per mil
        
        :param fs_input_channel: the fibre switch input channel

        :param fs_output_channel: the fibre switch output channel

        :param n_pulses: the number of pulses
        """
        
        #go into safe mode
        self.laser_driver.go_safe()
        
        #switch laser switch only if not already set
        if (self.laser_switch.get_active_channel() != channel): 
            self.laser_driver.port_close() #close before LaserSwitch d/c
            self.laser_switch.set_active_channel(ls_chan)
            self.laser_driver.port_open()

        self.fibre_switch.set_io_channel_numbers(fs_input_chan, fs_output_chan)

        #Pulse in master mode
        self.laser_driver.go_ready(intensity)
        self.trig_signals.generate_triggers(n_pulses, rep_rate, 'PQ')

        #go back to safe mode
        self.laser_driver.go_safe()
        return 0

    def laserheads_slave_mode(self, ls_chan, intensity, fs_input_chan, fs_output_chan, time):
        """
        Run the SMELLIE system in Slave Mode (SNO+ MTC/D provides the trigger signal for both the lasers and the detector) using the PicoQuant Laser Heads

        :param ls_chan: the laser switch channel
        
        :param intensity: the laser intensity in per mil
        
        :param fs_input_channel: the fibre switch input channel

        :param fs_output_channel: the fibre switch output channel

        :param n_pulses: the number of pulses
        
        :param time: time until SNODROP exits slave mode
        """
        
        #go into safe mode
        self.laser_driver.go_safe()
        
        #switch laser switch only if not already set
        if (self.laser_switch.get_active_channel() != channel): 
            self.laser_driver.port_close() #close before LaserSwitch d/c
            self.laser_switch.set_active_channel(ls_chan)
            self.laser_driver.port_open()

        self.fibre_switch.set_io_channel_numbers(fs_input_chan, fs_output_chan)

        #Wait in slave mode
        self.laser_driver.go_ready(intensity)
        sleep(time)
        
        #go back to safe mode
        self.laser_driver.go_safe()
        return 0

    def superk_master_mode(self, intensity, rep_rate, low_wavelength, high_wavelength, fs_input_chan, fs_output_chan, n_pulses):
        """
        Run the SMELLIE system in Master Mode (NI Unit provides the trigger signal for both the lasers and the detector) using the SuperK laser
        
        :param intensity: the laser intensity in per mil
        
        :param fs_input_channel: the fibre switch input channel

        :param fs_output_channel: the fibre switch output channel

        :param n_pulses: the number of pulses
        """
        
        #go into safe mode
        self.superk_driver.go_safe()
        
        #switch laser_switch only if not already set
        if (self.laser_switch.get_active_channel() != channel): 
            self.laser_driver.port_close() #close before LaserSwitch d/c
            self.laser_switch.set_active_channel(0)
            self.laser_driver.port_open()

        self.fibre_switch.set_io_channel_numbers(fs_input_chan, fs_output_chan)
        
        #Pulse in master mode
        self.superk_driver.go_ready(intensity, low_wavelength, high_wavelength)
        self.trig_signals.generate_triggers(n_pulses, rep_rate, 'SUPERK')

        #go back to safe mode
        self.superk_driver.go_safe()
        return 0
        
    def set_gain_control(self, voltage):
        """
        Set the Gain Voltage of the MPU's PMT ... applicable to both Master and Slave modes and both the Laser Heads and the SuperK laser
        
        :param voltage: PMU gain voltage set value
        """
        self.gain_voltage.generate_voltage(voltage)
        return 0

    def log_info(self):
        # pipe info return into logger
        pass

    def set_dummy_mode_on(self, dummy_mode_on = True):
        '''
        Put SNODROP into dummy mode, where all server function calls just result print the call signature
        
        :param dummy_mode_on: True for dummy mode/False for normal functioning
        '''
        smellie_config.DUMMY_MODE = dummy_mode_on
        return 0

    def info(self):
        pass

    def system_state(self):
        '''
        Return a formatted string with the current system settings
        '''
        return "SMELLIE git SHA: {0} git repository dirty : {1} CONFIGURATION: {2} LASER DRIVER: {3} LASER SWITCH: {4} FIBRE SWITCH: {5} GAIN CONTROL: {6}".format(system_state.get_SHA(),
           True if system_state.git_is_dirty() else False,
           system_state.get_config_str(),
           self.laser_driver.current_state(),
           self.laser_switch.current_state(),
           self.fibre_switch.current_state(),
           self.gain_voltage.current_state()
           )


