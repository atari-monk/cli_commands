from shared.command import Command
from storage.read import ReadCommand
from storage.set import SetCommand

def load():
    return {
        Command.storage_read.cmd_name: ReadCommand().run,
        Command.storage_set.cmd_name: SetCommand().run
    }
