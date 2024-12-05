from shared.logger_config import create_loggers

TASK_LOG_FILE_NAME = 'log_task'

def estimateTask(_):
    TASK_ESTIMATE_LOGGER_NAME = 'estimate_task'
    cliLogger, cliAndFileLogger = create_loggers(TASK_LOG_FILE_NAME, TASK_ESTIMATE_LOGGER_NAME)

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
