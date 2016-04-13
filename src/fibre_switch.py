from config import FIBRE_SWITCH_SERIAL_PORT, FIBRE_SWITCH_BAUD_RATE, FIBRE_SWITCH_WAIT_TIME
from serial import Serial
from time import sleep

"""
Control of the fibre switch hardware
"""

class FiberSwitchLogicError(Exception):
    """
    Thrown on inconsistencies noticed *before* any directions to the hardware
    """
    pass

class FiberSwitchHWError(Exception):
    """
    Thrown *after* a hardware instruction is exectued, if a discrepancy is detected
    """
    pass

def global_channel_number(in_chan, out_chan):
    '''
    Convert an (input channel, output channel) to a global channelID
    '''
    return (input_channel - 1) * 14 + out_chan    

def check_channel(channel_num):
    '''
    Fibre switch is limited to 70 channels input =  [1, 5], output = [1, 14]

    :param channel_num: The channel number to check

    :raises: :class:`.FiberSwitchLogicError` if the channel is unphysical
    '''
    if not ((channel_num > 1) and (channel_num < 70)):
        raise FiberSwitchError("Invalid Fibre Switch channel {0} requested, must be 1-70 or input = 1-5 output = 1-14")


class FibreSwitch(object):
    '''
    Controlles the fibre switch via commands sent down a serial port.
    Port and baud rate are set in config.py
    '''
    def __init__(self):
        self.channel_num = None
        self.serial      = Serial()
        self.serial.port = FIBRE_SWITCH_SERIAL_PORT
        self.serial.baudrate = FIBRE_SWITCH_BAUD_RATE

    def execute_message(self, msg):
        r"""
        Send a command message over the serial port, followed by \\r\\n
        to exectute (so you do not need to add this)

        :param msg:
        :type msg: string
        """
        self.serial.open()
        self.serial.write(msg)
        self.serial.write("\r\n") # executes previous command
        self.serial.close()

    def set_channel(self, channel_num):
        """
        Set the fibre switch channel, and check that it suceeded

        :param channel_num: requested new channel 

        :raises: :class:`.FiberSwitchLogicError`: if the channel is unphysical
        :raises: :class:`.FiberSwitchHWError` if the command is unsucessful
        """

        check_channel(channel_num)
        self.channel_num = channel_num
        self.execute_message("ch{0}".format(channel_num))
        if(get_channel() != channel_num):
            raise FiberSwitchHWError("Failed to set fibre switch to {0}".format(channel_num))

    def read_back(self):
        """
        Wait a configuration determined time, and read back a line 
        from the HW

        :returns: message
        :type message: string
        """
        sleep(FIBRE_SWITCH_WAIT_TIME)
        return self.serial.readline()

    def get_channel(self):
        """
        Poll the hardware for the current channel

        :returns: current channel
        :type current channel: int
        """
        self.execute_message("ch?")
        return self.read_back()

    def set_io_channels(self, in_channel, out_channel):
        """
        Set the channel number using an input and output channel

        :param in_channel: Input
        :param out_channel: Output
        
        :raises: :class:`.FiberSwitchLogicError` if channel is unphysical

        :raises: :class:`.FiberSwitchHWError` if the command is unsucessful
        """
        set_channel(global_channel_number(in_channel, out_channel))
        
    def get_fwr_version(self):
        """
        Get the current fwr version as a string
        """
        self.execute_message("firmware?")
        return self.read_back()
