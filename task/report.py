from shared.logger_config import create_loggers
from task.estimate import TASK_LOG_FILE_NAME

def reportTask(_):
    TASK_REPORT_LOGGER_NAME = 'report_task'
    cliLogger, cliAndFileLogger = create_loggers(TASK_LOG_FILE_NAME, TASK_REPORT_LOGGER_NAME)

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
