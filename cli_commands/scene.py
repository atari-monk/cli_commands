# scene.py

from scenes.read_scenes_command import ReadScenesCommand
from scenes.write_scene_command import WriteSceneCommand
from shared.command import Command

def load():
    return {
        Command.scene_read.cmd_name: ReadScenesCommand().run,
        Command.scene_write.cmd_name: WriteSceneCommand().run,
    }
