from smellie_config import FIBRE_SWITCH_SERIAL_PORT, FIBRE_SWITCH_BAUD_RATE, FIBRE_SWITCH_WAIT_TIME
from serial import Serial
from time import sleep

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
        self.serial = Serial()
        self.serial.port = FIBRE_SWITCH_SERIAL_PORT
        self.serial.baudrate = FIBRE_SWITCH_BAUD_RATE

    def execute_message(self, msg):
        r"""
        Send a command message over the serial port for the Fibre Switch to execute.  The message is automatically followed by \\r\\n , so you do not need to add this.

        :param msg:
        :type msg: string
        """
        sleep(FIBRE_SWITCH_WAIT_TIME)
        self.serial.write(msg+"\r\n")
        
    def read_back(self):
        """
        Wait for a configuration-determined time, and read back a line from the hardware

        :returns: message
        :type message: string
        """
        sleep(FIBRE_SWITCH_WAIT_TIME)
        readback = self.serial.readline()
        return readback

    def set_global_channel_number(self, channel_num):
        """
        Set the global Fibre Switch channel, and check that it succeeded

        :param channel_num: requested new global channel number

        :raises: :class:`.FibreSwitchLogicError`: if the requested global channel number is unphysical

        :raises: :class:`.FibreSwitchHWError` if the command is unsuccessful
        """
        check_global_channel_number(channel_num)
        self.channel_num = channel_num
        self.serial.open()
        self.execute_message("ch{0}".format(channel_num))
        self.serial.close()
        if(self.get_global_channel_number() != channel_num):
            raise FibreSwitchHWError("Failed to set Fibre Switch to {0}".format(channel_num))

    def get_global_channel_number(self):
        """
        Poll the Fibre Switch for the current global channel number

        :returns: current channel
        :type current channel: int
        """
        self.serial.open()
        self.execute_message("ch?")
        readback = int(str(self.read_back()).replace(' ','').replace('\r\n',''))
        self.serial.close()
        return readback
        
    def get_input_output_channel_number(self):
        """
        Poll the Fibre Switch for the current input and output channels

        :returns: {input channel, output channel}
        :type current channel: string
        """
        readback = self.get_global_channel_number()
        readback = find_input_output_number(readback)
        return readback

    def set_io_channel_numbers(self, in_channel, out_channel):
        """
        Set the global Fibre Switch channel number using explicit input and output channels

        :param in_channel: requested input channel
        :param out_channel: requested output channel
        
        :raises: :class:`.FibreSwitchLogicError` if the requested global channel number is unphysical

        :raises: :class:`.FibreSwitchHWError` if the command is unsuccessful
        """
        self.set_global_channel_number(find_global_channel_number(in_channel, out_channel))
        
    def get_fwr_version(self):
        """
        Get the current Fibre Switch firmware version as a string
        """
        self.serial.open()
        self.execute_message("firmware?")
        readback = str(self.read_back()).replace(' ','').replace('\r\n','')
        self.serial.close()
        return readback
        
    def get_type(self):
        """
        Get the current Fibre Switch hardware model as a string
        """
        self.serial.open()
        self.execute_message("type?")
        readback = str(self.read_back()).replace(' ','').replace('\r\n','')
        self.serial.close()
        return readback

    def current_state(self):
        """
        Return a formatted string with the current hardware settings

        :returns: 'FibreSwitch:: Type:{}, Firmware version:{}, Channel:{}'
        """
        return "FibreSwitch:: Type:{0}, Firmware:{1}, Channel:{2}".format(self.get_type(),self.get_fwr_version(), str(self.get_global_channel_number()) )

        
