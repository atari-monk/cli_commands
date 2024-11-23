# custom_commands.py

from convert.video_to_mp3 import VideoToMp3
from cli_logger.logger import setup_logger, LoggerConfig

logger = setup_logger(__name__, LoggerConfig)

def load():
    logger.debug("custom_commands.load() called")

    def vidmp3(args):
        logger.info(f"Video to mp3, Args received: {args}")
        converter = VideoToMp3()
        converter.run(args)

    return {
        "vidmp3": vidmp3
    }
