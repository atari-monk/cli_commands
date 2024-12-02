# write.py

import os
import pyperclip
from doc_site.cli_tool import CLITool
from doc_site.path_tool import PathTool
from log_task.log_setup import getConsoleFileLoggerConfig, getConsoleLoggerConfig
from shared.cli_command import CLICommand
from cli_logger.logger import setup_logger
import os
import pyperclip
from log_task.log_setup import getConsoleFileLoggerConfig, getConsoleLoggerConfig
from shared.cli_command import CLICommand
from cli_logger.logger import setup_logger
from shared.command import Command
from keyval_storage.config_and_key_value_storage_data_model import ConfigAndKeyValueStorageDataModel
from shared.constants import APP_NAME

class WriteCommand:
    def __init__(self):
        data_model = ConfigAndKeyValueStorageDataModel(APP_NAME)
        data_storage = data_model.getKeyValueStorage_LoadUsingConfig()
        self.data_folder = data_storage.get('doc_site_data_folder')

        name = Command.doc_site_write.cmd_name

        console_config = getConsoleLoggerConfig()
        self.console_logger = setup_logger(f"{name}_console", console_config)

        console_file_config = getConsoleFileLoggerConfig(name)
        self.file_logger = setup_logger(f"{name}_file", console_file_config)

        self.cli_command = CLICommand(
            prog=name,
            description=Command.doc_site_write.desc
        )

        self.cli_command.parser.add_argument('--file', type=str, help="Path to the markdown file to save input.")

        self.cli_command.set_execution_callback(self._execute_command)

    def run(self, input_args: str):
        self.cli_command.parse_and_execute(input_args)

    def _execute_command(self, parsed_args):
        self.console_logger.info(f"Data folder: {self.data_folder}")

        category = CLITool.generate_menu_and_select(PathTool.list_first_level_folders(self.data_folder))
        self.console_logger.info(f"Category: {category}")    

        markdown_data = []
        file_path = parsed_args.file or input("Enter the markdown file path: ").strip()

        if not os.path.exists(file_path):
            print(f"File {file_path} does not exist. Creating a new file.")
            open(file_path, 'w').close()

        print("Starting to collect markdown from clipboard.")
        print("Step 1: Copy a part of your markdown content.")
        print("Step 2: Press Enter to store that content.")
        print("Step 3: Type '--end' to finish when you're done.")

        while True:
            user_input = input("\nCopy a part of your markdown content and press Enter to store it (or type '--end' to stop): ").strip()

            if user_input.lower() == '--end':
                break

            clipboard_content = pyperclip.paste().strip()

            if clipboard_content:
                markdown_data.append(clipboard_content)
                print(f"Collected clipboard content: {clipboard_content}")
            else:
                print("No clipboard content found. Please copy some markdown text to clipboard.")

        with open(file_path, 'a') as f:
            f.write("\n\n".join(markdown_data) + "\n")

        self.console_logger.info(f"Collected markdown data: {markdown_data}")
        self.file_logger.info(f"Collected markdown data appended to {file_path}")

        print(f"\nMarkdown has been successfully appended to {file_path}!")
