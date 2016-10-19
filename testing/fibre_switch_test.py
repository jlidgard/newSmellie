# Test the SMELLIE fibre switch
# functions to test the functionality of all the fibre switch control code
# Test while pulsing laser and monitoring fibre_switch output with power meter

import logging, time, datetime
from smellie import fibre_switch
fs = fibre_switch.FibreSwitch()

logging.basicConfig(filename='test_fibre_switch.log', filemode="a", level=logging.DEBUG)
console = logging.StreamHandler() #print logger to console
console.setLevel(logging.DEBUG)
logging.getLogger('').addHandler(console)

npass = 0
nfail = 0

try:

    logging.debug( "Begin Testing SMELLIE Fibre Switch. {}".format( datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') ) )   
    #test current state. (in turn tests many of the getter functions).
    logging.debug( "Current state: {}".format( fs.current_state() ) )

    #test set channel
    chan_original = fs.get_global_channel_number()
    
    if (chan_original>=1 and chan_original<=69): fs.set_global_channel_number(chan_original+1)
    elif (chan_original==70): fs.set_global_channel_number(chan_original-1)
    else: logging.debug( "Error testing set channel")
    chan_new = fs.get_global_channel_number()
    logging.debug( "Test setting channel: {}, {}".format( chan_new, fs.get_input_output_channel_number() ) )
    
    time.sleep(3) #sleep for a few seconds to check power meter
    
    #set back to original channel
    fs.set_global_channel_number(chan_original)
    chan_restored = fs.get_global_channel_number()
    logging.debug( "Restore original channel: {}, {}".format(  chan_restored, fs.get_input_output_channel_number() ) )
    
    if (chan_restored==chan_original and chan_new!=chan_original): 
        logging.debug("Test PASSED")
        npass+=1
    else: 
        logging.debug("Test FAILED")
        nfail+=1
    
    logging.debug( "Finished Testing SMELLIE Fibre Switch, pass: {}/{}, fail:{}/{}".format(npass,npass+nfail,nfail,npass+nfail) )
    
except Exception, e:
    logging.debug( "Exception:" )
    logging.debug( e )