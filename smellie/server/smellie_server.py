from SimpleXMLRPCServer import SimpleXMLRPCServer
from exception_handler import str_wrap_exceptions
from dummy_mode import has_dummy_mode
from inspect import getmembers, isroutine

def wrap_all_methods(instance, *wrappers):
    '''
    Wrap every memeber function of instance with wrapper. Used to apply str_wrap_exceptions and dummy mode
    to the smellie controller instance
    '''
    for wrapper in wrappers:
        for name, method in getmembers(instance, isroutine):
            setattr(instance, name, wrapper(method))
    return instance

class SmellieServer:
    """
    XML-RPC Protocol server that exposes a list of functions to external 
    calls
    """
    def __init__(self, port, instance):
        """
        Initialise the server on port and register functions
        Calls: :func:`register <smellie_server.SmellieServer.register>

        :param port: port
        """
        
        self.server = SimpleXMLRPCServer(("0.0.0.0", port))
        self.register(instance)

    def serve_forever(self):
        """
        Listen indefinitely for function calls to exectute
        """
        self.server.serve_forever()


    def register(self, instance):
        """
        Register methods with internal server, after wrapping with 
        :func:`exception_handler.str_wrap_exceptions`
        """
        self.controller = instance
        self.server.register_instance(wrap_all_methods(self.controller, str_wrap_exceptions, has_dummy_mode))
        self.server.register_introspection_functions()
        
