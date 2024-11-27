# Argparse in Loop

## Base class

Here's a refactored solution where I provide a base class for creating CLI commands using `argparse`. This class is reusable and designed to run in a `while` loop without breaking. It allows you to define custom commands for your CLI easily by extending or composing it.

### Implementation

```python
import argparse


class BaseCLICommand:
    """
    Base class for defining CLI commands using argparse.
    Designed to be extended for custom commands in a CLI loop.
    """
    def __init__(self, prog: str, description: str):
        self.parser = argparse.ArgumentParser(
            prog=prog,
            description=description,
            add_help=False
        )
        self.parser.add_argument('-h', '--help', action='store_true', help='Show this help message and exit')

    def parse_and_execute(self, input_args: str):
        """
        Parses the input arguments and executes the corresponding action.
        :param input_args: String of command-line arguments.
        """
        args_list = input_args.split()
        try:
            # Parse arguments
            parsed_args = self.parser.parse_args(args_list)

            # Display help if requested
            if parsed_args.help:
                self.parser.print_help()
                return

            # Execute the command logic (to be overridden by subclasses or external logic)
            self.execute(parsed_args)

        except SystemExit:
            # Catch SystemExit to prevent breaking the loop
            pass

    def execute(self, parsed_args):
        """
        Placeholder for command execution logic.
        Override this in subclasses or inject logic through composition.
        """
        print("Executing base command with:", parsed_args)


# Example of a custom command using inheritance
class MyCustomCommand(BaseCLICommand):
    def __init__(self):
        super().__init__(prog="my_command", description="A custom command example")
        self.parser.add_argument('--name', type=str, help="Your name")
        self.parser.add_argument('--age', type=int, help="Your age")

    def execute(self, parsed_args):
        # Custom execution logic
        print(f"Hello, {parsed_args.name or 'stranger'}!")
        if parsed_args.age:
            print(f"You are {parsed_args.age} years old.")


# CLI Loop Example
def cli_loop():
    command = MyCustomCommand()
    print("Type 'exit' to quit the CLI.")

    while True:
        user_input = input("Enter command: ").strip()
        if user_input.lower() == "exit":
            print("Exiting CLI. Goodbye!")
            break
        command.parse_and_execute(user_input)


if __name__ == "__main__":
    cli_loop()
```

### Features

1. **Base Class (`BaseCLICommand`)**:

    - Initializes an `argparse.ArgumentParser` with `prog` and `description`.
    - Handles `--help` or `-h` to show help without breaking the loop.

2. **Extensibility**:

    - Extend `BaseCLICommand` and override the `execute` method to define custom logic.
    - Add arguments specific to the custom command in the subclass constructor.

3. **CLI Loop**:
    - Works seamlessly in a `while` loop.
    - Gracefully handles invalid inputs and `--help`.

### Example Interaction

```plaintext
Type 'exit' to quit the CLI.
Enter command: --help
usage: my_command [-h] [--name NAME] [--age AGE]

A custom command example

optional arguments:
  -h, --help     Show this help message and exit
  --name NAME    Your name
  --age AGE      Your age

Enter command: --name Alice --age 30
Hello, Alice!
You are 30 years old.
Enter command: exit
Exiting CLI. Goodbye!
```

This pattern ensures flexibility, reusability, and a clean design for building CLI tools.

## Here's an example of using **composition** instead of inheritance to define commands for a CLI loop. This approach allows you to define commands as separate components, making it easy to mix and match commands without tightly coupling them to the base class.

---

### Implementation with Composition

