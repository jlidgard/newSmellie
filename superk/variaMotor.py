from smellie_config import VARIAMOTOR_SERIAL_PORT, VARIAMOTOR_BAUD_RATE, VARIAMOTOR_WAIT_TIME
from serial import Serial
from time import sleep

"""
Control of the Varia stepper motor arduino controller hardware
"""

class variaMotorHWError(Exception):
    """
    Thrown if an inconsistency is noticed *after* any hardware instruction is executed (i.e. a problem with the hardware itself)
    """
    pass

class VariaMotor(object):
    """
    Controls the Varia stepper motor arduino controller via commands sent down a serial port.
    The port number and baud rate are set in config.py
    """
    def __init__(self):
        self.channel_num = None
        self.serial = Serial(VARIAMOTOR_SERIAL_PORT,VARIAMOTOR_BAUD_RATE,timeout=20)
        self.execute_message( "z" )
        response = str(self.read_back()).replace('\r\n','')
    
    def __del__(self):
        if (self.serial.isOpen() ): self.serial.close()
        
    def execute_message(self, msg):
        """
        Send a command message over the serial port for the motoro controller to execute.  The message is automatically followed by \\r\\n , so you do not need to add this.

        :param msg:
        :type msg: string
        """
        self.serial.write(msg+"\r\n")
        sleep(VARIAMOTOR_WAIT_TIME)
        
    def read_back(self):
        """
        Wait for a configuration-determined time, and read back a line from the hardware

        :returns: message
        :type message: string
        """
        readback = self.serial.readline()
        sleep(VARIAMOTOR_WAIT_TIME)
        return readback
        
    def get_position(self):
        """
        Send a command to query the arm/disarm status of the internal relay
        :param msg:
        :returns: arm/disarm status message (string)
        """
        #if (self.serial.isOpen() == True ): 
        #    print("was open")
        #    self.serial.close()
        #    sleep(10)
        #self.serial.open()
        self.execute_message( "a" )
        response = str(self.read_back()).replace('\r\n','')
        #self.serial.close()
        #sleep(1)
        return response
        
    def get_speed(self):
        """
        Send a command to query the arm/disarm status of the internal relay
        :param msg:
        :returns: arm/disarm status message (string)
        """
        #if (self.serial.isOpen() == False ): self.serial.open()
        self.execute_message( "b" )
        response = str(self.read_back()).replace('\r\n','')
        #self.serial.close()
        return response

    def set_speed(self, speedValue):
        """
        Send a command to arm the Varia stepper motor arduino controller
        
        :param msg: 'a'
        :type msg: string
        :returns: arm message (string)
        """
        #if (self.serial.isOpen() == True ):
        #    print("was open")
        #    self.serial.close()
        #    sleep(1)
        #self.serial.open()
        self.execute_message( "c"+str(speedValue) )
        response = str(self.read_back()).replace('\r\n','')
        #sleep(1)
        #self.serial.close()
        return response
        
    def set_position(self, positionValue):
        """
        Send a command to arm the Varia stepper motor arduino controller
        
        :param msg: 'a'
        :type msg: string
        :returns: arm message (string)
        """
        #if (self.serial.isOpen() == False ): self.serial.open()
        self.execute_message( "d"+str(positionValue) )
        response = str(self.read_back()).replace('\r\n','')
        #self.serial.close()
        return response
        
    def set_reference_position(self, positionValue):
        """
        Send a command to arm the Varia stepper motor arduino controller
        
        :param msg: 'a'
        :type msg: string
        :returns: arm message (string)
        """
        #if (self.serial.isOpen() == False ): self.serial.open()
        self.execute_message( "e"+str(positionValue) )
        response = str(self.read_back()).replace('\r\n','')
        #self.serial.close()
        return response
        
    def get_home_position(self):
        """
        Send a command to query the arm/disarm status of the internal relay
        :param msg:
        :returns: arm/disarm status message (string)
        """
        #if (self.serial.isOpen() == False ): self.serial.open()
        self.execute_message( "f" )
        response = str(self.read_back()).replace('\r\n','')
        #self.serial.close()
        return response
        
    def current_state(self):
        """
        Return a formatted string with the current hardware settings

        :returns: 'variaMotor:: Port:{}, Baudrate:{}, Current Position:{}, Set Speed: {}'
        """
        return "variaMotor:: Port:{}, Baudrate:{}, Current Position:{}, Set Speed: {}".format( self.serial.port, self.serial.baudrate, self.get_position() , self.get_speed() )


