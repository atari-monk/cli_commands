# Job Search

A CLI tool for tracking job-search-related data can collect various information about your efforts and progress. Here’s a breakdown of the information you might want to include:

---

### **Core Data to Collect**

1. **Job Details**

    - **Job Title**: Name of the job role.
    - **Company Name**: Name of the hiring organization.
    - **Job Type**: Permanent, Contract, Freelance, Internship, etc.
    - **Location**: City or remote.
    - **Salary Range**: If available.
    - **Application Date**: When you applied.
    - **Status**: Applied, Interviewing, Offered, Rejected, Pending.

2. **Portal/Source**

    - **Job Portal**: Platform where you found the job (e.g., LinkedIn, Indeed, Glassdoor).
    - **Referral Source**: Mention if referred by someone.
    - **Job Posting URL**: Optional, but useful for tracking.

3. **Skills**

    - **Skills Required**: Key skills listed in the job description.
    - **Skills Matched**: Skills you possess that match the requirements.
    - **Skill Gaps**: Skills you might need to learn or improve.

4. **Job Description**
    - Brief description or summary (optional but handy for review).

---

### **Additional Data to Collect**

5. **Personal Interaction**

    - **Contact Person**: Name of recruiter or manager.
    - **Email/Phone**: Contact details.
    - **Follow-up Date**: Date to follow up on the application.

6. **Company Research**

    - **Company Size**: Small, medium, large.
    - **Company Industry**: Tech, Finance, Healthcare, etc.
    - **Glassdoor Rating**: Optional, if researching reviews.

7. **Preparation Tracking**

    - **Resume Version Used**: If you tailor resumes for different roles.
    - **Cover Letter**: Whether it was submitted.
    - **Portfolio/Projects**: Links or mentions of relevant portfolio items.

8. **Outcome and Feedback**
    - **Interview Stages**: Count or descriptions (e.g., HR, Technical, Final).
    - **Feedback Received**: Any notes from recruiters or interviewers.
    - **Reason for Rejection (if applicable)**: To improve future applications.

---

### **Organizational Features**

-   **Timestamp**: Automatically log the date and time of entry.
-   **Tags**: Allow tagging entries with custom tags for better sorting (e.g., “urgent,” “dream job”).

---

### **Potential Extensions**

-   **Analytics**: Track the success rate of applications by portal, job type, or skill match.
-   **Reminders**: Option to set reminders for follow-ups.
-   **Learning Resources**: Recommend learning materials for skill gaps.

---

Would you like me to draft a Python CLI script based on this outline, or would you like to refine this list further?

## Design proposition

Based on your examples, we can design a CLI command for job search data collection that uses **composition** with a base class (`CLICommand`) and supports **logging** for input data. The new command will:

1. Accept various inputs related to job applications (job title, company name, skills, etc.).
2. Validate and store the inputs.
3. Log the collected data for reference.

Here’s how the implementation could look:

---

### **Job Search CLI Command**

```python
from typing import Any
from shared.cli_command import CLICommand
from log.log_setup import setup_logger, getConsoleLoggerConfig, getConsoleFileLoggerConfig

class JobSearchCommand:
    def __init__(self):
        # Logger setup
        console_config = getConsoleLoggerConfig()
        console_file_config = getConsoleFileLoggerConfig("job_search")
        self.console_logger = setup_logger("job_search_console", console_config)
        self.file_logger = setup_logger("job_search_file", console_file_config)

        # CLICommand setup
        self.cli_command = CLICommand(
            prog="jobsearch",
            description="Collect data about job searching."
        )

        # Adding arguments
        self.cli_command.parser.add_argument('--title', type=str, help="Job title.")
        self.cli_command.parser.add_argument('--company', type=str, help="Company name.")
        self.cli_command.parser.add_argument('--location', type=str, help="Job location.")
        self.cli_command.parser.add_argument('--skills', type=str, help="Comma-separated required skills.")
        self.cli_command.parser.add_argument('--portal', type=str, help="Job portal or source.")
        self.cli_command.parser.add_argument('--status', type=str, choices=['applied', 'interviewing', 'offered', 'rejected', 'pending'], help="Application status.")
        self.cli_command.parser.add_argument('--feedback', type=str, help="Feedback received (if any).")

        # Setting the execution callback
        self.cli_command.set_execution_callback(self._execute_command)

    def run(self, input_args: str):
        """Parse and execute the command."""
        self.cli_command.parse_and_execute(input_args)

    def _execute_command(self, parsed_args):
        """Handle the parsed arguments and log the data."""
        job_data = {
            "Job Title": parsed_args.title or input("Enter job title: ").strip(),
            "Company Name": parsed_args.company or input("Enter company name: ").strip(),
            "Location": parsed_args.location or input("Enter job location: ").strip(),
            "Skills": parsed_args.skills or input("Enter required skills (comma-separated): ").strip(),
            "Job Portal": parsed_args.portal or input("Enter job portal/source: ").strip(),
            "Application Status": parsed_args.status or input("Enter application status (applied/interviewing/offered/rejected/pending): ").strip(),
            "Feedback": parsed_args.feedback or input("Enter feedback (optional): ").strip(),
        }

        # Log to console and file
        self.console_logger.info(f"Collected job data: {job_data}")
        self.file_logger.info(job_data)

        print("\nJob search data has been logged successfully!")

```

---

### **Key Features**

1. **Arguments and Interactivity**: Supports command-line arguments while prompting for missing data interactively.
2. **Validation**: Ensures the `status` field uses predefined choices.
3. **Logging**: Logs the collected data to both the console and a file for easy tracking.
4. **Flexibility**: Allows optional fields like `feedback`.

---

### **Usage Example**

#### 1. Command with CLI Arguments:

```bash
python your_script.py jobsearch --title "Software Engineer" --company "TechCorp" --location "Remote" --skills "Python,SQL" --portal "LinkedIn" --status "applied"
```

#### 2. Interactive Mode:

```bash
python your_script.py jobsearch
```

The script will prompt for any missing fields.

---

Would you like to refine the features or add additional functionality, such as storing this data in a database or generating reports?
