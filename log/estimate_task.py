import datetime
from log.log_setup import getConsoleLoggerConfig
from log.log_setup import getConsoleFileLoggerConfig
from cli_logger.logger import setup_logger
from cli_logger.logger import LoggerConfig

def estimateTask(_):
    console_config = getConsoleLoggerConfig()
    console_file_config = getConsoleFileLoggerConfig(__name__)

    consoleLogger = setup_logger(f'{__name__}console', console_config)
    consoleFileLogger = setup_logger(__name__, console_file_config)

    consoleFileLogger.info(f'LOG_FILE_PATH, {console_file_config[LoggerConfig.LOG_FILE_PATH]}')

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
