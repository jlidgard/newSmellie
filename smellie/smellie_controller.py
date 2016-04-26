from config import LASER_DRIVER_DEV_ID, LASER_DRIVER_SLOT_ID
from laser_driver import LaserDriver
from laser_switch import LaserSwitch
from fiber_switch import FibreSwitch
from ni_box import TriggerGenerator, GainVoltageGenerator

class SmellieController(object):
    def __init__(self):
        self.laser_driver = LaserDriver(LASER_DRIVER_DEV_ID, 
                                        LASER_DRIVER_SLOT_ID)
        self.fiber_switch = FibreSwitch()
        self.laser_switch = LaserSwitch()
        self.go_safe()
        
    def go_safe(self):
        self.laser_switch.go_safe()
        with self.laser_driver:
            self.laser_driver.go_safe()

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
                         ls_chan, intensity):
        try:
            self.laser_switch.set_channel(ls_chan)
            self.laser_driver.set_intensity(intensity)
            self.fiber_switch.set_channel(fs_input_chan, fs_output_chan)
            
        except:
            self.go_safe()
            raise

    def end_slave_mode(self):
        self.go_safe()

    def set_gain_control(self, voltage):
        with GainVoltageGenerator() as g:
            g.set_voltage(voltage)

        
        
