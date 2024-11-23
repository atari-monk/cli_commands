# custom_commands.py

from cli_commands.config import LOGGER_CONFIG
from convert.video_to_mp3 import VideoToMp3
from cli_logger.logger import setup_logger

logger = setup_logger(__name__, LOGGER_CONFIG)

def load():
    logger.debug("custom_commands.load() called")

    def vidmp3(args):
        logger.info(f"Video to mp3, Args received: {args}")
        converter = VideoToMp3()
        converter.run(args)

    return {
        "vidmp3": vidmp3
    }
