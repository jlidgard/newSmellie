from config import LASER_DRIVER_DEV_ID, LASER_DRIVER_SLOT_ID
from laser_driver import LaserDriver
from laser_switch import LaserSwitch
from fiber_switch import FibreSwitch
from time import sleep
from ni_box import TriggerGenerator, GainVoltageGenerator
import system_state

class SmellieController(object):    
    def __init__(self):
        self.laser_driver = LaserDriver(LASER_DRIVER_DEV_ID, 
                                        LASER_DRIVER_SLOT_ID)
        self.fiber_switch = FibreSwitch()
        self.laser_switch = LaserSwitch()
        self.gain_voltage_gen = GainVoltageGenerator()
        self.go_safe()
        
    def go_safe(self):
        with self.laser_driver:
            self.laser_driver.go_safe()
        self.gain_voltage_gen.go_safe()

    def deactivate(self):
        self.go_safe()
        self.laser_switch.go_safe()
        
    def pulse_master_mode(self, freq, n_pulses, 
                          fs_input_chan, fs_output_chan,
                          ls_chan, intensity
                          ):
        try:
            self.laser_switch.set_channel(ls_chan)
            self.laser_driver.set_intensity(intensity)
            self.fiber_switch.set_channel(input_channel, output_channel)
            
            with TriggerGenerator() as trig:
                trig.generate(n_pulses)

        finally:
            self.go_safe()

    def begin_slave_mode(self, fs_input_chan, fs_output_chan, 
                         ls_chan, intensity, time):
        try:
            self.laser_switch.set_channel(ls_chan)
            self.laser_driver.set_intensity(intensity)
            self.fiber_switch.set_channel(fs_input_chan, fs_output_chan)
            sleep(time)

        finally:
            self.go_safe()

    def set_gain_control(self, voltage):
        with GainVoltageGenerator() as g:
            g.set_voltage(voltage)

    def system_state(self):
        with self.laser_driver:
            laser_driver_state = self.laser_driver.current_state()
        return """ SMELLIE Software SHA: {0}
CONFIGURATION:
{1}

LASER DRIVER:
{2}

LASER SWITCH:
{3}

FIBER SWITCH:
{4}

GAIN CONTROL:
{5}
""".format(system_state.get_SHA(),
           system_state.get_config_str(),
           laser_driver_state,
           self.laser_switch.current_state(),
           self.fiber_switch.current_state()
           self.gain_voltage_gen.current_state()
           )
