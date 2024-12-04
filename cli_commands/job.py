from job.job_search_command import JobCommand
from shared.command import Command

def load():
    return {
        Command.job_write.cmd_name: JobCommand().run,
    }
