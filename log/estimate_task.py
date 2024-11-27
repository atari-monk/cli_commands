# estimate_task.py

import datetime
from log.constants import CONSOLE_LOG, LOG_TASK_NAME
from log.log_setup import getConsoleLoggerConfig
from log.log_setup import getConsoleFileLoggerConfig
from cli_logger.logger import setup_logger

def estimateTask(_):
    console_config = getConsoleLoggerConfig()
    console_file_config = getConsoleFileLoggerConfig(LOG_TASK_NAME)

    consoleLogger = setup_logger(f'{LOG_TASK_NAME}_{CONSOLE_LOG}', console_config)
    consoleFileLogger = setup_logger(LOG_TASK_NAME, console_file_config)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    project = input("State project: ")
    task = input("State task: ")
    time_estimate = input("State time estimate (e.g., 2 hours): ")
    
    log_data = {
        "timestamp": timestamp,
        "project": project,
        "task": task,
        "time_estimate": time_estimate
    }
    consoleFileLogger.info(log_data)
    consoleLogger.info("\nYour input has been logged. Thank you!")
