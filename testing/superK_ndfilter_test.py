# Test the SMELLIE SuperK laser
# functions to test the functionality of the SuperK control code
# Test with the spectrometer (or, alternatively the power meter)

import logging, time, datetime, numpy
from smellie import superk_driver, fibre_switch, power_meter
#import matplotlib.pyplot as plt

pm = power_meter.PowerMeter()
fs = fibre_switch.FibreSwitch()
sk = superk_driver.SuperKDriver()

logging.basicConfig(filename=r'C:/SMELLIE/logs/testing/test_superk_ndfilter.log', filemode="a", level=logging.DEBUG)
console = logging.StreamHandler() #print logger to console
console.setLevel(logging.DEBUG)
logging.getLogger('').addHandler(console)

npass = 0
nfail = 0

try:
    logging.debug( "Begin Testing SMELLIE ND filter. {}".format( datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') ) )   
    
    pm.port_open()
    sk.port_open()
    sk.set_parameters(trig_mode=0, pulse_rate=20000)
    fs.port_open()
    fs.set_global_channel_number(70)

    wavelengths = range(605,606,10)
    variaBW = 10
    
    NDPositions = range(200,501,1)
    
    sk.go_ready(0,(wavelengths[0]-variaBW/2)*10,(wavelengths[0]+variaBW/2)*10)
    
    for setWavelength in wavelengths:
        powerDataMean = []
        powerRangeDataMean = []
        powerDataSD = []
        sk.go_ready(0,(setWavelength-variaBW/2)*10,(setWavelength+variaBW/2)*10)
        pm.set_wavelength(setWavelength)
        print sk.NDFilter_position()
        sk.NDFilter_set_position(-1*200)
        time.sleep(60)
        print sk.NDFilter_position()
        time.sleep(1)
    
        for currentNDPosition in NDPositions:

            sk.NDFilter_set_position(-1*currentNDPosition)
            
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

            print "(Wavelength, NDPosition, Power, SD, Range): {}, {}, {}, {}, {}".format(setWavelength, currentNDPosition, powermean, powersd, powerrange)

        fileOut = open(r'C:/SMELLIE/workDiary/test_superk_ndfilter_{}nm.dat'.format(setWavelength), 'a')
        fileOut.write('NDposition,MeanIntensity(W),SDIntensity(W),MeterRange(W)\n')
        for i,j,k,l in zip(NDPositions,powerDataMean,powerDataSD,powerRangeDataMean):
            fileOut.write( '{},{},{},{}\n'.format( i,j,k,l ) )
        fileOut.closed
    
    print sk.NDFilter_position()
    sk.NDFilter_set_position(-1*1)
    time.sleep(200)
    print sk.NDFilter_position()
    
    sk.go_safe()
    sk.port_close()
    pm.port_close()
    
    logging.debug( "Finished Testing SMELLIE SuperK ND filter" )
    
    #plt.errorbar(NDPositions,powerDataMean, yerr=powerDataSD,fmt='o')
    #plt.axis([000,450,1E-10,1E-6])
    #plt.show()
    
except Exception, e:
    logging.debug( "Exception: {}".format(e) )