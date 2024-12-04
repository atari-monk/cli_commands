from vid.link import VideoDataCommand
from shared.command import Command
from vid.vid_to_mp3_command import VidToMp3Command

def load():
    return {
        Command.vidmp3.cmd_name: VidToMp3Command().run,
        Command.vid_write.cmd_name: VideoDataCommand().run
    }
