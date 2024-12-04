# report_task.py

from task.constant import CONSOLE_LOG, LOG_REPORT_TASK, LOG_TASK_NAME
from shared.log_setup import getConsoleLoggerConfig
from shared.log_setup import getConsoleFileLoggerConfig
from cli_logger.logger import setup_logger

def reportTask(_):
    cliLogger = setup_logger(f'{LOG_REPORT_TASK}_{CONSOLE_LOG}', getConsoleLoggerConfig())
    cliAndFileLogger = setup_logger(LOG_REPORT_TASK, getConsoleFileLoggerConfig(LOG_TASK_NAME))

    project = input("State project: ")
    task = input("State task: ")
    coded = input("Has the task been coded? (yes/no): ")
    tested = input("Has the task been tested? (yes/no): ")
    documented = input("Has the task been documented? (yes/no): ")
    committed = input("Has the task been committed? (yes/no): ")
    real_time = input("Actual time taken (e.g., 2 hours): ")
    
    log_data = {
        "project": project,
        "task": task,
        "coded": coded,
        "tested": tested,
        "documented": documented,
        "committed": committed,
        "real_time": real_time
    }
    
    cliAndFileLogger.info(log_data)
    cliLogger.info("\nYour input has been logged. Thank you!")
