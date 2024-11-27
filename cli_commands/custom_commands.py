# custom_commands.py

from shared.config import LOGGER_CONFIG
from cli_logger.logger import setup_logger
from example.argparse import argparse
from log.log_test import logTest
from log.estimate_task import estimateTask
from log.report_task import reportTask
from vid_to_mp3.vid_to_mp3_command import VidToMp3Command

logger = setup_logger(__name__, LOGGER_CONFIG)

def load():
    return {
        "vidmp3": VidToMp3Command().run,
        "ping": lambda _: logger.info('ping'),
        "argparse": argparse,
        "logtest": logTest,
        "estimate": estimateTask,
        "report": reportTask
    }
