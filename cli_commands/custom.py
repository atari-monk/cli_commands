# custom.py

from job_search.job_search_command import JobSearchCommand
from log_vid.video_data_command import VideoDataCommand
from shared.command import Command
from vid_to_mp3.vid_to_mp3_command import VidToMp3Command

def load():
    return {
        Command.vidmp3.cmd_name: VidToMp3Command().run,
        Command.job_write.cmd_name: JobSearchCommand().run,
        Command.vid_write.cmd_name: VideoDataCommand().run
    }
