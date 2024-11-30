class Message:
    def __init__(self, sender: str, content: str):
        self.sender = sender
        self.content = content

    def format_message(self):
        return f"{self.sender}: {self.content}"
