from smellie_config import LOGGER_SERVER, LOGGER_PORT, LOGGER_CONNECT_TO_SERVER
from snotdaq import Logger
import time,datetime 

"""
Interface with the SNOTDAQ Logger
"""

class SMELLIEInterlockLoggerLogicError(Exception):
    """
    Thrown if an inconsistency is noticed *after* any hardware instruction is executed (i.e. a problem with the hardware itself)
    """
    pass

class SMELLIEInterlockLogger(object):

    the_logger = None  
    def __init__(self):
        raise SMELLIEInterlockLoggerLogicError("Do not initiate object. Use classes only.")

    @classmethod
    def new_logger(cls):
        """
        Create a new logger
        """
        cls.the_logger = Logger()

        if LOGGER_CONNECT_TO_SERVER:
           cls.connect()

        cls.the_logger.set_logfile('C:\SMELLIE\logs\smellie_interlock_logger_time{}.log'.format( datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S') ) )  #write local log 
  
    @classmethod    
    def connect(cls):
         cls.the_logger.connect('SMELLIE',LOGGER_SERVER,LOGGER_PORT) #connect to logging server
   
    @classmethod
    def debug(cls,*args, **kwargs):
        cls.the_logger.debug(*args, **kwargs)
        
    @classmethod
    def verbose(cls,*args, **kwargs):
        cls.the_logger.verbose(*args, **kwargs)
    
    @classmethod
    def notice(cls,*args, **kwargs):
        cls.the_logger.notice(*args, **kwargs)
    
    @classmethod
    def warn(cls,*args, **kwargs):
        cls.the_logger.warn(*args, **kwargs)
        
SMELLIEInterlockLogger.new_logger()