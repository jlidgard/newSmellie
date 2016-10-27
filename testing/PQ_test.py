# Test the SMELLIE SuperK laser
# functions to test the functionality of the SuperK control code
# Test with the spectrometer (or, alternatively the power meter)

import logging, time, datetime, numpy
from smellie import laser_driver, power_meterfibre_switch
ld = superk.SuperK()
pm = power_meter.PowerMeter()
fs = fibre_switch.FibreSwitch()
ls = laser_switch.LaserSwitch()

logging.basicConfig(filename=r'C:\SMELLIE\software\newSmellie\testing\test_PQlaser.log', filemode="a", level=logging.DEBUG)
console = logging.StreamHandler() #print logger to console
console.setLevel(logging.DEBUG)
logging.getLogger('').addHandler(console)

npass = 0
nfail = 0

try:
    logging.debug( "Begin Testing SMELLIE PQ lasers. {}".format( datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') ) )
    
    #open devices
    ld.port_open()
    fs.port_open()
    pm.port_open()
    
    logging.debug( "Current state: {}".format( ld.current_state() ) )
    
    
    #record original settings
    ls_original = ls.get_active_channel()
    fs_original = fs.get_global_channel_number()
    pm_original = pm.get_wavelength()
    
    #set test settings
    laser_number = 4 #use 550nm laser as test
    ls.set_active_channel(laser_number)
    fs.set_io_channel_numbers(laser_number, 14) #output fibre 14 = power meter
    pm.set
    
    #now run tests,
    
    powerData = numpy.array([])
    powerRangeData = numpy.array([])
    for x in range(11):
        power = pm.get_power()
        powerRange = pm.get_power_range()
        powerData = numpy.append(powerData,power)
        powerRangeData = numpy.append(powerRangeData,powerRange)
        time.sleep(0.1)


    #set back to original settings
    ls.set_active_channel(ls_original)
    fs_original.set_global_channel_number(fs_original)
    pm.set_wavelength(pm_original)
    
    logging.debug( "Restore original channel: {}, ('selected' state: {})".format(  chan_restored, ls.get_selected_channel() ) )
 

    #if True:
    logging.debug("Test PASSED")
    npass+=1
    else:
        logging.debug("Test FAILED")
        nfail+=1
    
    #close devices
    ld.port_close()
    fs.port_close()
    pm.port_close()
    
    logging.debug( "Finished Testing SMELLIE SuperK, pass: {}/{}, fail:{}/{}".format(npass,npass+nfail,nfail,npass+nfail) )
    
except Exception, e:
    logging.debug( "Exception:" )
    logging.debug( e )