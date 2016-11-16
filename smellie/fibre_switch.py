from smellie_config import FIBRE_SWITCH_SERIAL_PORT, FIBRE_SWITCH_BAUD_RATE, FIBRE_SWITCH_WAIT_TIME
from serial import Serial
from time import sleep
from smellie.smellie_logger import SMELLIELogger
from server.exception_handler import str_wrap_exceptions
from functools import wraps

"""
Control of the Fibre Switch hardware
"""

class FibreSwitchLogicError(Exception):
    """
    Thrown if an inconsistency is noticed *before* any instructions are sent to the hardware (i.e. a problem with code logic)
    """
    pass

class FibreSwitchHWError(Exception):
    """
    Thrown if an inconsistency is noticed *after* any hardware instruction is executed (i.e. a problem with the hardware itself)
    """
    pass

def find_global_channel_number(in_chan, out_chan):
    """
    Convert a specific combination of (input channel, output channel) into a global Fibre Switch channel number

    :returns: global channel
    :type global channel: int
    """
    return ((in_chan - 1) * 14) + out_chan

def find_input_output_number(chan):
    """
    Convert a global Fibre Switch channel number into a specific combination of (input channel, output channel)

    :returns: global channel
    :type global channel: int
    """
    input_channel = int( (chan+7)/14.1 )//1
    if (chan%14==0): output_channel = 14
    else: output_channel = chan%14
    return "({},{})".format( str(input_channel), str(output_channel) )

def check_global_channel_number(channel_num):
    """
    Check the validity of the desired global Fibre Switch channel number, which must be at most = 70 (input channel = [1, 5], output channel = [1, 14])

    :param channel_num: the global channel number to check

    :raises: :class:`.FibreSwitchLogicError` if the channel is unphysical, i.e. not between 1 and 70
    """
    if not (channel_num-1) in xrange(70):
        raise FibreSwitchLogicError("Invalid Fibre Switch channel {0} requested ... must be 1 - 70, or input = 1 - 5 and output = 1 - 14")

