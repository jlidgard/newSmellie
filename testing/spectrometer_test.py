# Test the SMELLIE Spectrometer
# functions to test the functionality of the Spectrometer control code
# Test while pulsing a laser

import logging, time, datetime
from smellie import spectrometer
from smellie.smellie_logger import SMELLIELogger

class SpectrometerTest(object):
    def __enter__(self):
        """
        Open the hardware required for tests. Record setting which will be changed during testing.
        """
        global logging, npass, nfail
        logging.debug("Open devices and record current settings:")
        
        self.spec = spectrometer.Spectrometer()
        
        #open devices
        self.spec.port_open()
        
    def __exit__(self, type, value, traceback):
        """
        Close the hardware. Ensure the settings have been reset.
        """
        global logging, npass, nfail
        logging.debug("Close devices :")

        #close devices
        self.spec.port_close()

    def test1(self):
        """
        Test the current state
        """
        global logging, npass, nfail
        logging.debug("Run test 1.")
        
        #print current state. (in turn tests many of the getter functions).
        logging.debug( "    System state: {}".format( self.spec.system_state() ) )
        
    def test2(self):
        """
        Test taking a spectrum
        """
        global logging, npass, nfail
        logging.debug("Run test 2.")
        #take data
        spectrumData = self.spec.get_spectrum()
        wavelengthData = self.spec.get_wavelengths()
        maxWave, maxSpec = self.spec.get_spectrum_maximum(wavelengthData,spectrumData)
        print "Max intensity: {} at {}nm".format(maxSpec, maxWave)
        self.spec.write_spectrum(r'C:/SMELLIE/logs/testing/test_spectrometer_spectrum.dat',wavelengthData,spectrumData)

#setup python logger      
logging.basicConfig(filename=r'C:/SMELLIE/logs/testing/test_spectrometer.log', filemode="a", level=logging.DEBUG)
console = logging.StreamHandler() #print logger to console
console.setLevel(logging.DEBUG)
logging.getLogger('').addHandler(console)
logging.debug( "Begin Testing SMELLIE Spectrometer. {}".format( datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') ) )
SMELLIELogger.new_logger("test") #give SMELLIE logger a name 
npass = 0
nfail = 0

spectrometer_test = SpectrometerTest()
with spectrometer_test:
    try:
        #test current state
        spectrometer_test.test1()
        #test taking data
        spectrometer_test.test2()
    except Exception as e:
        logging.debug( "Exception: {}".format(e))
        
#results
logging.debug( "Finished Testing SMELLIE Spectrometer. pass: {}/{}, fail:{}/{}".format(npass,npass+nfail,nfail,npass+nfail) )

