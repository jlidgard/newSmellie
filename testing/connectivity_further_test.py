# Test connection to SMELLIE hardware
# functions to test if a connection can be made to each piece of equipment

import logging, time, datetime
from smellie import laser_switch, ni_trigger_generator, fibre_switch, laser_driver, interlock, power_meter, superk_driver, spectrometer

ls = laser_switch.LaserSwitch()
ni = ni_trigger_generator.TriggerGenerator()
fs = fibre_switch.FibreSwitch()
ld = laser_driver.LaserDriver()
il = interlock.Interlock()
pm = power_meter.PowerMeter()
sk = superk_driver.SuperkDriver()
sp = spectrometer.Spectrometer()

logging.basicConfig(filename='C:/SMELLIE/logs/test_connectivity_further.log', filemode="a", level=logging.DEBUG)
console = logging.StreamHandler() #print logger to console
console.setLevel(logging.DEBUG)
logging.getLogger('').addHandler(console)

npass = 0
nfail = 0

try:
    logging.debug( "Begin Testing SMELLIE equipment connectivity further (is_alive() method): {}".format( datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') ) )   
    
    #Now open (and close) all and test if connection is successful 
    logging.debug( "Testing connected states (True = connected):" )
    lsc = ls.is_alive()
    logging.debug( "Laser Switch: {}".format( lsc ) )
    
    nic = ni.is_alive()
    logging.debug( "NI DAQ: {}".format( nic ) )
    
    fs.port_open()
    fsc = fs.is_alive()
    logging.debug( "Fibre Switch: {}".format( fsc ) )
    fs.port_close()
    
    ld.port_open()
    ldc = ld.is_alive()
    logging.debug( "PQ Lasers: {}".format( ldc ) )
    ld.port_close()
    
    il.port_open()
    ilc = il.is_alive()
    logging.debug( "Interlock: {}".format( ilc ) )
    il.port_close()
    
    pm.port_open()
    pmc = pm.is_alive()
    logging.debug( "Power Meter: {}".format( pmc ) )
    pm.port_close()
    
    sk.port_open()
    skc = sk.is_alive()
    logging.debug( "SuperK Laser: {}".format( skc ) )
    sk.port_close()
    
    sp.port_open()
    spc = sp.is_alive()
    logging.debug( "Spectrometer: {}".format( spc ) )   
    sp.port_close()

    if (lsc==True and nic==True and fsc==True and ldc==True and ilc==True and pmc==True and skc==True and spc==True): 
        logging.debug("Test PASSED")
        npass+=1
    else: 
        logging.debug("Test FAILED")
        nfail+=1
    
    logging.debug( "Finished Testing SMELLIE equipment connection status. pass: {}/{}, fail:{}/{}".format(npass,npass+nfail,nfail,npass+nfail) )
    
except Exception, e:
    logging.debug( "Exception:" )
    logging.debug( e )