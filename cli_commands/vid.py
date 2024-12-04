from shared.command import Command
from vid.link import VideoDataCommand
from vid.vid_mp3 import VidToMp3Command

def load():
    return {
        Command.vidmp3.cmd_name: VidToMp3Command().run,
        Command.vid_write.cmd_name: VideoDataCommand().run
    }
