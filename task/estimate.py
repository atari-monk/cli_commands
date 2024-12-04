# estimate.py

from task.constant import CONSOLE_LOG, LOG_ESTIMATE_TASK, LOG_TASK_NAME
from shared.log_setup import getConsoleLoggerConfig
from shared.log_setup import getConsoleFileLoggerConfig
from cli_logger.logger import setup_logger

def estimateTask(_):
    cliLogger = setup_logger(f'{LOG_ESTIMATE_TASK}_{CONSOLE_LOG}', getConsoleLoggerConfig())
    cliAndFileLogger = setup_logger(LOG_ESTIMATE_TASK, getConsoleFileLoggerConfig(LOG_TASK_NAME))

    project = input("State project: ")
    task = input("State task: ")
    time_estimate = input("State time estimate (e.g., 2 hours): ")
    
    log_data = {
        "project": project,
        "task": task,
        "time_estimate": time_estimate
    }

    cliAndFileLogger.info(log_data)
    cliLogger.info("\nYour input has been logged. Thank you!")
