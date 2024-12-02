class CLITool:
    @staticmethod
    def generate_menu_and_select(options: list[str]) -> str:
        if not options:
            raise ValueError("The options list is empty. Cannot generate a menu.")
        
        print("Please select an option from the menu:")
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")
        
        while True:
            try:
                choice = int(input("Enter the number of your choice: "))
                if 1 <= choice <= len(options):
                    return options[choice - 1]
                else:
                    print(f"Invalid choice. Please select a number between 1 and {len(options)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")
