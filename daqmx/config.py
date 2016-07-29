import sys
import platform
from smellie_config import FILE_LOC_WINXP, FILE_LOC_WIN7_64BIT, FILE_LOC_LINUX, LIB_NAME_WIN, LIB_NAME_LINUX

dot_h_file = FILE_LOC_WIN7_64BIT
lib_name = LIB_NAME_WIN

if sys.platform.startswith('win'):
    dot_h_file = FILE_LOC_WINXP

    if platform.release() == '7' and platform.architecture()[0] == '64bit':
        dot_h_file = FILE_LOC_WIN7_64BIT

    lib_name = LIB_NAME_WIN

elif sys.platform.startswith('linux'):
    dot_h_file = FILE_LOC_LINUX
    lib_name = LIB_NAME_LINUX

else:
    raise NotImplementedError, "Location of niDAQmx library and include file unknown on %s - if you find out, please let the PyDAQmx project know" % (sys.platform)
