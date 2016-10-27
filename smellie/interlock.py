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
        self.serial = None
        self.isConnected = False
        
    def port_open(self):
        """
        Open the serial port connection
        """
        self.serial = Serial(INTERLOCK_SERIAL_PORT,INTERLOCK_BAUD_RATE,timeout=1)
        self.isConnected = True
    
    def port_close(self):
        """
        Close the serial port connection
        """
        if (self.serial.isOpen() ): self.serial.close()
        self.isConnected = False
        
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
        response = None
        if (self.serial.isOpen() == True ): 
            self.execute_message("v")
            response = str(self.read_back()).replace('\r\n','')
            if (response!="Relay contacts are CLOSED" and response!="Relay contacts are OPEN"):
                self.port_close()
                raise InterlockHWError("Unknown status response from interlock. Interlock state unknown.")
        else:
            raise InterlockHWError("Interlock port not open.")
        return response
        
    def is_interlocked(self):
        """
        Send a command to query the arm/disarm status of the internal relay
        :param msg:
        :returns: arm/disarm boolean: True for closed, False for open (None for unknown)
        """
        status = None
        response = self.get_status()
        if (response=="Relay contacts are CLOSED"): status = True
        elif (response=="Relay contacts are OPEN"): status = False
        else: 
            raise InterlockHWError("Unknown status response from interlock. Interlock state unknown.")
        return status

    def set_arm(self):
        """
        Send a command to arm the interlock
        
        :param msg: 'a'
        :type msg: string
        :returns: arm message (string)
        """
        response = None
        if (self.serial.isOpen() == True ): 
            self.execute_message("a")
            response = str(self.read_back()).replace('\r\n','')
        else:
            raise InterlockHWError("Interlock port not open.")
        return response
        
    def set_disarm(self):
        """
        Send a command to disarm the interlock

        :param msg: 'd'
        :type msg: string
        """
        
        if (self.serial.isOpen() == True ): 
            self.execute_message("d")
            #response = str(self.read_back()).replace('\r\n','') #arduino code doesn't send a disarm message unlike the arm.. (change?)
        else:
            raise InterlockHWError("Interlock port not open.")
        return 0
        
    def send_keepalive(self):
        """
        Send a command to the interlock to maintain its armed state
                
        :param msg: '1'
        :type msg: string
        """
        if (self.serial.isOpen() == True ): 
            self.execute_message("1")
        else:
            raise InterlockHWError("Interlock port not open.")
        return 0

    def is_connected(self):
        """   
        Check if the connection to the device is open
        """
        return self.isConnected
        
    def is_alive(self):
        """
        Quick check alive or not.
        """
        isAlive = None
        if self.isConnected: 
            checkValue = self.is_interlocked()  #choose to check the interlock status:
        else:
            self.port_open()
            checkValue = self.is_interlocked()
            self.port_close()
        if (checkValue == True or checkValue == False): isAlive = True
        else: isAlive = False
        return isAlive
        
    def current_state(self):
        """
        Return a formatted string with the current hardware settings

        :returns: 'Interlock:: Port:{}, Baudrate:{}, Status message:{}, State: {}'
        """
        return "Interlock:: Status message:{}, State: {}".format( self.get_status(), self.get_status_boolean() )


