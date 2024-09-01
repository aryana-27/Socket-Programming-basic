import socket  
PORT = 8080  # Define the port number 

# Create a new socket object for the client
# AF_INET indicates IPv4, and SOCK_STREAM indicates TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', PORT)) # Connect the client to the server at '127.0.0.1' localhost
message = 'Hello from the client' # the message that the client will send to the server

# Send the message to the server
# The message is encoded to bytes because the socket expects bytes data
client.sendall(message.encode())

data = client.recv(1024) # recv is data recieved which can read 1024 bytes

# Print the server's response after decoding it from bytes to a string
print('Server Response:', data.decode())

# Close the connection to the server
client.close()
