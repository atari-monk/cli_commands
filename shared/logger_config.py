from dataclasses import dataclass

@dataclass
class LoggerConfig:
    cli_logger_name: str
    cli_and_file_logger_name: str
    log_file_name: str
