# storage_commands.py

from doc_site.index import IndexCommand
from doc_site.validate import ValidateCommand
from doc_site.write import WriteCommand
from shared.command import Command
from shared.config import LOGGER_CONFIG
from cli_logger.logger import setup_logger

logger = setup_logger(__name__, LOGGER_CONFIG)

def load():
    return {
        Command.doc_site_validate.cmd_name: ValidateCommand().run,
        Command.doc_site_index.cmd_name: IndexCommand().run,
        Command.doc_site_write.cmd_name: WriteCommand().run,

    }
