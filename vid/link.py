import json
import os
from datetime import datetime
from shared.command import Command
from shared.cli_command import CLICommand
from shared.logger_config import create_loggers

class VideoDataCommand:
    def __init__(self):
        self.__cliLogger, self.__cliAndFileLogger = create_loggers(Command.vid_write.cmd_name)
        
        self.__cli_command = CLICommand(
            prog=Command.vid_write.cmd_name,
            description=Command.vid_write.desc
        )

        self.__cli_command.parser.add_argument('--title', type=str, help="Video title.")
        self.__cli_command.parser.add_argument('--link', type=str, help="Video link.")
        self.__cli_command.parser.add_argument('--desc', type=str, help="Video description.")
        self.__cli_command.parser.add_argument('--grade', type=int, choices=range(1, 11), help="Video grade (1-10).")
        self.__cli_command.parser.add_argument('--tags', type=str, help="Comma-separated tags for the video.")
        self.__cli_command.parser.add_argument('--upload_date', type=str, help="Video upload date (YYYY-MM-DD).")
        self.__cli_command.parser.add_argument('--duration', type=str, help="Video duration in minutes.")
        self.__cli_command.parser.add_argument('--comments', type=str, help="Any additional comments.")

        self.__cli_command.set_execution_callback(self._execute_command)

    def run(self, input_args: str):
        self.__cli_command.parse_and_execute(input_args)

    def _execute_command(self, parsed_args):
        try:
            title = parsed_args.title or input("Enter video title: ").strip()
            link = parsed_args.link or input("Enter video link: ").strip()
            desc = parsed_args.desc or input("Enter video description: ").strip()
            grade = parsed_args.grade or int(input("Enter grade (1-10): ").strip())
            if grade < 1 or grade > 10:
                print("Invalid grade input. Setting to default value of 5.")
                grade = 5
            tags = parsed_args.tags or input("Enter tags for the video (comma-separated): ").strip()
            upload_date = self._validate_date(parsed_args.upload_date or input("Enter video upload date (YYYY-MM-DD): ").strip())
            duration = self._validate_duration(parsed_args.duration or input("Enter video duration in minutes: ").strip())
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

            self.__cliLogger.info(f"Collected video data: {video_data}")
            self.__cliAndFileLogger.info(json.dumps(video_data, indent=2))

            if not os.path.exists('video_data.json'):
                with open('video_data.json', 'w') as file:
                    file.write("[]")  # Initialize an empty JSON array

            with open('video_data.json', 'a') as file:
                json.dump(video_data, file, indent=2)
                file.write("\n")
            print("Data saved successfully.")

        except Exception as e:
            self.__cliLogger.error(f"Error while executing command: {e}")
            print("An error occurred:", e)

    def _validate_date(self, date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")
    
    def _validate_duration(self, duration_str):
        if not duration_str.isdigit():
            raise ValueError("Duration must be a numeric value in minutes.")
        return int(duration_str)
