from smellie_config import LOGGER_SERVER, LOGGER_PORT, LOGGER_CONNECT_TO_SERVER
from snotdaq import Logger
import time,datetime 

"""
Interface with the SNOTDAQ Logger
"""

class SMELLIELogger(object):

    the_logger = None  
    def __init__(self):
        raise "No you can't, use the class stuff"

    @classmethod
    def new_logger(cls, run_number = "-1"):
        """
        Create a new logger
        """
        cls.the_logger = Logger()
        
        if LOGGER_CONNECT_TO_SERVER:
           cls.connect()

        cls.the_logger.set_logfile('C:\SMELLIE\logs\smellie_logger_run{}_time{}.log'.format( run_number, datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S') ) )  #write local log 
  
    @classmethod    
    def connect(cls):
         cls.the_logger.connect('smellie',LOGGER_SERVER,LOGGER_PORT) #connect to logging server
   
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
        
SMELLIELogger.new_logger()