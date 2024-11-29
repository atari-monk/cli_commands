# Mind sim

Creating a basic artificial "mind" in a CLI app is a fascinating idea! We can create a script that simulates a simple information-processing system. For now, we can limit the complexity while giving it perception (input processing), memory (storing data), and reaction (output generation). Building a model or decision-making process can be added later, but let's start small and scalable.

Here’s how we can break it down into manageable steps:

1. **Perception** (Input):

    - This could be simple text input from the user or data passed to the system.
    - We could define various "perceptions" or inputs like sensory information, questions, or requests.

2. **Memory** (Storing data):

    - Store past perceptions or inputs and perhaps some derived data like responses, decisions, or any internal model (a very basic one for now, like keywords and associations).
    - Memory could be stored as key-value pairs in a dictionary.

3. **Reaction** (Output):

    - After processing the input, the system generates a response. This could be based on stored memories or some simple pattern recognition.
    - Reactions could be random or based on defined rules, like echoing back perceived data, reacting to keywords, or even building simple models or responses over time.

4. **Model-building** (Optional for now):
    - Start with a simple structure like categorizing information or associating certain inputs with certain outputs.
    - We could introduce a basic associative memory model (a dictionary or a simple decision tree).

### Basic CLI Artifical Mind: Initial Script

Here's a Python script to demonstrate a simple CLI "mind" with perception, memory, and reaction:

```python
import random

class ArtificialMind:
    def __init__(self):
        self.memory = {}  # Memory storage
        self.model = {}   # A simple model to map input to reactions

    def perceive(self, input_data):
        """Simulate perception by processing input."""
        print(f"Perceived: {input_data}")
        self.process_memory(input_data)

    def process_memory(self, input_data):
        """Store input in memory, process it to create model."""
        if input_data not in self.memory:
            self.memory[input_data] = 1
        else:
            self.memory[input_data] += 1

        self.create_model(input_data)

    def create_model(self, input_data):
        """Basic model-building: Count occurrences and map inputs to reactions."""
        if self.memory[input_data] > 3:
            self.model[input_data] = "I've seen this before, let's focus on it!"
        else:
            self.model[input_data] = "This is new, let's remember it!"

    def react(self, input_data):
        """Generate reaction based on the model and memory."""
        reaction = self.model.get(input_data, "I don't understand that.")
        print(f"Reaction: {reaction}")

    def think(self, input_data):
        """Process input and generate a reaction."""
        self.perceive(input_data)
        self.react(input_data)

    def show_memory(self):
        """Display stored memory."""
        print("\nMemory:")
        for item, count in self.memory.items():
            print(f"{item}: {count} times")

if __name__ == "__main__":
    mind = ArtificialMind()

    print("Welcome to the artificial mind! Start interacting:")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "exit":
            break

        mind.think(user_input)
        mind.show_memory()
```

### Breakdown of the Script:

1. **ArtificialMind class**:

    - `perceive`: Takes input and simulates the perception process, simply prints what was perceived.
    - `process_memory`: Stores the input in memory (a dictionary) and tracks the frequency of perceptions.
    - `create_model`: Based on memory, builds a simple model that associates perceived inputs with a reaction.
    - `react`: The system generates a reaction based on its model. If it has seen the input before, it will react differently than to a new input.
    - `think`: Combines the perception, memory processing, and reaction into a single thought process.
    - `show_memory`: Shows stored memory, including the frequency of perceptions.

2. **Interaction**:
    - The user interacts by typing inputs. The system will process them and show reactions.
    - The system builds its memory and model incrementally.
    - Typing `exit` ends the interaction.

### Enhancing the Model:

-   **Perception** can be more sophisticated (e.g., text analysis, recognizing patterns in input).
-   **Memory** can be more complex (e.g., associating different perceptions or inputs with different categories or concepts).
-   **Reaction** can evolve with better decision-making models (e.g., using basic rule-based logic or even machine learning for more complex patterns).

For now, the script is simple and shows the basic flow. If you want to go further, you could add features like:

-   **Learning**: The system could track previous conversations or build a more complex association.
-   **Decision-making**: It could start reacting based on long-term goals (e.g., pursuing a certain outcome in the conversation).
-   **Improved Model**: Introduce a more sophisticated approach for reacting based on more complex stored data (e.g., past conversations, sentiment).

This script provides a starting point for building an artificial mind. How complex the mind becomes depends on the steps you choose to add next!
