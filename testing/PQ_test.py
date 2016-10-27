# Test the SMELLIE PicoQuant (PQ) lasers
# Runs an intensity scan of each laser and saves to file (so also uses laser switch, fibre switch, powermeter).

import logging, time, datetime, numpy
from smellie import laser_driver, power_meter, fibre_switch, laser_switch
ld = laser_driver.LaserDriver()
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
    

    
    
    #record original settings
    ls_original = ls.get_active_channel()
    fs_original = fs.get_global_channel_number()
    pm_original = pm.get_wavelength()
    logging.debug( "Current settings: Laser switch chan: {}, Fibre switch: {}, Power meter wavelength: {}".format( ls_original, fs_original, pm_original ) )
    
    #------------------- testing -----------------
    #get current state
    logging.debug( "Current state: {}".format( ld.current_state() ) )
    
    laser_numbers = range(1,5,1) #test lasers 1 thru 4
    intensities = range(0,101,1) #from 0 to 100% intensity
    wavelengths = (375, 407, 446, 495)
    
    #for laser_number, wavelength in zip(laser_numbers,wavelengths):
    
    laser_number = 4
    wavelength = 495
    ls.set_active_channel(laser_number)
    fs.set_io_channel_numbers(laser_number, 14) #output fibre 14 = power meter
    pm.set_wavelength(wavelength)

    powerMean = []
    powerSD = []
    powerRange = []
    
    logging.debug( "Begin intensity scan of laser: {} ({}nm)".format(  laser_number, wavelength ) )

    for intensity in intensities:
    
        #take an average power measurement, n entries.
        entries = 10
        power_entries = numpy.array([])
        power_ranges = numpy.array([])
        for x in range(entries+1):
            power_entries = numpy.append(power_entries, pm.get_power() )
            power_ranges = numpy.append(power_ranges, pm.get_power_range() )
            time.sleep(0.01)
            
        power_mean = numpy.mean(power_entries)
        power_sd = numpy.std(power_entries)
        power_range = numpy.amax(power_ranges)
        
        powerMean.append( power_mean )
        powerSD.append( power_sd )
        powerRange.append( power_range )

        print "(laser, wavelength, intensity(%), power_mean(W), power_sd(W), power_range(W)): {}, {}, {}, {}, {}".format(laser_number, wavelength, intensity, power_mean, power_sd, power_range)
        
    fileOut = open(r'C:\SMELLIE\software\newSmellie\testing\test_PQlaser_{}nm.dat'.format(wavelength), 'a')
    fileOut.write('Laser, Wavelength(nm):'.format( laser_number, wavelength ))
    fileOut.write('Intensity(%), Power_mean(W), Power_sd(W), Power_range(W)\n')
    for i,j,k,l in zip(intensities,powerMean,powerSD,powerRange):
        fileOut.write( '{},{},{},{}\n'.format( i,j,k,l ) )
    fileOut.closed

    logging.debug( "Finish intensity scan of laser: {} ({}nm)".format(  laser_number, wavelength ) )
 
    #-------------------end of testing -----------------
    #set back to original settings
    ls.set_active_channel(ls_original)
    fs_original.set_global_channel_number(fs_original)
    pm.set_wavelength(pm_original)
    
    logging.debug( "Current settings: Laser switch chan: {}, Fibre switch: {}, Power meter wavelength: {}".format( ls_original, fs_original, pm_original ) )


    #if True:
    logging.debug("Test PASSED")
    npass+=1
    #else:
    #    logging.debug("Test FAILED")
    #    nfail+=1
    
    #close devices
    ld.port_close()
    fs.port_close()
    pm.port_close()
    
    logging.debug( "Finished Testing SMELLIE SuperK, pass: {}/{}, fail:{}/{}".format(npass,npass+nfail,nfail,npass+nfail) )
    
except Exception, e:
    logging.debug( "Exception:" )
    logging.debug( e )