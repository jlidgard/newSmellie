# Test the SMELLIE PicoQuant (PQ) lasers
# Runs an intensity scan of each laser and saves to file (so also uses laser switch, fibre switch, powermeter).

import logging, time, datetime, numpy
from multiprocessing.pool import ThreadPool
from smellie import laser_driver, power_meter, fibre_switch, laser_switch, ni_trigger_generator

def measure_power(nsamples,sample_rate):
    print "Power measurement begin."
    power_mean, power_sd, power_range = pm.get_mean_power(nsamples,sample_rate)
    print "Power measurement finished."
    return power_mean, power_sd, power_range
    
def generate_triggers(n_pulses, repetition_rate):
    ni.generate_triggers(n_pulses, repetition_rate, 'SUPERK') 
    return 0

if __name__ == "__main__":
    logging.basicConfig(filename=r'C:\SMELLIE\software\newSmellie\testing\test_PQ_intensity_scan.log', filemode="a", level=logging.DEBUG)
    console = logging.StreamHandler() #print logger to console
    console.setLevel(logging.DEBUG)
    logging.getLogger('').addHandler(console)

    npass = 0
    nfail = 0
    #ls_original = None
    #fs_original = None
    pm_original = None

    try:

        #ld = laser_driver.LaserDriver()
        pm = power_meter.PowerMeter()
        #fs = fibre_switch.FibreSwitch()
        #ls = laser_switch.LaserSwitch()
        ni = ni_trigger_generator.TriggerGenerator()
        pool = ThreadPool(processes=1)
        
        logging.debug( "Begin Testing SMELLIE PQ intensity scan. {}".format( datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') ) )
        
        #open devices
        #ld.port_open()
        #fs.port_open()
        pm.port_open()
        
        #record original settings
        #ls_original = ls.get_active_channel()
        #fs_original = fs.get_global_channel_number()
        pm_original = pm.get_wavelength()
        
        #logging.debug( "Current settings: Laser switch chan: {}, Fibre switch: {}, Power meter wavelength: {}".format( ls_original, fs_original, pm_original ) )
        
        #------------------- testing -----------------
        #get current state
        #logging.debug( "Laser Driver current state: {}".format( ld.current_state() ) )
        #logging.debug( "Laser Switch current state: {}".format( ls.current_state() ) )
        
        laser_numbers = range(1,5,1) #test lasers 1 thru 4
        intensities = range(0,2,1) #from 0 to 100% intensity
        wavelengths = (375, 407, 446, 495)
        measure_power_args = (10,10) #(nsamples,rate)
        trig_pulses = 30000
        trig_rate = 10000 #Hz


        
        #for laser_number, wavelength in zip(laser_numbers,wavelengths):
        
        laser_number = 4
        wavelength = 495
        #ls.set_active_channel(laser_number)
        #fs.set_io_channel_numbers(laser_number, 14) #output fibre 14 = power meter
        pm.set_wavelength(wavelength)

        powerMean = []
        powerSD = []
        powerRange = []
        
        logging.debug( "Begin intensity scan of laser: {} ({}nm)".format(  laser_number, wavelength ) )
        

        for intensity in intensities:
            
            async_measure_power = pool.apply_async(measure_power, measure_power_args)
            print "Triggers begin."
            ni.generate_triggers(trig_pulses, trig_rate, 'SUPERK')
            print "Triggers finished."
            power_mean, power_sd, power_range = async_measure_power.get()
            powerMean.append( power_mean )
            powerSD.append( power_sd )
            powerRange.append( power_range )

            print "(laser, wavelength, intensity(%), power_mean(W), power_sd(W), power_range(W)): {}, {}, {}, {}, {}".format(laser_number, wavelength, intensity, power_mean, power_sd, power_range)
            
        fileOut = open(r'C:\SMELLIE\software\newSmellie\testing\test_PQ_intensity_scan_{}nm.dat'.format(wavelength), 'a')
        fileOut.write('Laser, Wavelength(nm):'.format( laser_number, wavelength ))
        fileOut.write('Intensity(%), Power_mean(W), Power_sd(W), Power_range(W)\n')
        for i,j,k,l in zip(intensities,powerMean,powerSD,powerRange):
            fileOut.write( '{},{},{},{}\n'.format( i,j,k,l ) )
        fileOut.closed

        logging.debug( "Finish intensity scan of laser: {} ({}nm)".format(  laser_number, wavelength ) )
     
        #-------------------end of testing -----------------
        
    except Exception, e:
        logging.debug( "Exception:" )
        logging.debug( e )
        
    finally:
        
        #set back to original settings
        #ls.set_active_channel(ls_original)
        #fs.set_global_channel_number(fs_original)
        #pm.set_wavelength(pm_original)
        #ls_restored = ls.get_active_channel()
        #fs_restored = fs.get_global_channel_number()
        pm_restored = pm.get_wavelength()
        #logging.debug( "Current settings (restored/original): Laser switch chan: {}/{}, Fibre switch: {}/{}, Power meter wavelength: {}/{}".format( ls_restored,ls_original, fs_restored,fs_original, pm_restored,pm_original ) )

        #if True:
        logging.debug("Test PASSED")
        npass+=1
        #else:
        #    logging.debug("Test FAILED")
        #    nfail+=1
        
        #close devices
        #ld.port_close()
        #fs.port_close()
        pm.port_close()
        
        logging.debug( "Finished Testing SMELLIE PQ intensity scan. pass: {}/{}, fail:{}/{}".format(npass,npass+nfail,nfail,npass+nfail) )
        
