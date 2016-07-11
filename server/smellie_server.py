"""
The SMELLIE server is a python SimpleXMLRPCServer but wrapped so that each method of the exposed instance is wrapped by 
:func:`exception_handler.str_wrap_exceptions` and :func:`dummy_mode.has_dummy_mode`, so that any exceptions thrown are translated as strings over the server, and to allow 
running in dummy mode - where each function call just results in a signature print, and no logic.
"""

from SimpleXMLRPCServer import SimpleXMLRPCServer
from exception_handler import str_wrap_exceptions
from dummy_mode import has_dummy_mode
from inspect import getmembers, isroutine

def wrap_all_methods(instance, *wrappers):
    '''
    Wrap every member function of instance with each wrapper in turn. 
    Used to apply str_wrap_exceptions and dummy mode
    to the smellie controller instance

    :param instance: the object to wrap

    :param wrappers: tuple of function wrappers
    '''
    for wrapper in wrappers:
        for name, method in getmembers(instance, isroutine):
            setattr(instance, name, wrapper(method))
    return instance

class SmellieServer:
    '''
    XML-RPC Protocol server that exposes a SmellieController to external 
    calls
    '''
    def __init__(self, port, instance):
        '''
        Initialise the server on port and register functions
        Calls: :func:`register <smellie_server.SmellieServer.register>

        :param port: port
        
        :param instance: controller object to expose to the server
        '''
        
        self.server = SimpleXMLRPCServer(("0.0.0.0", port))
        self.register(instance)

    def serve_forever(self):
        '''
        Listen indefinitely for function calls to exectute
        '''
        self.server.serve_forever()


    def register(self, instance):
        '''
        Register methods of instance with internal server, after wrapping with
        :func:`exception_handler.str_wrap_exceptions` and :func:`dummy_mode.has_dummy_mode`
        
        :param instance: controller object to expose to the server
        '''
        self.controller = instance
        self.server.register_instance(wrap_all_methods(self.controller, str_wrap_exceptions, has_dummy_mode))
        self.server.register_introspection_functions()
        
