import json
from shared.command import Command
from shared.log_setup import getConsoleFileLoggerConfig, getConsoleLoggerConfig
from shared.cli_command import CLICommand
from cli_logger.logger import setup_logger
from shared.logger_config import LoggerConfig

class VideoDataCommand:
    def __init__(self):
        self.loggerConfig = LoggerConfig(
            cli_logger_name="video_data_console",
            cli_and_file_logger_name="video_data_console_and_file",
            log_file_name="video_data")
        
        self.cliLogger = setup_logger(self.loggerConfig.cli_logger_name, getConsoleLoggerConfig())
        self.cliAndFileLogger = setup_logger(self.loggerConfig.cli_and_file_logger_name, getConsoleFileLoggerConfig(self.loggerConfig.log_file_name))

        self.cli_command = CLICommand(
            prog=Command.vid_write.cmd_name,
            description=Command.vid_write.desc
        )

        self.cli_command.parser.add_argument('--title', type=str, help="Video title.")
        self.cli_command.parser.add_argument('--link', type=str, help="Video link.")
        self.cli_command.parser.add_argument('--desc', type=str, help="Video description.")
        self.cli_command.parser.add_argument('--grade', type=int, choices=range(1, 11), help="Video grade (1-10).")
        self.cli_command.parser.add_argument('--tags', type=str, help="Comma-separated tags for the video.")
        self.cli_command.parser.add_argument('--upload_date', type=str, help="Video upload date (YYYY-MM-DD).")
        self.cli_command.parser.add_argument('--duration', type=str, help="Video duration in minutes.")
        self.cli_command.parser.add_argument('--comments', type=str, help="Any additional comments.")

        self.cli_command.set_execution_callback(self._execute_command)

    def run(self, input_args: str):
        self.cli_command.parse_and_execute(input_args)

    def _execute_command(self, parsed_args):
        title = parsed_args.title or input("Enter video title: ").strip()
        link = parsed_args.link or input("Enter video link: ").strip()
        desc = parsed_args.desc or input("Enter video description: ").strip()
        grade = parsed_args.grade or int(input("Enter grade (1-10): ").strip())

        if grade < 1 or grade > 10:
            print("Invalid grade input. Setting to default value of 5.")
            grade = 5

        tags = parsed_args.tags or input("Enter tags for the video (comma-separated): ").strip()
        upload_date = parsed_args.upload_date or input("Enter video upload date (YYYY-MM-DD): ").strip()
        duration = parsed_args.duration or input("Enter video duration in minutes: ").strip()
        comments = parsed_args.comments or input("Enter any additional comments: ").strip()

        video_data = {
            "title": title,
            "link": link,
            "desc": desc,
            "grade": grade,
            "tags": tags.split(",") if tags else [],
            "upload_date": upload_date,
            "duration": duration,
            "comments": comments
        }

        self.cliLogger.info(f"Collected video data: {video_data}")
        self.cliAndFileLogger.info(json.dumps(video_data, indent=2))

        with open('video_data.json', 'a') as file:
            json.dump(video_data, file, indent=2)
            file.write("\n")
        print("Data saved successfully.")

        print("\nVideo data has been logged successfully!")
