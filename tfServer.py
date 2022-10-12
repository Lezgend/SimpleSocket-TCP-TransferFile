import socket, sys              # Import socket module.

# ============================================================================

port = 60000                    # Reserve a port for your service.
host = socket.gethostname()     # Get local machine name.

socketObj = socket.socket()     # Create a socket object.
socketObj.bind((host, port))    # Bind to the port.
socketObj.listen(5)             # Now wait for client connection.
print ("Server Listening....")

# ============================================================================

try:
    while True:
        connection, addr = socketObj.accept()     # Establish connectionection with client. 
        print ("Got connection from", addr)
        data = connection.recv(1024)
        print("Server received request file transfer of",(data))

        filename=data.decode()
        f = open(filename,'rb')
        l = f.read(1024)
        while (l):
            connection.send(l)
            l = f.read(1024)
        f.close()
        print("Done Sending")
        connection.close()

except KeyboardInterrupt:
    print("Bye!")
    sys.exit()

# ============================================================================
