from smellie_config import INTERLOCK_SERIAL_PORT, INTERLOCK_BAUD_RATE, INTERLOCK_WAIT_TIME
from serial import Serial
from time import sleep

"""
Control of the Interlock hardware
"""

class InterlockHWError(Exception):
    """
    Thrown if an inconsistency is noticed *after* any hardware instruction is executed (i.e. a problem with the hardware itself)
    """
    pass

class Interlock(object):
    """
    Controls the interlock via commands sent down a serial port.
    The port number and baud rate are set in config.py
    """
    def __init__(self):
        self.channel_num = None
        self.serial = Serial(INTERLOCK_SERIAL_PORT,INTERLOCK_BAUD_RATE,timeout=1)
    
    def __del__(self):
        if (self.serial.isOpen() ): self.serial.close()
        
    def execute_message(self, msg):
        """
        Send a command message over the serial port for the Fibre Switch to execute.  The message is automatically followed by \\r\\n , so you do not need to add this.

        :param msg:
        :type msg: string
        """
        self.serial.write(msg+"\r\n")
        sleep(INTERLOCK_WAIT_TIME)
        
    def read_back(self):
        """
        Wait for a configuration-determined time, and read back a line from the hardware

        :returns: message
        :type message: string
        """
        readback = self.serial.readline()
        sleep(INTERLOCK_WAIT_TIME)
        return readback
        
    def get_status(self):
        """
        Send a command to query the arm/disarm status of the internal relay
        :param msg:
        :returns: arm/disarm status message (string)
        """
        if (self.serial.isOpen() == False ): self.serial.open()
        self.execute_message("v")
        response = str(self.read_back()).replace('\r\n','')
        if (response!="Relay contacts are CLOSED" and response!="Relay contacts are OPEN"):
            self.serial.close()
            raise InterlockHWError("Unknown status response from interlock. Interlock state unknown.")
        self.serial.close()
        return response
        
    def get_status_boolean(self):
        """
        Send a command to query the arm/disarm status of the internal relay
        :param msg:
        :returns: arm/disarm boolean: 1 for closed, 0 for open (-1 for unknown) (int)
        """
        if (self.serial.isOpen() == False ): self.serial.open()
        self.execute_message("v")
        response = str(self.read_back()).replace('\r\n','')
        self.serial.close()
        if (response=="Relay contacts are CLOSED"): status = 1
        elif (response=="Relay contacts are OPEN"): status = 0
        else: 
            self.serial.close()
            raise InterlockHWError("Unknown status response from interlock. Interlock state unknown.")
        return status

    def set_arm(self):
        """
        Send a command to arm the interlock
        
        :param msg: 'a'
        :type msg: string
        :returns: arm message (string)
        """
        if (self.serial.isOpen() == False ): self.serial.open()
        self.execute_message("a")
        response = str(self.read_back()).replace('\r\n','')
        self.serial.close()
        return response
        
    def set_disarm(self):
        """
        Send a command to disarm the interlock

        :param msg: 'd'
        :type msg: string
        """
        if (self.serial.isOpen() == False ): self.serial.open()
        self.execute_message("d")
        #response = str(self.read_back()).replace('\r\n','') #arduino code doesn't send a disarm unlike the arm.. (change?)
        self.serial.close()
        #return response
        
    def send_keepalive(self):
        """
        Send a command to the interlock to maintain its armed state
                
        :param msg: '1'
        :type msg: string
        """
        if (self.serial.isOpen() == False ): self.serial.open()
        self.execute_message("1")
        self.serial.close()
        
    def get_port(self):
        """
        Get the port number
        """
        return self.serial.port
        
    def get_baudrate(self):
        """
        Get the baud rate
        """
        return self.serial.baudrate

    def current_state(self):
        """
        Return a formatted string with the current hardware settings

        :returns: 'Interlock:: Port:{}, Baudrate:{}, Status message:{}, State: {}'
        """
        return "Interlock:: Port:{}, Baudrate:{}, Status message:{}, State: {}".format( self.get_port(),self.get_baudrate(),self.get_status(), self.get_status_boolean() )


