from dataclasses import dataclass
from cli_logger.logger import setup_logger
from shared.log_setup import getConsoleFileLoggerConfig, getConsoleLoggerConfig

@dataclass
class LoggerConfig:
    base_name: str
    cli_logger_name: str = ""
    cli_and_file_logger_name: str = ""
    log_file_name: str = ""
    
    def __post_init__(self):
        self.cli_logger_name = f"{self.base_name}_console"
        self.cli_and_file_logger_name = f"{self.base_name}_console_and_file"
        self.log_file_name = self.base_name

def create_loggers(base_name: str):
    logger_config = LoggerConfig(base_name=base_name)
    
    cli_logger = setup_logger(logger_config.cli_logger_name, getConsoleLoggerConfig())
    cli_and_file_logger = setup_logger(logger_config.cli_and_file_logger_name, getConsoleFileLoggerConfig(logger_config.log_file_name))
    
    return cli_logger, cli_and_file_logger
