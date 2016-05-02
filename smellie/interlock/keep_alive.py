from serial import Serial
from config import INTERLOCK_PORT, INTERLOCK_BAUD_RATE

def pulse_keep_alive():
    """
    Pulse 01010101 down the serial port at the specified baud rate
    """
    serial_connection = Serial(INTERLOCK_PORT, INTERLOCK_BAUD_RATE)

    while True:
        try:
            serial_connection.write("01010101")
            pass
        except KeyboardInterrupt:
            print "SMELLIE Interlock : Keyboard Interrupt has locked the Laser ... please reset the interlock and Restart"
            break
