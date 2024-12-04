# test.py

from cli_logger.logger import setup_logger
from shared.command import Command
from shared.config import LOGGER_CONFIG
from example.argparse import argparse
from shared.log_test import logTest

logger = setup_logger(__name__, LOGGER_CONFIG)

def load():
    return {
        Command.test_ping.cmd_name: lambda _: logger.info('ping'),
        Command.test_argparse.cmd_name: argparse,
        Command.test_log.cmd_name: logTest,
    }
