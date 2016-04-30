import sys
import platform
from config import FILE_LOC_WINXP, FILE_LOC_WIN7_64BIT, FILE_LOC_LINUX, LIB_NAME_WIN, LIB_NAME_LINUX

if sys.platform.startswith('win'):
    # This is the full path of the NIDAQmx.h file if it is installed on a Windows XP machine, which (as of 29/04/16) is also the default location
    dot_h_file = FILE_LOC_WINXP

    # This is the full path of the NIDAQmx.h file if it is installed on a 64-bit Windows 7 machine, which (as of 29/04/16) is also the default location
    if platform.release() == '7' and platform.architecture()[0] == '64bit':
        dot_h_file = FILE_LOC_WIN7_64BIT

    # The name and path of the library (the default name is `nicaiu`)
    lib_name = LIB_NAME_WIN

elif sys.platform.startswith('linux'):
    # This is the full paths and name of the NIDAQmx.h file and library if they are installed on a Linux machine, which (as of 29/04/16) are also the default location and name
    # To find the file, use the command: `find_library('nidaqmx')`
    dot_h_file = FILE_LOC_LINUX
    lib_name = LIB_NAME_LINUX

else:
    raise NotImplementedError, "Location of niDAQmx library and include file unknown on %s - if you find out, please let the PyDAQmx project know" % (sys.platform)
