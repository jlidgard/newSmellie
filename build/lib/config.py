# Dummy mode just prints the signature of calls to server functions
DUMMY_MODE = False

# SEPIA Laser Driver
SEPIA_DLL_PATH        = "C:\Users\LocalAdmin\Desktop\Pysepia\Sepia2_Lib.dll"
SEPIA_STR_BUFFER_SIZE = 128  # must be at minimum = 64 bytes
LASER_DRIVER_DEV_ID   = 0
LASER_DRIVER_SLOT_ID  = 200

# Smellie Controller Server
PORT = 5020

# Logging Server
LOGGER_PORT = 0

# Fibre Switch 
FIBRE_SWITCH_SERIAL_PORT = 0
FIBRE_SWITCH_BAUD_RATE   = 57600
FIBRE_SWITCH_WAIT_TIME   = 0.1  # in seconds

# Interlock
INTERLOCK_PORT      = 3  # = COM4
INTERLOCK_BAUD_RATE = 57600

# Laser Switch
RELAY_COM_CHANNEL = 1
RELAY_SLEEP       = 30  # in seconds
