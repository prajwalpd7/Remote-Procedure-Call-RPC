from xmlrpc.server import SimpleXMLRPCServer
import os

#define server and create it
server = SimpleXMLRPCServer(('localhost', 3000), logRequests=True)

# define any functions we want available
def list_directory(dir):
     return os.listdir(dir)
    
# Register there funtions with the server instance
server.register_function(list_directory)

# if this module is run from the command line as opposed to being imported
# then go into server_forever mode

if __name__ == '__main__':
    try:
        print('Serving...')
        server.serve_forever()
    except KeyboardInterrupt:
        print('Exiting')