```python
import argparse


class CLICommand:
    """
    Command wrapper for using argparse with a CLI tool via composition.
    """
    def __init__(self, prog: str, description: str):
        self.parser = argparse.ArgumentParser(
            prog=prog,
            description=description,
            add_help=False
        )
        self.parser.add_argument('-h', '--help', action='store_true', help='Show this help message and exit')
        self.execution_callback = None  # Callback to define custom command logic

    def set_execution_callback(self, callback):
        """
        Sets the callback function for executing the command's logic.
        :param callback: Callable that takes parsed arguments.
        """
        self.execution_callback = callback

    def parse_and_execute(self, input_args: str):
        """
        Parses the input arguments and executes the callback if defined.
        :param input_args: String of command-line arguments.
        """
        args_list = input_args.split()
        try:
            parsed_args = self.parser.parse_args(args_list)

            # Display help if requested
            if parsed_args.help:
                self.parser.print_help()
                return

            # Call the execution callback
            if self.execution_callback:
                self.execution_callback(parsed_args)
            else:
                print("No execution logic defined for this command.")

        except SystemExit:
            # Prevent the loop from breaking on invalid inputs
            pass


# Define commands as standalone objects
def create_greet_command():
    command = CLICommand(prog="greet", description="Greet the user with a message")
    command.parser.add_argument('--name', type=str, required=True, help="Your name")
    command.parser.add_argument('--greeting', type=str, default="Hello", help="Greeting message")

    def execute_greet(parsed_args):
        print(f"{parsed_args.greeting}, {parsed_args.name}!")

    command.set_execution_callback(execute_greet)
    return command


def create_math_command():
    command = CLICommand(prog="math", description="Perform basic math operations")
    command.parser.add_argument('--operation', type=str, choices=['add', 'subtract'], required=True, help="Operation to perform")
    command.parser.add_argument('--a', type=float, required=True, help="First number")
    command.parser.add_argument('--b', type=float, required=True, help="Second number")

    def execute_math(parsed_args):
        if parsed_args.operation == "add":
            result = parsed_args.a + parsed_args.b
            print(f"The result of addition: {result}")
        elif parsed_args.operation == "subtract":
            result = parsed_args.a - parsed_args.b
            print(f"The result of subtraction: {result}")

    command.set_execution_callback(execute_math)
    return command


# CLI Loop Example
def cli_loop():
    # Register commands
    commands = {
        "greet": create_greet_command(),
        "math": create_math_command(),
    }

    print("Type 'exit' to quit the CLI. Available commands: greet, math")

    while True:
        user_input = input("Enter command: ").strip()
        if user_input.lower() == "exit":
            print("Exiting CLI. Goodbye!")
            break

        # Parse the command name and arguments
        if not user_input:
            continue
        cmd_name, *cmd_args = user_input.split(maxsplit=1)
        cmd_args = cmd_args[0] if cmd_args else ""

        # Execute the corresponding command
        if cmd_name in commands:
            commands[cmd_name].parse_and_execute(cmd_args)
        else:
            print(f"Unknown command: {cmd_name}. Try 'greet' or 'math'.")


if __name__ == "__main__":
    cli_loop()
```

---

### Features of Composition

1. **Command Objects**:

    - Each command is created as an instance of `CLICommand`.
    - A command is initialized with its own arguments and logic.

2. **Execution Callback**:

    - The `set_execution_callback` method allows you to assign custom logic to each command without subclassing.

3. **Command Registration**:
    - Commands are stored in a dictionary, where the key is the command name, and the value is the corresponding `CLICommand` object.

---

### Example Interaction

```plaintext
Type 'exit' to quit the CLI. Available commands: greet, math
Enter command: greet --help
usage: greet [-h] --name NAME [--greeting GREETING]

Greet the user with a message

optional arguments:
  -h, --help          Show this help message and exit
  --name NAME         Your name
  --greeting GREETING Greeting message

Enter command: greet --name Alice --greeting Hi
Hi, Alice!
Enter command: math --operation add --a 5 --b 10
The result of addition: 15.0
Enter command: math --operation subtract --a 10 --b 3
The result of subtraction: 7.0
Enter command: exit
Exiting CLI. Goodbye!
```

---

### Benefits of Composition

-   **Flexibility**: You can dynamically create and assign commands without tightly coupling them to a base class.
-   **Reusability**: Commands are modular and can be reused in different CLI tools.
-   **Ease of Extension**: Adding new commands is straightforward and doesn't require inheritance or class modification.
