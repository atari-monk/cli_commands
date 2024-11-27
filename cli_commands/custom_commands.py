# custom_commands.py

from cli_commands.config import LOGGER_CONFIG
from convert.vid_to_mp3 import VidToMp3
from cli_logger.logger import setup_logger
from example.argparse import argparse
from log.log_test import logTest
from log.estimate_task import estimateTask
from log.report_task import reportTask

logger = setup_logger(__name__, LOGGER_CONFIG)

def load():
    def vidmp3(args):
        converter = VidToMp3()
        converter.run(args)

    def ping(_):
        logger.info('ping')

    return {
        "vidmp3": vidmp3,
        "ping": ping,
        "argparse": argparse,
        "logtest": logTest,
        "estimate": estimateTask,
        "report": reportTask
    }
