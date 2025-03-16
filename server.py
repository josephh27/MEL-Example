import socket

# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))  # Bind to localhost on port 12345
server_socket.listen(1)  # Listen for incoming connections

print("Server is waiting for a connection...")

# Accept connection
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

# Receive data from the client
data = client_socket.recv(1024).decode()
print(f"Received from client: {data}")

# Send a response
response = "Hello, Client! Message received."
client_socket.send(response.encode())

# Close sockets
client_socket.close()
server_socket.close()
