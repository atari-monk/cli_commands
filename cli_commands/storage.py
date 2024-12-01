# storage_commands.py

from shared.config import LOGGER_CONFIG
from cli_logger.logger import setup_logger
from storage.read import StorageReadCommand
from storage.set import StorageSetCommand

logger = setup_logger(__name__, LOGGER_CONFIG)

def load():
    return {
        "storage_read": StorageReadCommand().run,
        "storage_set": StorageSetCommand().run
    }
