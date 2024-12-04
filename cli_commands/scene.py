# scene.py

from scene.read import ReadCommand
from scene.write import WriteCommand
from shared.command import Command

def load():
    return {
        Command.scene_read.cmd_name: ReadCommand().run,
        Command.scene_write.cmd_name: WriteCommand().run,
    }
