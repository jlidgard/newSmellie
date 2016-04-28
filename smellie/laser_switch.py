from config import RELAY_COM_CHANNEL, RELAY_SLEEP
from time import sleep

"""
Control of the Laser Switch hardware
"""

def invert(bit):
    '''
    Invert the input bit, i.e. convert 0 to 1, or 1 to 0

    :param bit: the input bit
    '''
    if bit in (0, 1):
        return (not bit)
    raise TypeError("Cannot invert bit - not a boolean!")

def translate_bits_big_endian(b1, b2, b3):
    '''
    Convert a binary value into a sequence of bytes, according to big-endian ordering
    '''
    return int("{2}{1}{0}".format(b1, b2, b3), 2)

class LaserSwitchLogicError(Exception):
    """
    Thrown if an inconsistency is noticed *before* any instructions are sent to the hardware (i.e. a problem with code logic)
    """
    pass

class LaserSwitchHWError(Exception):
    """
    Thrown if an inconsistency is noticed *after* any hardware instruction is executed (i.e. a problem with the hardware itself)
    """
    pass

class LaserSwitch(object):
    '''
    Controls the Laser Switch via commands sent down a USB port.
    The port number is set in config.py .
    '''
    def __init__(self):
        self.com_channel = RELAY_COM_CHANNEL
        self.connection = U12()

    def selected_channel_up(self):
        """
        Increment the currently selected Laser Switch channel by + 1

        :raises: :class:`.LaserSwitchHWError` if the command is unsuccessful
        """
        original_channel = get_selected_channel()
        self.connection.eDigitalOut(self.com_channel, 1, writeD = 1) 
        self.connection.eDigitalOut(self.com_channel, 0, writeD = 1) 
        self.connection.eDigitalOut(self.com_channel, 1, writeD = 1) 
        if (1 + original_channel) != get_selected_channel():
            raise LaserSwitchHWError("Failed to increment the selected Laser Switch channel number!")

    def execute(self):
        """
        Change the active Laser Switch channel from the currently active one to the currently selected one
        """
        self.connection.eDigitalOut(0, 1, writeD = 1) 
        self.connection.eDigitalOut(0, 0, writeD = 1) 
        self.connection.eDigitalOut(0, 1, writeD = 1)
        sleep(RELAY_SLEEP)
        
    def get_selected_channel(self):
        """
        Poll the Laser Switch for the current selected channel, i.e. the one which will become "active" with the next "execute" command

        :returns: selected channel
        :type selected channel: int
        """
        return translate_bits_big_endian(self.connection.eDigitalIn(2),
                                         self.connection.eDigitalIn(3),
                                         self.connection.eDigitalIn(4))

    def get_active_channel(self):
        """
        Poll the Laser Switch for the current active channel, i.e. corresponding to the currently operating laser head

        :returns: active channel
        :type active channel: int

		:raises: :class:`.LaserSwitchHWError` if the command is unsuccessful
        """
        channel = translate_bits_big_endian(self.connection.eDigitalIn(5),
                                            self.connection.eDigitalIn(6),
                                            self.connection.eDigitalIn(7))
        if not channel in xrange(6):
            raise LaserSwitchHWError("Laser Switch returned unphysical active channel number!  It should be between 0 and 5 inclusive.")
        return channel

    def set_active_channel(self, channel):
        """
        Set the active Laser Switch channel - must be between 0 and 5 inclusive
        
        :param channel: requested active channel

        :raises: :class:`.LaserSwitchLogicError` if the requested active channel number is unphysical
        """
        if not channel in xrange(6):
            raise LaserSwitchLogicError("Cannot set selected Laser Switch channel to {0} - must be between 0 and 5 inclusive.".format(channel))
        while(channel != self.get_selected_channel()):
            self.selected_channel_up()
        self.execute()
    
    def current_state(self):
        """
        Return a formatted string with the current hardware settings
        """
        return """Active channel : {0}
Selected channel : {1}
""".format(get_active_channel(), get_selected_channel())
