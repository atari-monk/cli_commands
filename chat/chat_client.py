from chat.ClientConnection import ClientConnection
from message import Message
import threading

class ChatClient:
    def __init__(self, host: str, port: int, username: str):
        self.connection = ClientConnection(host, port)
        self.username = username

    def send_message(self, message: str):
        formatted_message = Message(self.username, message).format_message()
        self.connection.send_message(formatted_message)

    def receive_messages(self):
        while True:
            message = self.connection.receive_message()
            if message:
                print(message)

    def start(self):
        threading.Thread(target=self.receive_messages, daemon=True).start()
        while True:
            message = input("You: ")
            if message.lower() == "exit":
                self.connection.close_connection()
                break
            self.send_message(message)

if __name__ == "__main__":
    username = input("Enter your username: ")
    client = ChatClient("localhost", 12345, username)
    client.start()
