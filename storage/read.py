from shared.cli_command import CLICommand
from shared.command import Command
from shared.constants import APP_NAME
from keyval_storage.config_and_key_value_storage_data_model import ConfigAndKeyValueStorageDataModel

class ReadCommand:
    def __init__(self):
        self._data_storage = ConfigAndKeyValueStorageDataModel(APP_NAME).getKeyValueStorage_LoadUsingConfig()

        self.cli_command = CLICommand(
            prog=Command.storage_read.cmd_name,
            description=Command.storage_read.desc
        )

        self.cli_command.set_execution_callback(self._execute_command)

    def run(self, input_args: str):
        self.cli_command.parse_and_execute(input_args)

    def _execute_command(self, _):
        for key, value in self.data_storage._read_data().items():
            print(f"{key}: {value}")
