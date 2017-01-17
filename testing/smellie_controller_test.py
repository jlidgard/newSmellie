# Test the SMELLIE controller
# loads the controller (opens all HW)
# test by printing current state

import logging, time, datetime
from smellie.smellie_controller import SmellieController
#from smellie.smellie_logger import SMELLIELogger

#setup a python logger (for this test, not SMELLIE logger)
logging.basicConfig(filename=r'C:/SMELLIE/logs/testing/test_smellie_controller.log', filemode="a", level=logging.DEBUG)
console = logging.StreamHandler() #print logger to console
console.setLevel(logging.DEBUG)
logging.getLogger('').addHandler(console)
logging.debug( "Begin Testing SMELLIE controller. {}".format( datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') ) )
#SMELLIELogger.new_logger("test") #give SMELLIE logger a name 


with SmellieController() as controller:

    #begin a new run. A SMELLIE log file should be created.
    runNumber = 123456
    controller.new_run(runNumber)
    
    #Test the current state. Queries all devices.
    currentState = controller.current_state()
    logging.debug('Current state: \n{}'.format(currentState))
    
    #Test firing SuperK laser (monitor power meter).
    controller.superk_master_mode(intensity=1, rep_rate=20000, low_wavelength=6000, high_wavelength=6100, fs_input_chan=5, fs_output_chan=14, n_pulses=2000, gain_voltage=0.25)
    #Test the current state after firing laser.
    currentState = controller.current_state()
    logging.debug('Current state: \n{}'.format(currentState))
    
    controller.laserheads_master_mode(ls_chan=4, intensity=1000, rep_rate=20000, fs_input_chan=4, fs_output_chan=14, n_pulses=2000, gain_voltage=0.25)
    #Test the current state after firing laser.
    currentState = controller.current_state()
    logging.debug('Current state: \n{}'.format(currentState))
    
    controller.laserheads_slave_mode(ls_chan=4, intensity=1000, fs_input_chan=4, fs_output_chan=14, time=10, gain_voltage=0.25)
    #Test the current state after firing laser.
    currentState = controller.current_state()
    logging.debug('Current state: \n{}'.format(currentState))
    
logging.debug( "Finished Testing SMELLIE controller. {}".format(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') ) )
