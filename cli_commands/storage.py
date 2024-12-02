# storage.py

from shared.command import Command
from storage.read import StorageReadCommand
from storage.set import StorageSetCommand

def load():
    return {
        Command.storage_read.cmd_name: StorageReadCommand().run,
        Command.storage_set.cmd_name: StorageSetCommand().run
    }
