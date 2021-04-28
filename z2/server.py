from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import sys
# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(('127.0.0.1', 1234),requestHandler=RequestHandler)
server.register_introspection_functions()

# Register a function under a different name
def adder_function(y):
    return [y[0]+y[1]]
def conv_function(params):
 for c in params[0]:
	 yolo = '{:x}'.format(ord(c))
	 sys.stdout.write(yolo)
 sys.stdout.write('\n')
 return params
server.register_function(adder_function, 'add')
server.register_function(conv_function, 'conv')


# Run the server's main loop
server.serve_forever()
