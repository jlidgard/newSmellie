'''
This module wraps manufacturer provided functions contained in a dll
for use in the program. The 
'''
from config import SEPIA_DLL_PATH
import ctypes
import os


class SepiaHW(object):
    def __init__(self):
        # check that the dll exists
        if not os.path.exists(SEPIA_DLL_PATH):
            raise Exception
        
        # open the dll
        self.dll = ctypes.OleDLL(dll_path)
        
    def __enter__(self):
        
        
        

