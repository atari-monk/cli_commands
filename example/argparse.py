import argparse

def argparse_command(args):
    # Split the args string into a list
    args_list = args.split()
    
    # Create the argument parser with a custom program name
    parser = argparse.ArgumentParser(
        prog="argparse",  # Set the custom command name for usage
        description="Demonstrate argparse in a CLI tool",
        add_help=False
    )
    
    # Add arguments
    parser.add_argument('-h', '--help', action='store_true', help='Show this help message and exit')
    parser.add_argument('--name', type=str, help='Your name')
    parser.add_argument('--age', type=int, help='Your age')
    parser.add_argument('--greet', action='store_true', help='Print a greeting')
    
    try:
        # Parse arguments
        parsed_args = parser.parse_args(args_list)
        
        # Check for help flag
        if parsed_args.help:
            parser.print_help()
            return  # Exit gracefully after showing help

        # Handle other arguments
        if parsed_args.greet:
            if parsed_args.name and parsed_args.age is not None:
                print(f"Hello, {parsed_args.name}! You are {parsed_args.age} years old.")
            else:
                print("Error: Please provide both --name and --age to use the --greet option.")
        else:
            print("Run with --greet to see the greeting.")
    except SystemExit:
        # Catch argparse's SystemExit to prevent breaking the CLI loop
        pass  # Do nothing
