COM_CHANNEL = 1
RELAY_SLEEP = 30
from time import sleep

def invert(bit):
    if bit in (0, 1):
        return (not bit)
    raise TypeError("Invert bit - not a boolean!")

class LaserSwitchLogicError(Exception):
    pass

class LaserSwitchHWError(Exception):
    pass


class LaserSwitch(object):
    def __init__(channel):
        self.com_channel = CHANNEL
        self.connection = U12()

    def __enter__(self):
        pass

    def __exit__(self):
        self.go_safe()

    def channel_up(self):
        orig = get_selected_channel()
        self.connection.eDigitalOut(self.com_channel, 1, writeD = 1) 
        self.connection.eDigitalOut(self.com_channel, 0, writeD = 1) 
        self.connection.eDigitalOut(self.com_channel, 1, writeD = 1) 
        if not (1 + orig = get_selected_channel()):
            raise LaserSwitchHWError("channel_up call failed!")

    def execute(self):
        self.connection.eDigitalOut(0, 1, writeD = 1) 
        self.connection.eDigitalOut(0, 0, writeD = 1) 
        self.connection.eDigitalOut(0, 1, writeD = 1)
        sleep(RELAY_SLEEP)
        
    def get_selected_channel(self):
        channel = invert(self.connection.eDigitalIn(5)) + (2.0 * invert(self.connection.eDigitalIn(6))) + (4.0 * invert(self.connection.eDigitalIn(7)))
        return int(channel)

    def get_active_channel(self):
          channel = invert(d.eDigitalIn(5)) + (2.0 * invert(d.eDigitalIn(6))) + (4.0 * invert(d.eDigitalIn(7)))
          if not channel in xrange(6):
              raise LaserSwitchHWError("Laser switch returned unphysical channel number!")
          return int(channel)

    def set_channel(self, channel):
        if not channel in xrange(6):
            raise LaserSwitchLogicError("Can't set display channel to {0}, must be 0-5 inclusive".format(channel))
        
        while(channel != self.get_channel()):
            self.channel_up()
            
        self.execute()

    def go_safe(self):
        self.set_channel(0)
