import socket

class ServerConnection:
    def __init__(self, host: str, port: int):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)

    def accept_connection(self):
        client_socket, client_address = self.server_socket.accept()
        return client_socket, client_address

    def send_message(self, client_socket, message: str):
        client_socket.sendall(message.encode())

    def receive_message(self, client_socket):
        return client_socket.recv(1024).decode()

    def close_connection(self, client_socket):
        client_socket.close()
