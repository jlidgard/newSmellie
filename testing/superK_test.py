# Test the SMELLIE SuperK laser
# functions to test the functionality of the SuperK control code
# Test with the spectrometer (or, alternatively the power meter)

import logging, time, datetime
from smellie import fibre_switch, ni_trigger_generator, superk
fs = fibre_switch.FibreSwitch()
ni = ni_trigger_generator.TriggerGenerator()
sk = superk.SuperK()

logging.basicConfig(filename=r'C:\SMELLIE\software\newSmellie\testing\test_superk.log', filemode="a", level=logging.DEBUG)
console = logging.StreamHandler() #print logger to console
console.setLevel(logging.DEBUG)
logging.getLogger('').addHandler(console)

npass = 0
nfail = 0

try:
    logging.debug( "Begin Testing SMELLIE SuperK. {}".format( datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') ) )   
    
    #test current state. (in turn tests many of the getter functions).
    fs.port_open()
    sk.open_superk()
    
    #record original settings
    wavelength_low_original, wavelength_high_original = sk.get_wavelengths()
    fs_original = fs.get_global_channel_number()
    
    #Test1: Current state
    logging.debug( "Current state: {}".format( sk.current_state() ) )
    
    #Test2: Turn ready state (lock and emission) on and off
    
    #Test3: Move wavelengths
    
    #Test4: Fire laser (recieve triggers)
    
    #if True: 
    logging.debug("Test PASSED")
    npass+=1
    #else: 
    #    logging.debug("Test FAILED")
    #    nfail+=1
    
    #close superk 
    fs.port_close()
    sk.port_close()
    
    logging.debug( "Finished Testing SMELLIE SuperK, pass: {}/{}, fail:{}/{}".format(npass,npass+nfail,nfail,npass+nfail) )
    
except Exception, e:
    logging.debug( "Exception:" )
    logging.debug( e )