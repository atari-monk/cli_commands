import os
from shared.cli_command import CLICommand
from shared.command import Command
from shared.constants import APP_NAME
from keyval_storage.config_and_key_value_storage_data_model import ConfigAndKeyValueStorageDataModel
from shared.storage_key import StorageKey

class IndexCommand:
    def __init__(self):
        self._data_storage = ConfigAndKeyValueStorageDataModel(APP_NAME).getKeyValueStorage_LoadUsingConfig()

        self.cli_command = CLICommand(
            prog=Command.doc_site_index.cmd_name,
            description=Command.doc_site_index.desc
        )

        self.cli_command.set_execution_callback(self._execute_command)

        self.ignored_folders = ['.git']
        self.ignored_files  = ['index.md']

    def run(self, input_args: str):
        self.cli_command.parse_and_execute(input_args)

    def _execute_command(self, _):
        dataFolderPath = self.data_storage.get(StorageKey.DOC_SITE_DATA_FOLDER.value)

        if not dataFolderPath: 
            print(f"Error: No record for key {StorageKey.DOC_SITE_DATA_FOLDER.value}.")
        else:
            self.create_global_index(dataFolderPath)
            self.create_category_indexes(dataFolderPath)

    def create_global_index(self, base_path):
        global_index_path = os.path.join(base_path, 'index.md')

        with open(global_index_path, 'w') as global_index:
            global_index.write('# DOC SITE with atari monk\n\n')
            global_index.write('Hint: To toogle dark mode see Chrome->Dark Mode.\n\n')
            for category in os.listdir(base_path):
                category_path = os.path.join(base_path, category)
                if os.path.isdir(category_path) and category not in self.ignored_folders:
                    global_index.write(f'- [{category}]({category}/index.md)\n')

        print(f"Global index created at {global_index_path}")

    def create_category_indexes(self, base_path):
        for category in os.listdir(base_path):
            category_path = os.path.join(base_path, category)
            if os.path.isdir(category_path) and category not in self.ignored_folders:
                index_path = os.path.join(category_path, 'index.md')
                self.create_category_index(category_path, index_path)

    def create_category_index(self, category_path, index_path):
        with open(index_path, 'w') as category_index:
            category_name = os.path.basename(category_path)
            category_index.write(f'# {category_name}\n\n')

            for file in os.listdir(category_path):
                file_path = os.path.join(category_path, file)
                if file.endswith('.md') and file != 'index.md' and file not in self.ignored_files:
                    category_index.write(f'- [{file}]({file})\n')

        print(f"Index for category '{category_name}' created at {index_path}")
