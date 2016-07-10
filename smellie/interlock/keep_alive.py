from serial import Serial
from config import INTERLOCK_PORT, INTERLOCK_BAUD_RATE

def pulse_keep_alive(port, baudrate):
    '''
    Pulse 01010101 down serial port at baudrate
    '''
    serial_connection = Serial(INTERLOCK_PORT, INTERLOCK_BAUD_RATE)


    while True:
        try:
            serial_connection.write("01010101")
            pass
        except KeyboardInterrupt:
            print "interlockSMELLIE::Keyboard Interrupt has locked the Laser.Please Restart"
            break
        



    
        
