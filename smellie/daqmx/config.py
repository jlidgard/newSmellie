import sys
import platform

if sys.platform.startswith('win'):
    # This is the full path of the NIDAQmx.h file if it is installed on a Windows XP machine, which (as of 29/04/16) is also the default location
    dot_h_file =  r'C:\Program Files (x86)\National Instruments\NI-DAQ\DAQmx ANSI C Dev\include\NIDAQmx.h'

    # This is the full path of the NIDAQmx.h file if it is installed on a 64-bit Windows 7 machine, which (as of 29/04/16) is also the default location
    if platform.release() == '7' and platform.architecture()[0] == '64bit':
        dot_h_file = r'C:\Program Files (x86)\National Instruments\NI-DAQ\DAQmx ANSI C Dev\include\NIDAQmx.h'

    # The name and path of the library (the default name is `nicaiu`)
    lib_name = "nicaiu"

elif sys.platform.startswith('linux'):
    # This is the full paths and name of the NIDAQmx.h file and library if they are installed on a Linux machine, which (as of 29/04/16) are also the default location and name
    # To find the file, use the command: `find_library('nidaqmx')`
    dot_h_file = '/usr/local/natinst/nidaqmx/include/NIDAQmx.h'
    lib_name = 'libnidaqmx.so'

else:
    raise NotImplementedError, "Location of niDAQmx library and include file unknown on %s - if you find out, please let the PyDAQmx project know" % (sys.platform)
