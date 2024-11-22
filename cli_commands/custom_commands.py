# custom_commands.py

def load():
    print("custom_commands.load() called")

    def greet():
        print("Hello from the custom commands package!")

    return {
        "greet": greet,
    }
