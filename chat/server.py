from connection import ServerConnection
from message import Message
import threading

class ChatServer:
    def __init__(self, host: str, port: int):
        self.connection = ServerConnection(host, port)
        self.clients = []

    def broadcast_message(self, message: str):
        for client_socket in self.clients:
            self.connection.send_message(client_socket, message)

    def handle_client(self, client_socket, client_address):
        print(f"New connection from {client_address}")
        while True:
            try:
                message = self.connection.receive_message(client_socket)
                if message:
                    print(f"Message from {client_address}: {message}")
                    formatted_message = Message("Server", message).format_message()
                    self.broadcast_message(formatted_message)
                else:
                    break
            except:
                break

        self.connection.close_connection(client_socket)
        self.clients.remove(client_socket)
        print(f"Connection from {client_address} closed")

    def start(self):
        print("Server started, waiting for connections...")
        while True:
            client_socket, client_address = self.connection.accept_connection()
            self.clients.append(client_socket)
            threading.Thread(target=self.handle_client, args=(client_socket, client_address)).start()

if __name__ == "__main__":
    server = ChatServer("localhost", 12345)
    server.start()