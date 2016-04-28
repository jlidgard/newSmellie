from SimpleXMLRPCServer import SimpleXMLRPCServer
from exception_handler import str_wrap_exceptions

class SmellieServer:
    """
    XML-RPC Protocol server that exposes a list of functions to external 
    calls
    """
    def __init__(self, port):
        """
        Initialise the server on port and register functions
        Calls: :func:`register <smellie_server.SmellieServer.register>

        :param port: port
        """
        
        self.server = SimpleXMLRPCServer(("0.0.0.0", port))
        self.register()

    def serve_forever(self):
        """
        Listen indefinitely for function calls to exectute
        """
        self.server.serve_forever()

    def register(self):
        """
        Register methods with internal server, after wrapping with 
        :func:`exception_handler.str_wrap_exceptions`
        """
        # wrap all the functions available to redirect exceptions to server
        for function in REGISTERED_FUNCTIONS:
            self.server.register_function(str_wrap_exceptions(function))
