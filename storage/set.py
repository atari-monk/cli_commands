from shared.cli_command import CLICommand
from shared.command import Command
from shared.constants import APP_NAME
from keyval_storage.config_and_key_value_storage_data_model import ConfigAndKeyValueStorageDataModel

class SetCommand:
    def __init__(self):
        self._data_storage = ConfigAndKeyValueStorageDataModel(APP_NAME).getKeyValueStorage_LoadUsingConfig()

        self.cli_command = CLICommand(
            prog=Command.storage_set.cmd_name,
            description=Command.storage_set.desc
        )

        self.cli_command.add_argument('--key', type=str, help="Key for the value to be set", required=True)
        self.cli_command.add_argument('--value', type=str, help="Value to be set for the specified key", required=True)

        self.cli_command.set_execution_callback(self._execute_command)

    def run(self, input_args: str):
        self.cli_command.parse_and_execute(input_args)

    def _execute_command(self, parsed_args):
        key = parsed_args.key
        value = parsed_args.value

        self.data_storage.set(key, value)
        
        print(f"Set {key} to {value}")
