import socket

PORT = 8080  # Port number which will listen for incoming connections
# AF_INET indicates IPv4, and SOCK_STREAM indicates TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creates a new socket object
server.bind(('127.0.0.1', PORT))  # bind function binds the sicket with address number and port number
# # 127.0.0.1 is the localhost address which means the server will listen
server.listen(50)  ## only 50 queue connects allowed else it will reject them

print("Server Listening on Port:", PORT)

while True:
    conn, addr = server.accept()  # here when client connects , new socket object conn and addr being address of client
    print('Connected to', addr)

    data = conn.recv(1024)  # recv is data recieved which can read 1024 bytes
    print(f"Client Message: {data}")  # Prints the raw bytes received from the client
    conn.sendall(b'Server Echo: ' + data)  # sendall sends the data back to the client

    conn.close()  # Closes the connection

