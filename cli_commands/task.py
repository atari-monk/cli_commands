# task.py

from log_task.estimate_task import estimateTask
from log_task.report_task import reportTask
from shared.command import Command

def load():
    return {
        Command.task_estimate.cmd_name: estimateTask,
        Command.task_report.cmd_name: reportTask,
    }
