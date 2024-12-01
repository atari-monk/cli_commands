# storage_commands.py

from doc_site.validate import ValidateCommand
from shared.command import Command
from shared.config import LOGGER_CONFIG
from cli_logger.logger import setup_logger

logger = setup_logger(__name__, LOGGER_CONFIG)

def load():
    return {
        Command.doc_site_validate.name: ValidateCommand().run
    }
