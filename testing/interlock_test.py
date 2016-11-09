# Test the SMELLIE laser keepalive
# functions to test the functionality of the interlock control code
# Test with superK GUI open, watch interlock status reported on gui

import logging, time, datetime
from smellie import interlock
il = interlock.Interlock()

logging.basicConfig(filename='C:\SMELLIE\logs\test_interlock.log', filemode="a", level=logging.DEBUG)
console = logging.StreamHandler() #print logger to console
console.setLevel(logging.DEBUG)
logging.getLogger('').addHandler(console)

npass = 0
nfail = 0

try:

    logging.debug( "Begin Testing SMELLIE Interlock. {}".format( datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') ) ) 

    #open serial connection
    il.port_open()
    
    #test current state. (in turn tests many of the getter functions).
    logging.debug( "Current state: {}".format( il.current_state() ) )

    #test disarm (watch status quickly flash on & off)
    logging.debug("Test Sending Arm then a Disarm")
    il.set_arm()
    il.set_disarm()
    status = il.is_interlocked()
    logging.debug("Get status: {}, state: {}".format( il.get_status(), status ) )
    if (status==0): 
        logging.debug("Test PASSED")
        npass+=1
    else: 
        logging.debug("Test FAILED")
        nfail+=1
    
    #test arm timeout
    logging.debug("Test Sending Arm and waiting for time-out (no keepalive sent): {}".format( il.set_arm() ) )
    status = il.is_interlocked()
    logging.debug("Get state: {}".format( status ) )
    logging.debug("Wait 1.1 seconds")
    time.sleep(1.1)
    status2 = il.is_interlocked()
    logging.debug("Get state: {}".format( status2 ) )
    if (status==1 and status2==0): 
        logging.debug("Test PASSED")
        npass+=1
    else: 
        logging.debug("Test FAILED")
        nfail+=1
    
    #test sending keepalive
    logging.debug("Test Sending Arm with keep alive @ 1Hz: {}".format( il.set_arm() ) )
    status = il.is_interlocked()
    pulses = 0
    while (pulses < 5):
        pulses+=1
        logging.debug("Test keep alive pulse {}".format( pulses ) )
        il.send_keepalive()
        time.sleep(1)
    status2 = il.is_interlocked()
    logging.debug("Get state: {}".format( status2 ) )
    if (status==1 and status2==1): 
        logging.debug("Test PASSED")
        npass+=1
    else: 
        logging.debug("Test FAILED")
        nfail+=1
        
    #close serial connection
    il.port_close()
    
    logging.debug( "Finished Testing SMELLIE Fibre Switch, pass: {}/{}, fail:{}/{}".format(npass,npass+nfail,nfail,npass+nfail) )
    
except Exception, e:
    logging.debug( "Exception:" )
    logging.debug( e )