# Test the SMELLIE SuperK laser
# functions to test the functionality of the SuperK control code
# Test with the spectrometer (or, alternatively the power meter)

import logging, time, datetime
from smellie import superk
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
    sk.open_superk()
    logging.debug( "Current state: {}".format( sk.current_state() ) )
    
    #if True: 
    logging.debug("Test PASSED")
    npass+=1
    #else: 
    #    logging.debug("Test FAILED")
    #    nfail+=1
    
    #close superk   
    sk.close_superk()
    
    logging.debug( "Finished Testing SMELLIE SuperK, pass: {}/{}, fail:{}/{}".format(npass,npass+nfail,nfail,npass+nfail) )
    
except Exception, e:
    logging.debug( "Exception:" )
    logging.debug( e )