import os
import pyperclip
import tempfile
import subprocess
from doc_site.cli_tool import CLITool
from doc_site.path_tool import PathTool
from shared.log_setup import getConsoleFileLoggerConfig, getConsoleLoggerConfig
from shared.cli_command import CLICommand
from cli_logger.logger import setup_logger
from shared.command import Command
from keyval_storage.config_and_key_value_storage_data_model import ConfigAndKeyValueStorageDataModel
from shared.constants import APP_NAME
from shared.storage_key import StorageKey

class WriteCommand:
    def __init__(self):
        data_storage = ConfigAndKeyValueStorageDataModel(APP_NAME).getKeyValueStorage_LoadUsingConfig()
        self.data_folder = data_storage.get(StorageKey.DOC_SITE_DATA_FOLDER.value)

        name = Command.doc_site_write.cmd_name
        self.cliLogger = setup_logger(f"{name}_console", getConsoleLoggerConfig())
        self.cliFileLogger = setup_logger(f"{name}_file", getConsoleFileLoggerConfig(name))

        self.cli_command = CLICommand(
            prog=name,
            description=Command.doc_site_write.desc
        )

        self.cli_command.set_execution_callback(self._execute_command)

    def run(self, input_args: str):
        self.cli_command.parse_and_execute(input_args)

    def _execute_command(self, _):
        self.cliLogger.info(f"Data folder: {self.data_folder}")

        category = CLITool.generate_menu_and_select(PathTool.list_first_level_folders(self.data_folder))
        self.cliLogger.info(f"Category: {category}")    

        name = input("Provide file name: ")

        markdown_data = []
        print(f"data_folder: {self.data_folder}, category: {category}, name: {name}")
        file_path = os.path.join(self.data_folder, category, f"{name}.md")

        if not os.path.exists(file_path):
            print(f"Creating a new file {file_path}.")
            open(file_path, 'w').close()

        print("Starting to collect markdown from clipboard.")
        print("Step 1: Copy a part of your markdown content.")
        print("Step 2: Press Enter to edit the content.")
        print("Step 3: Type 'e' to finish when you're done.")

        while True:
            user_input = input("\nCopy a part of your markdown content and press Enter to edit it (or type 'e' to stop): ").strip()

            if user_input.lower() == 'e':
                break

            clipboard_content = pyperclip.paste().strip()

            if clipboard_content:
                edited_content = self._edit_content(clipboard_content)
                markdown_data.append(edited_content)
                print(f"Collected and edited content: {edited_content}")
            else:
                print("No clipboard content found. Please copy some markdown text to clipboard.")

        with open(file_path, 'a') as f:
            f.write("\n\n".join(markdown_data) + "\n")

        self.cliLogger.info(f"Collected markdown data: {markdown_data}")
        self.cliFileLogger.info(f"Collected markdown data appended to {file_path}")

        print(f"\nMarkdown has been successfully appended to {file_path}!")

    def _edit_content(self, initial_content):
        with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.md') as temp_file:
            temp_file.write(initial_content)
            temp_file.flush()
            temp_name = temp_file.name

        editor = os.environ.get('EDITOR', 'nano' if os.name != 'nt' else 'notepad')
        subprocess.call([editor, temp_name])

        with open(temp_name, 'r') as temp_file:
            edited_content = temp_file.read().strip()

        os.remove(temp_name)
        return edited_content
