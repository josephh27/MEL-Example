import socket

# Create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 12345))  # Connect to the server

# Send a message to the server
message = "Hello, Server! This is the client."
client_socket.send(message.encode())

# Receive response from server
response = client_socket.recv(1024).decode()
print(f"Received from server: {response}")

# Close socket
client_socket.close()