class FibreSwitch(object):
    """
    Controls the Fibre Switch via commands sent down a serial port.
    The port number and baud rate are set in config.py .
    """
    def __init__(self):
        self.channel_num = None
        self.serial = None
        self.isConnected = False
    
    @str_wrap_exceptions
    def port_open(self):
        """
        Open the serial port connection
        """
        SMELLIELogger.debug('SNODROP DEBUG: FibreSwitch.port_open()')
        if not self.isConnected:
            self.serial = Serial(FIBRE_SWITCH_SERIAL_PORT, FIBRE_SWITCH_BAUD_RATE, timeout=1)
            self.isConnected = True
        else:
            raise FibreSwitchLogicError("Fibre switch port already open.")
        
    @str_wrap_exceptions
    def port_close(self):
        """
        Close the serial port connection
        """
        SMELLIELogger.debug('SNODROP DEBUG: FibreSwitch.port_close()')
        if (self.serial.isOpen()): self.serial.close()
        self.isConnected = False
 
    @str_wrap_exceptions
    def execute_message(self, msg):
        """
        Send a command message over the serial port for the Fibre Switch to execute.  The message is automatically followed by \\r\\n , so you do not need to add this.

        :param msg:
        :type msg: string
        """
        SMELLIELogger.debug('SNODROP DEBUG: FibreSwitch.execute_message({})'.format(msg))
        if self.isConnected:
            self.serial.write(msg+"\r\n")
            sleep(FIBRE_SWITCH_WAIT_TIME)
        else:
            raise FibreSwitchLogicError("Fibre Switch port not open.") 
        
    @str_wrap_exceptions
    def read_back(self):
        """
        Wait for a configuration-determined time, and read back a line from the hardware

        :returns: message
        :type message: string
        """
        if self.isConnected:
            readback = self.serial.readline()
            sleep(FIBRE_SWITCH_WAIT_TIME)
            SMELLIELogger.debug('SNODROP DEBUG: FibreSwitch.read_back = {}'.format(readback))
            return readback
        else:
            raise FibreSwitchLogicError("Fibre Switch port not open.")
            return 0

    @str_wrap_exceptions
    def set_global_channel_number(self, channel_num):
        """
        Set the global Fibre Switch channel, and check that it succeeded

        :param channel_num: requested new global channel number

        :raises: :class:`.FibreSwitchLogicError`: if the requested global channel number is unphysical

        :raises: :class:`.FibreSwitchHWError` if the command is unsuccessful
        """ 
        SMELLIELogger.debug('SNODROP DEBUG: FibreSwitch.set_global_channel_number({})'.format(channel_num))
        check_global_channel_number(channel_num)
        self.execute_message("ch{0}".format(channel_num))
        if(self.get_global_channel_number() != channel_num): #check set value was set
            raise FibreSwitchHWError("Failed to set Fibre Switch to {0}".format(channel_num))
        else:
            self.channel_num = channel_num

    @str_wrap_exceptions
    def get_global_channel_number(self):
        """
        Poll the Fibre Switch for the current global channel number

        :returns: current channel
        :type current channel: int
        """
        self.execute_message("ch?")
        channel_num = int(str(self.read_back()).replace(' ','').replace('\r\n',''))
        SMELLIELogger.debug('SNODROP DEBUG: FibreSwitch.get_global_channel_number() = {}'.format(channel_num))
        return channel_num
        
    @str_wrap_exceptions
    def get_input_output_channel_number(self):
        """
        Poll the Fibre Switch for the current input and output channels

        :returns: {input channel, output channel}
        :type current channel: string
        """
        in_out_num = find_input_output_number(self.get_global_channel_number())
        SMELLIELogger.debug('SNODROP DEBUG: FibreSwitch.get_input_output_channel_number() = {}'.format(in_out_num))
        return in_out_num

    @str_wrap_exceptions
    def set_io_channel_numbers(self, in_channel, out_channel):
        """
        Set the global Fibre Switch channel number using explicit input and output channels

        :param in_channel: requested input channel
        :param out_channel: requested output channel
        
        :raises: :class:`.FibreSwitchLogicError` if the requested global channel number is unphysical

        :raises: :class:`.FibreSwitchHWError` if the command is unsuccessful
        """
        SMELLIELogger.debug('SNODROP DEBUG: FibreSwitch.set_io_channel_numbers({},{})'.format(in_channel, out_channel))
        self.set_global_channel_number(find_global_channel_number(in_channel, out_channel))

    @str_wrap_exceptions
    def get_fwr_version(self):
        """
        Get the current Fibre Switch firmware version as a string
        """
        self.execute_message("firmware?")
        fwr_ver = str(self.read_back()).replace(' ','').replace('\r\n','')
        SMELLIELogger.debug('SNODROP DEBUG: FibreSwitch.get_fwr_version = {}'.format(fwr_ver))
        return fwr_ver

    @str_wrap_exceptions
    def get_type(self):
        """
        Get the current Fibre Switch hardware model as a string
        """ 
        self.execute_message("type?")
        type = str(self.read_back()).replace(' ','').replace('\r\n','')
        SMELLIELogger.debug('SNODROP DEBUG: FibreSwitch.get_type = {}'.format(type))
        return type

    @str_wrap_exceptions
    def is_connected(self):
        """   
        Check if the connection to the device is open
        """
        return self.isConnected

    @str_wrap_exceptions
    def is_alive(self):
        """
        Quick check alive or not.
        """
        if (self.get_type() == 'mol5x14'): isAlive = True #choose to check the HW model:
        else: isAlive = False
        return isAlive
        
    @str_wrap_exceptions
    def system_state(self):
        """
        Returns a formatted string with the hardware info
        """
        return "Fibre switch (system):: Port: COM{}, Baudrate: {}, Timeout: {}sec, Type:{}, Firmware:{}".format( self.serial.port+1, self.serial.baudrate, self.serial.timeout, self.get_type(), self.get_fwr_version() )  
        
    @str_wrap_exceptions
    def current_state(self):
        """
        Return a formatted string with the current hardware settings

        :returns: 'FibreSwitch:: Port:{}, Baudrate:{}, Type:{}, Firmware version:{}, Channel:{}'
        """
        return "Fibre switch (settings):: Channel:{}".format( str(self.get_global_channel_number()) )

        
