# Test the SMELLIE laser switch
# functions to test the functionality of the laser switch control code
# Test while watching laser switch. (possibly with triggers and with powermeter? but ideally spectrometer)

import logging, time, datetime, random
from smellie import laser_switch
from smellie.smellie_logger import SMELLIELogger

class LaserSwitchTest(object):
    def __enter__(self):
        """
        Open the hardware required for tests. Record setting which will be changed during testing.
        """
        global logging, npass, nfail
        logging.debug("Open devices and record current settings:")
        
        self.ls = laser_switch.LaserSwitch()
        
        #open device
        self.ls.port_open()

        #record original settings
        self.ls_original = self.ls.get_active_channel()
        
    def __exit__(self, type, value, traceback):
        """
        Close the hardware. Ensure the settings have been reset.
        """
        global logging, npass, nfail
        logging.debug("Close devices and restore original settings (restored/original):")
        
        #restore original settings        
        self.ls_restored = self.ls.get_active_channel()
        if (self.ls_restored!=self.ls_original):
            self.ls.set_active_channel(self.ls_original)
            self.ls_restored = self.ls.get_active_channel()

        #results
        logging.debug( "    Laser switch channel: {}/{}".format(self.ls_restored,self.ls_original))
        if (self.ls_original==self.ls_restored):
            logging.debug("Restore Settings PASSED")
            npass+=1
        else:
            logging.debug("Restore Settings FAILED")
            nfail+=1

        #close devices
        self.ls.port_close()

    def test1(self):
        """
        Test current state.
        """
        global logging, npass, nfail
        logging.debug("Run test 1.")
        
        #print current state. (in turn tests many of the getter functions).
        logging.debug( "    Current state: {}".format( self.ls.current_state() ) )
        
    def test2(self):
        """
        Test setting the laser switch.
        """
        global logging, npass, nfail
        logging.debug("Run test 2.")
        
        #test setting channel (to random channel)
        chan_random = random.randint(1,5)
        while chan_random==self.ls_original:
            chan_random = random.randint(1,5)

        self.ls.set_active_channel(chan_random)
        chan_new = self.ls.get_active_channel()
        logging.debug( "Test setting random channel: set={}, get={}".format(chan_random, chan_new))

        #result
        if (chan_random==chan_new): 
            logging.debug("Test PASSED")
            npass+=1
        else: 
            logging.debug("Test FAILED")
            nfail+=1
        
#setup python logger
logging.basicConfig(filename=r'C:/SMELLIE/logs/testing/test_laser_switch.log', filemode="a", level=logging.DEBUG)
console = logging.StreamHandler() #print logger to console
console.setLevel(logging.DEBUG)
logging.getLogger('').addHandler(console)
logging.debug( "Begin Testing SMELLIE laser switch. {}".format( datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') ) )
SMELLIELogger.new_logger("test") #give SMELLIE logger a name 
npass = 0
nfail = 0

ls_test = LaserSwitchTest()
with ls_test:
    try:
        #test current state
        ls_test.test1()
        #test switching
        ls_test.test2()
    except Exception as e:
        logging.debug( "Exception: {}".format(e))
#results
logging.debug( "Finished Testing SMELLIE laser switch. pass: {}/{}, fail:{}/{}".format(npass,npass+nfail,nfail,npass+nfail) )
