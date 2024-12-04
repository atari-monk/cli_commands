from shared.command import Command
from shared.log_setup import getConsoleFileLoggerConfig, getConsoleLoggerConfig
from shared.cli_command import CLICommand
from cli_logger.logger import setup_logger

class JobCommand:
    def __init__(self):
        self.cliLogger = setup_logger("job_search_console", getConsoleLoggerConfig())
        self.cliFileLogger = setup_logger("job_search_file", getConsoleFileLoggerConfig("job_search"))

        self.cli_command = CLICommand(
            prog=Command.job_write.cmd_name,
            description=Command.job_write.desc
        )

        self.cli_command.parser.add_argument('--title', type=str, help="Job title.")
        self.cli_command.parser.add_argument('--company', type=str, help="Company name.")
        self.cli_command.parser.add_argument('--location', type=str, help="Job location.")
        self.cli_command.parser.add_argument('--skills', type=str, help="Comma-separated required skills.")
        self.cli_command.parser.add_argument('--portal', type=str, help="Job portal or source.")
        self.cli_command.parser.add_argument('--status', type=str, choices=['applied', 'interviewing', 'offered', 'rejected', 'pending'], help="Application status.")
        self.cli_command.parser.add_argument('--feedback', type=str, help="Feedback received (if any).")

        self.cli_command.set_execution_callback(self._execute_command)

    def run(self, input_args: str):
        self.cli_command.parse_and_execute(input_args)

    def _execute_command(self, parsed_args):
        job_data = {
            "Job Title": parsed_args.title or input("Enter job title: ").strip(),
            "Company Name": parsed_args.company or input("Enter company name: ").strip(),
            "Location": parsed_args.location or input("Enter job location: ").strip(),
            "Skills": parsed_args.skills or input("Enter required skills (comma-separated): ").strip(),
            "Job Portal": parsed_args.portal or input("Enter job portal/source: ").strip(),
            "Application Status": parsed_args.status or input("Enter application status (applied/interviewing/offered/rejected/pending): ").strip(),
            "Feedback": parsed_args.feedback or input("Enter feedback (optional): ").strip(),
        }

        self.cliLogger.info(f"Collected job data: {job_data}")
        self.cliFileLogger.info(job_data)

        print("\nJob search data has been logged successfully!")
