from shared.cli_command import CLICommand
from shared.command import Command
from shared.constants import APP_NAME
from shared.storage_key import StorageKey
from vid.vid_mp3_convert import VidToMp3
from keyval_storage.config_and_key_value_storage_data_model import ConfigAndKeyValueStorageDataModel
from pytoolbox.file_system import ensure_folder_exists

class VidToMp3Command:
    def __init__(self):
        self._data_storage = ConfigAndKeyValueStorageDataModel(APP_NAME).getKeyValueStorage_LoadUsingConfig()        
        self.vid_to_mp3 = VidToMp3()

        self.cli_command = CLICommand(
            prog=Command.vidmp3.cmd_name,
            description=Command.vidmp3.desc
        )

        self.cli_command.parser.add_argument(
            'video_url',
            type=str,
            help="The YouTube URL of the video to download as MP3."
        )

        self.cli_command.set_execution_callback(self._execute_command)

    def run(self, input_args: str):
        self.cli_command.parse_and_execute(input_args)

    def _execute_command(self, parsed_args):
        video_url = parsed_args.video_url
        output_folder = self.data_storage.get(StorageKey.VID_TO_MP3_SAVE_FOLDER.value)

        if not output_folder:
            output_folder = input("Provide folder to SAVE downloads> ").strip()
            ensure_folder_exists(output_folder)
            self.data_storage.set(StorageKey.VID_TO_MP3_SAVE_FOLDER.value, output_folder)

        self.vid_to_mp3.validate_and_download(video_url, output_folder)
