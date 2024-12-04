# task.py

from task.estimate import estimateTask
from task.report import reportTask
from shared.command import Command

def load():
    return {
        Command.task_estimate.cmd_name: estimateTask,
        Command.task_report.cmd_name: reportTask,
    }
