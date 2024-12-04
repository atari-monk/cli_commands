from job.write import WriteCommand
from shared.command import Command

def load():
    return {
        Command.job_write.cmd_name: WriteCommand().run,
    }
