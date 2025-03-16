# Simple Python Socket Communication

This repository contains a basic example of a client-server communication setup using Python's `socket` module.

## How It Works

1. The `server.py` script creates a socket server that listens for incoming connections on `localhost:12345`.
2. The `client.py` script connects to the server and sends a message.
3. The server receives the message, prints it, and sends a response.
4. The client receives and prints the response before closing the connection.

## Running the Example

### Step 1: Start the Server
Run the following command in a terminal:
```bash
python server.py
