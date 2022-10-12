import socket                   # Import socket module.

# ============================================================================

s = socket.socket()             # Create a socket object.
host = socket.gethostname()     # Get local machine name.
port = 60000                    # Reserve a port for your service.

s.connect((host, port))
fileNeeded = input("What File do you need, please enter the name: ")
s.send(fileNeeded.encode())

fileToBeSaved = input("Enter file name to save requested file: ")

# ============================================================================

with open(fileToBeSaved, 'wb') as f:
    print("File was opened")
    while True:
        print("Receiving Data...")
        data = s.recv(1024)
        #print(data)
        if not data:
            break
        # Write data to a file
        f.write(data)

f.close()
print("Successfully got the file!")
s.close()
print("Connection Closed!")

# ============================================================================
