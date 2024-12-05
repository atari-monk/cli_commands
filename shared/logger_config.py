from dataclasses import dataclass
from cli_logger.logger import setup_logger
from shared.log_setup import getConsoleFileLoggerConfig, getConsoleLoggerConfig

@dataclass
class LoggerConfig:
    base_name: str
    logger_name: str = ""
    cli_logger_name: str = ""
    cli_and_file_logger_name: str = ""
    log_file_name: str = ""
    
    def __post_init__(self):
        if not self.logger_name:
            self.cli_logger_name = f"{self.base_name}_cli"
            self.cli_and_file_logger_name = self.base_name
        else:
            self.cli_logger_name = f"{self.logger_name}_cli"
            self.cli_and_file_logger_name = self.logger_name
        self.log_file_name = self.base_name

def create_loggers(base_name: str, logger_name: str = None):
    logger_config = LoggerConfig(base_name=base_name, logger_name=logger_name)
    
    cli_logger = setup_logger(logger_config.cli_logger_name, getConsoleLoggerConfig())
    cli_and_file_logger = setup_logger(logger_config.cli_and_file_logger_name, getConsoleFileLoggerConfig(logger_config.log_file_name))
    
    return cli_logger, cli_and_file_logger
