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

    def __init__(self):
        """
        Controls the arduino stepper motor controller attached to the Varia ND filter.
        """
        self.serial = None
         
    def open_controller(self):
        """
        Send a command message over the serial port for the motor controller to execute.  The message is automatically followed by \\r\\n , so you do not need to add this.

        :param msg:
        :type msg: string
        """
        self.channel_num = None
        self.serial = Serial(VARIAMOTOR_SERIAL_PORT,VARIAMOTOR_BAUD_RATE,timeout=1)
        sleep(2)
        self.serial.flushInput()
        self.serial.flushOutput()
        sleep(VARIAMOTOR_WAIT_TIME)
            
    def close_controller(self):
        """
        Send a command message over the serial port for the motoro controller to execute.  The message is automatically followed by \\r\\n , so you do not need to add this.

        :param msg:
        :type msg: string
        """    
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
     
    def get_connected_status(self):
        """
        Send a command to query the status of the Varia stepper motor arduino controller
        :param msg:
        :returns: get the current connection status of the controller. If connected returns: 'Connected.' (string)
        """
        self.execute_message( "z" )
        response = str(self.read_back()).replace('\r\n','')
        return response

    def get_position(self):
        """
        Send a command to query the status of the Varia stepper motor arduino controller
        :param msg:
        :returns: get the current position of the motor 'Position: {}' (string)
        """
        self.execute_message( "a" )
        response = str(self.read_back()).replace('\r\n','')
        return response

    def get_max_speed(self):
        """
        Send a command to query the status of the Varia stepper motor arduino controller
        :param msg:
        :returns: max speed of motor 'Max Speed: {}' (string)
        """
        self.execute_message( "j" )
        response = str(self.read_back()).replace('\r\n','')
        return response

    def set_max_speed(self, speedValue=5):
        """
        Send a command to the Varia stepper motor arduino controller
        The default argument is 5, which sets the acceleration to 5 step/s.
        
        :param msg: 'c'
        :type msg: string
        """
        self.execute_message( "c"+str(speedValue) )

    def set_acceleration(self, accelValue=1):
        """
        Send a command to the Varia stepper motor arduino controller
        The default argument is 1, which sets the acceleration to 1 step/s/s.
        
        :param msg: 'i'
        :type msg: string
        """
        self.execute_message( "i"+str(accelValue) )
        
    def set_position(self, positionValue=0):
        """
        Send a command to the Varia stepper motor arduino controller
        The default argument is 0, which sets the position to the current position.

        :param msg: 'd'
        :type msg: string
        """
        self.execute_message( "d"+str(positionValue) )
        
    def set_reference_position(self, positionValue=0):
        """
        Send a command to the Varia stepper motor arduino controller
        The default argument is 0, which sets the reference position to the current position.
        
        :param msg: 'e'
        :type msg: string
        """
        self.execute_message( "e"+str(positionValue) )
        
    def get_home_status(self):
        """
        Send a command to query the status of the Varia stepper motor arduino controller. 
        The sensor is read by a digital pin and is high (1) when the switch is not pressed (low when pressed i.e. at home).
        Controller returns either 'Home sensor: 0' or 'Home sensor: 1' which is converted to True/False.
        :param msg:
        :returns: status of home switch: True, False or None (for a return string which isn't recognised) (string)
        """
        self.execute_message( "f" )
        response = str(self.read_back()).replace('\r\n','')
        if (response == 'Home sensor: 1'):
            homeStatus = False
        elif (response == 'Home sensor: 0'):
            homeStatus = True
        else: homeStatus = None
        return homeStatus

    def current_state(self):
        """
        Return a formatted string with the current hardware settings

        :returns: 'variaMotor:: Port:{}, Baudrate:{}, Current Position:{}, Set Max Speed: {}'
        """
        return "variaMotor:: Port:{}, Baudrate:{}, Position:{}, Speed: {}".format( self.serial.port, self.serial.baudrate, self.get_position() , self.get_speed() )


