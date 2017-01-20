from xmlrpclib import ServerProxy

if __name__ == "__main__":
    client = ServerProxy("http://localhost:5020")
    #print client.current_state()
    
    client.new_run(1234567)
    #Test firing SuperK laser (monitor power meter).
    #client.superk_master_mode(1, 1000, 6000, 6100, 5, 14, 5000, 0.25)
    #Test the current state after firing laser.
    #currentState = controller.current_state()
    #logging.debug('Current state: \n{}'.format(currentState))
    client.laserheads_master_mode(4, 1000, 20000, 4, 14, 2000, 0.25)