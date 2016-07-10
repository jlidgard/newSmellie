"""
This module is a direct port of the C-API contained in:
     NIDAQmx.h, nicaiu.dll
provided by National Instruments.
The header is parsed, and ctypes is used to wrap each of the functions,
leaving the same signature function names.
Non-zero error codes are automatically translated to error strings and 
thrown as DAQError
"""
