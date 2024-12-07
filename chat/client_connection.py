import socket

class ClientConnection:
    def __init__(self, host: str, port: int):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))

    def send_message(self, message: str):
        self.client_socket.sendall(message.encode())

    def receive_message(self):
        return self.client_socket.recv(1024).decode()

    def close_connection(self):
        self.client_socket.close()
