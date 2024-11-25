# custom_commands.py

from cli_commands.config import LOGGER_CONFIG
from convert.video_to_mp3 import VideoToMp3
from cli_logger.logger import setup_logger
from example.argparse import argparse_command

logger = setup_logger(__name__, LOGGER_CONFIG)

def load():
    def vidmp3(args):
        converter = VideoToMp3()
        converter.run(args)

    def ping(_):
        logger.info('ping')

    def argparse(args):
        argparse_command(args)

    return {
        "vidmp3": vidmp3,
        "ping": ping,
        "argparse": argparse
    }
