COM_CHANNEL = 1
RELAY_SLEEP = 30
from time import sleep

def invert(bit):
    if bit in (0, 1):
        return (not bit)
    raise TypeError("Invert bit - not a boolean!")

def translate_bits_big_endian(b1, b2, b3):
    return int("{2}{1}{0}".format(b1, b2, b3), 2)

class LaserSwitchLogicError(Exception):
    pass

class LaserSwitchHWError(Exception):
    pass

class LaserSwitch(object):
    def __init__(channel):
        self.com_channel = COM_CHANNEL
        self.connection = U12()

    def channel_up(self):
        orig = get_selected_channel()
        self.connection.eDigitalOut(self.com_channel, 1, writeD = 1) 
        self.connection.eDigitalOut(self.com_channel, 0, writeD = 1) 
        self.connection.eDigitalOut(self.com_channel, 1, writeD = 1) 
        if 1 + orig != get_selected_channel():
            raise LaserSwitchHWError("channel_up call failed!")

    def execute(self):
        self.connection.eDigitalOut(0, 1, writeD = 1) 
        self.connection.eDigitalOut(0, 0, writeD = 1) 
        self.connection.eDigitalOut(0, 1, writeD = 1)
        sleep(RELAY_SLEEP)
        
    def get_selected_channel(self):
        return translate_bits_big_endian(self.connection.eDigitalIn(2),
                                         self.connection.eDigitalIn(3),
                                         self.connection.eDigitalIn(4),
                                         )

    def get_active_channel(self):
        channel = translate_bits_big_endian(self.connection.eDigitalIn(5),
                                            self.connection.eDigitalIn(6),
                                            self.connection.eDigitalIn(7),
                                            )
        if not channel in xrange(6):
            raise LaserSwitchHWError("Laser switch returned unphysical channel number!")
        return channel

    def set_channel(self, channel):
        if not channel in xrange(6):
            raise LaserSwitchLogicError("Can't set display channel to {0}, must be 0-5 inclusive".format(channel))
        
        while(channel != self.get_channel()):
            self.channel_up()
            
        self.execute()

    def go_safe(self):
        self.set_channel(0)
    
    def current_state(self):
        return """Active Channel : {0}
Current Channel : {1}
""".format(self.get_active_channel(), self.get_selected_channel())
