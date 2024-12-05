import os
from shared.cli_command import CLICommand
from shared.command import Command
from shared.constants import APP_NAME
from keyval_storage.config_and_key_value_storage_data_model import ConfigAndKeyValueStorageDataModel
from shared.storage_key import StorageKey

class ValidateCommand:
    def __init__(self):
        self.__data_storage = ConfigAndKeyValueStorageDataModel(APP_NAME).getKeyValueStorage_LoadUsingConfig()

        self.__cli_command = CLICommand(
            prog=Command.doc_site_validate.cmd_name,
            description=Command.doc_site_validate.desc
        )

        self.__cli_command.set_execution_callback(self._execute_command)

        self.ignored_folders = ['.git']
        self.ignored_files  = ['index.md']

    def run(self, input_args: str):
        self.__cli_command.parse_and_execute(input_args)

    def _execute_command(self, _):
        data = self.__data_storage.get(StorageKey.DOC_SITE_DATA_FOLDER.value)

        if not data: 
            print(f"Error: No record for key {StorageKey.DOC_SITE_DATA_FOLDER.value}.")
        else:
            self.validate_doc_site_structure(data)

    def _folder_exists(self,path):
        return os.path.exists(path)
        
    def _is_lower_case(self,name):
        return name == name.lower()
    
    def _contains_only_md_files(self,folder_path):
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isdir(item_path) or not item.endswith('.md'):
                return False
        return True

    def validate_doc_site_structure(self,path):
        if not self._folder_exists(path):
            print(f"Error: The folder '{path}' does not exist.")
            return False

        for folder in os.listdir(path):
            folder_path = os.path.join(path, folder)

            if folder in self.ignored_folders:
                continue

            if os.path.isdir(folder_path):
                if not self._is_lower_case(folder):
                    print(f"Error: Folder '{folder}' is not in lower case.")
                    return False

                if not self._contains_only_md_files(folder_path):
                    print(f"Error: Folder '{folder}' contains items that are not .md files or has nested folders.")
                    return False
            else:
                if folder in self.ignored_files:
                    continue

                if not folder.endswith('.md'):
                    print(f"Error: File '{folder}' is not a .md file.")
                    return False
                
        print("Validation passed!")
        return True
