# Test the SMELLIE fibre switch
# functions to test the functionality of all the fibre switch control code
# Test while pulsing laser and monitoring fibre_switch output with power meter

import logging, time, datetime
from smellie import fibre_switch

import paramiko
paramiko.util.log_to_file('./test_status_scp_login.log')

fs = fibre_switch.FibreSwitch()

logging.basicConfig(filename='C:/SMELLIE/software/smellieReport.txt', filemode="a", level=logging.DEBUG)
console = logging.StreamHandler() #print logger to console
console.setLevel(logging.DEBUG)
logging.getLogger('').addHandler(console)

npass = 0
nfail = 0

try:

    #logging.debug( "Begin Testing SMELLIE Fibre Switch. {}".format( datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%M-%d %H:%M:%S') ) )   
    #test current state. (in turn tests many of the getter functions).
    
    fibreSwitchTest = fs.current_state()
    
    logging.debug( "FibreSwitch state: {}".format( fibreSwitchTest ) )
 
    #logging.debug( "Finished Testing SMELLIE Status mail, pass: {}/{}, fail:{}/{}".format(npass,npass+nfail,nfail,npass+nfail) )
    
except Exception, e:
    logging.debug( "Exception:" )
    logging.debug( e )
    
finally:
    #open SSH connection
    myhost = 'pplxint9.physics.ox.ac.uk'
    myport = 22
    myuser = 'lidgard'
    mykey = paramiko.RSAKey.from_private_key_file('C:/SMELLIE/software/smelliekey.prv')
    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(myhost, myport, username = myuser, pkey = mykey)
    sftp = ssh.open_sftp()

    #send file
    filepath = '/home/lidgard/SMELLIE/smellieReport.txt'
    localpath = 'C:/SMELLIE/software/smellieReport.txt'
    sftp.put(localpath, filepath)

    #close connections
    sftp.close()
    ssh.close()