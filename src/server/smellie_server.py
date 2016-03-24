from SimpleXMLRPCServer import SimpleXMLRPCServer
from exception_handler import str_wrap_exceptions
from fake_function import test

REGISTERED_FUNCTIONS = [test]

class SmellieServer:
    def __init__(self, port):
        '''
         XML-RPC Protocol server hosted on the SNODROP machine on port 5020
        '''
        self.server = SimpleXMLRPCServer(("0.0.0.0", port), 
                                         allow_none = True)
        self.register()

    def serve_forever(self):
        self.server.serve_forever()

    def register(self):
        # wrap all the functions available to redirect exceptions to server
        for function in REGISTERED_FUNCTIONS:
            self.server.register_function(str_wrap_exceptions(function))
