from smellie.smellie_controller import SmellieController
from smellie_server import SmellieServer
from SimpleXMLRPCServer import SimpleXMLRPCServer
from config import PORT

server = SmellieServer(("0.0.0.0", PORT))
try:
    with SmellieController() as controller:
        server.register_instance(controller)    
        server.serve_forever()

except KeyboardInterrupt:
    print "Server terminated by keyboard interrupt"
