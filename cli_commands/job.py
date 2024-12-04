from job.job_search_command import JobSearchCommand
from shared.command import Command

def load():
    return {
        Command.job_write.cmd_name: JobSearchCommand().run,
    }
