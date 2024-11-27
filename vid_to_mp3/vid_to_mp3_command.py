import argparse
from shared.constants import APP_NAME, DOWNLOAD_FOLDER_KEY
from vid_to_mp3.vid_to_mp3 import VidToMp3
from keyval_storage.config_and_key_value_storage_data_model import ConfigAndKeyValueStorageDataModel
from pytoolbox.file_system import ensure_folder_exists

class VidToMp3Command:
    def __init__(self):
        self._dataStorage = ConfigAndKeyValueStorageDataModel(APP_NAME)
        self.vid_to_mp3 = VidToMp3()

    def run(self, args):
        dataStorage = self._dataStorage.getKeyValueStorage_LoadUsingConfig()
        output_folder = dataStorage.get(DOWNLOAD_FOLDER_KEY)
        
        if not output_folder:
            output_folder = input("Provide folder to SAVE downloads> ").strip()
            ensure_folder_exists(output_folder)
            dataStorage.set(DOWNLOAD_FOLDER_KEY, output_folder)

        args = self._parse_arguments()
        self._execute_command(args, output_folder)

    def _parse_arguments(self):
        parser = argparse.ArgumentParser(description="Download YouTube video as MP3")
        parser.add_argument(
            'video_url',
            type=str,
            help="The YouTube URL of the video to download as MP3."
        )
        return parser.parse_args()

    def _execute_command(self, args, output_folder: str):
        video_url = args.video_url
        self.vid_to_mp3.run(video_url, output_folder)
