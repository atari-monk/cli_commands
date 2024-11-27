# report_task.py

import datetime
from log.constants import CONSOLE_LOG, LOG_TASK_NAME
from log.log_setup import getConsoleLoggerConfig
from log.log_setup import getConsoleFileLoggerConfig
from cli_logger.logger import setup_logger

def reportTask(_):
    console_config = getConsoleLoggerConfig()
    console_file_config = getConsoleFileLoggerConfig(LOG_TASK_NAME)

    consoleLogger = setup_logger(f'{LOG_TASK_NAME}_{CONSOLE_LOG}', console_config)
    consoleFileLogger = setup_logger(LOG_TASK_NAME, console_file_config)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    project = input("State project: ")
    task = input("State task: ")
    coded = input("Has the task been coded? (yes/no): ")
    tested = input("Has the task been tested? (yes/no): ")
    documented = input("Has the task been documented? (yes/no): ")
    committed = input("Has the task been committed? (yes/no): ")
    real_time = input("Actual time taken (e.g., 2 hours): ")
    
    log_data = {
        "timestamp": timestamp,
        "project": project,
        "task": task,
        "coded": coded,
        "tested": tested,
        "documented": documented,
        "committed": committed,
        "real_time": real_time
    }
    
    consoleFileLogger.info(log_data)
    consoleLogger.info("\nYour input has been logged. Thank you!")
