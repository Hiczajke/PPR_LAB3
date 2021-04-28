from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(('127.0.0.1', 12345),requestHandler=RequestHandler)
server.register_introspection_functions()

# Register a function under a different name
def adder_function(x, y):
    return x + y
server.register_function(adder_function, 'add')


# Run the server's main loop
server.serve_forever()
