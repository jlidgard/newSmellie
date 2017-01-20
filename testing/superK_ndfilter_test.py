# Test the superK ND filter motor
# Tests the functions used to control the motor and takes a spectrum vs position.

import logging, time, datetime, numpy
from smellie import superk_driver, fibre_switch, power_meter
from smellie.smellie_logger import SMELLIELogger

class SuperKNDFilterTest(object):
    """
    Test controlling the superK ND filter motor
    """
    def __enter__(self):
        """
        Open the hardware required for tests.
        """
        global logging
        logging.debug("Open devices:")
        
        self.sk = superk_driver.SuperKDriver()
        self.fs = fibre_switch.FibreSwitch()
        self.pm = power_meter.PowerMeter()
        
        #open devices
        self.sk.port_open()
        self.fs.port_open()
        self.pm.port_open()

        #setup
        self.sk.set_parameters(trig_mode=0, pulse_rate=20000) #use the internal trigger (so we don't have to thread the NI trigger functions)
        self.fs.set_io_channel_numbers(5,14) #power meter fibre, superK input.
        self.fs_channel = self.fs.get_global_channel_number()
        logging.debug( "    Set Fibre switch chan: {}".format(self.fs_channel))

    def __exit__(self, type, value, traceback):
        """
        Close the hardware. Ensure the settings have been reset.
        """
        global logging, npass, nfail

        logging.debug("Close devices.")
        #close devices
        self.sk.port_close()
        self.fs.port_close()
        self.pm.port_close()

    def test1(self):
        """
        Test current state
        """
        global logging, npass, nfail
        
    def test2(self):
        """
        Test home status
        """
        global logging, npass, nfail
        
    def test3(self):
        """
        Test current state & disarm (watch status quickly flash on & off)
        """
        global logging, npass, nfail
        
        wavelengths = range(6050,6060,100)
        variaBW = 100
        
        NDPositions = range(2000,5010,10)
        
        sk.go_ready(0,(wavelengths[0]-variaBW/2),(wavelengths[0]+variaBW/2))
        
        for wavelength in wavelengths:
            powerDataMean = []
            powerRangeDataMean = []
            powerDataSD = []
            sk.go_ready(0,(wavelength-variaBW/2),(wavelength+variaBW/2))
            pm.set_wavelength(wavelength)
            print sk.NDFilter_position()
            sk.NDFilter_set_position(-1*200)
            time.sleep(60)
            print sk.NDFilter_position()
            time.sleep(1)
        
            for NDPosition in NDPositions:

                sk.NDFilter_set_position(-1*NDPosition)
                
                time.sleep(0.2)
                
                #get power measurement from power meter
                powerData = numpy.array([])
                powerRangeData = numpy.array([])
                for x in range(11):
                    power = pm.get_power()
                    powerRange = pm.get_power_range()
                    powerData = numpy.append(powerData,power)
                    powerRangeData = numpy.append(powerRangeData,powerRange)
                    time.sleep(0.1)
                
                powermean = numpy.mean(powerData)
                powersd = numpy.std(powerData)
                powerrange = numpy.amax(powerRangeData)
                
                powerDataMean.append( powermean )
                powerDataSD.append( powersd )
                powerRangeDataMean.append( powerrange )

                print "(Wavelength, NDPosition, Power, SD, Range): {}, {}, {}, {}, {}".format(wavelength, NDPosition, powermean, powersd, powerrange)

            fileOut = open(r'C:/SMELLIE/logs/testing/test_superk_ndfilter_{}nm.dat'.format(wavelength), 'a')
            fileOut.write('NDposition,MeanIntensity(W),SDIntensity(W),MeterRange(W)\n')
            for i,j,k,l in zip(NDPositions,powerDataMean,powerDataSD,powerRangeDataMean):
                fileOut.write( '{},{},{},{}\n'.format( i,j,k,l ) )
            fileOut.closed

        print sk.NDFilter_position()
        sk.NDFilter_set_position(-1*1)
        time.sleep(200)
        print sk.NDFilter_position()

#setup python logger
logging.basicConfig(filename=r'C:/SMELLIE/logs/testing/test_superk_ndfilter.log', filemode="a", level=logging.DEBUG)
console = logging.StreamHandler() #print logger to console
console.setLevel(logging.DEBUG)
logging.getLogger('').addHandler(console)
logging.debug( "Begin Testing SMELLIE SuperK ND filter. {}".format( datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') ) )
SMELLIELogger.new_logger("test") #give SMELLIE logger a name 
npass = 0
nfail = 0

superk_nd_filter_test = SuperKNDFilterTest()
with superk_nd_filter_test:
    try:
        pass #test ability to set into ready mode and restore safe mode
        #superk_nd_filter_test.test1()
        #test firing pulses (while monitoring the power meter)
        #superk_nd_filter_test.test2()
    except Exception as e:
        logging.debug( "Exception: {}".format(e))
#results
logging.debug( "Finished Testing SMELLIE SuperK ND filter. pass: {}/{}, fail:{}/{}".format(npass,npass+nfail,nfail,npass+nfail) )
