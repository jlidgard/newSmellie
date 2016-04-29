from laser_driver import LaserDriver
from laser_switch import LaserSwitch
from fibre_switch import FibreSwitch
from ni_trigger_generator import TriggerGenerator
from ni_gain_control import GainVoltageGenerator
import system_state
from time import sleep

class SmellieController(object):    
    def __enter__(self):
        """
        Open the SMELLIE Controller, with all hardware in deactivated mode
        """        
        self.fibre_switch = FibreSwitch()              
        self.laser_switch = LaserSwitch()              
        self.gain_voltage = GainVoltageGenerator()
        self.trig_signals = TriggerGenerator()
        self.laser_driver = LaserDriver()              
        self.laser_driver.open_connection()            
        self.deactivate()                              

    def __exit__(self, type, value, traceback):
        """
        Clean up code goes here - it is guaranteed to get called even if an exception is thrown during one of the other functions
        """
        self.deactivate()
        self.laser_driver.close_connection()

    def go_safe(self):        
        self.laser_driver.go_safe()
        self.gain_voltage.go_safe()
        return 0

    def deactivate(self):
        self.go_safe()
        self.laser_switch.set_active_channel(0)
        return 0

    def laserheads_master_mode(self, ls_chan, intensity, fs_input_chan, fs_output_chan, n_pulses):
        self.laser_switch.set_active_channel(ls_chan)
        self.laser_driver.set_intensity(intensity)
        self.fibre_switch.set_io_channel_numbers(fs_input_chan, fs_output_chan)
        with TriggerGenerator() as trigGen:
            trigGen.generate_triggers(n_pulses)
        self.go_safe()
        return 0

    def laserheads_slave_mode(self, ls_chan, intensity, fs_input_chan, fs_output_chan, time):
        self.laser_switch.set_active_channel(ls_chan)
        self.laser_driver.set_intensity(intensity)
        self.fibre_switch.set_io_channel_numbers(fs_input_chan, fs_output_chan)
        sleep(time)
        self.go_safe()
        return 0

    # def superK_master_mode function to be completed here

    def set_gain_control(self, voltage):
        with GainVoltageGenerator() as gainGen:
            gainGen.generate_voltage(voltage)
        return 0

    def system_state(self):
        return """ SMELLIE git SHA: {0}
CONFIGURATION:
{1}

LASER DRIVER:
{2}

LASER SWITCH:
{3}

FIBRE SWITCH:
{4}

GAIN CONTROL:
{5}
""".format(system_state.get_SHA(),
           system_state.get_config_str(),
           self.laser_driver.current_state(),
           self.laser_switch.current_state(),
           self.fibre_switch.current_state(),
           self.gain_voltage.current_state())
