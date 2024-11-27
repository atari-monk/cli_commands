## **CLI Tool Documentation: Log Command Set**

This document describes the functionality, purpose, and implementation of the `log` command set for a CLI tool. The commands facilitate structured task tracking, including estimation, reporting, and logging of task-related events. This system aims to streamline project management by providing comprehensive and detailed logs for tracking progress, time estimates, and task statuses.

---

### **Overview**

The `log` command set consists of modules designed to handle specific logging requirements for projects and tasks. Each command integrates dual logging outputs (console and file) and provides structured data storage for later analysis.

### **Modules**

#### **1. `log_test.py`**

**Purpose:**  
A utility script to verify and demonstrate logging configurations. It ensures that the logging setup is functional and capable of handling messages at different severity levels.

**Features:**

-   Tests logging for all severity levels: `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`.
-   Logs both to the console and a file for module-specific information.
-   Demonstrates exception logging by capturing stack traces.

**Use Case:**  
Useful for debugging the logger configuration and validating that logs are correctly stored and displayed.

---

#### **2. `estimate_task.py`**

**Purpose:**  
Captures user input to log estimated time for tasks. It helps plan and organize tasks by recording time estimates in a structured format.

**Features:**

-   **User Prompts**:
    -   Project name
    -   Task description
    -   Time estimate (e.g., "3 hours")
-   **Dual Logging**:
    -   Console: Provides immediate feedback to the user.
    -   File: Saves structured task details for persistence.
-   **Timestamped Entries**: Includes the date and time when the estimate was logged.

**Use Case:**  
Ideal for project managers or developers to plan tasks and estimate workloads efficiently.

**Example Workflow:**

1. Run the command via the CLI.
2. Enter the required information when prompted.
3. Review the logged estimate in the console or log file.

---

#### **3. `report_task.py`**

**Purpose:**  
Logs the status of completed tasks, including detailed information on progress and actual time spent. It ensures that all task lifecycle stages are tracked for auditing and review.

**Features:**

-   **User Prompts**:
    -   Project name
    -   Task description
    -   Status indicators (coded, tested, documented, committed)
    -   Actual time taken to complete the task
-   **Dual Logging**:
    -   Console: Confirms task report logging.
    -   File: Saves comprehensive task details in a structured format.
-   **Timestamped Entries**: Records the exact time of reporting.

**Use Case:**  
Designed for post-task reporting to monitor project progress and maintain accurate records of task completion.

**Example Workflow:**

1. Run the command via the CLI.
2. Enter the task details and status updates.
3. Review the logged report in the console or log file.

---

### **Technical Details**

#### **Logging Configuration**

All modules utilize a shared logging setup with customizable configurations:

-   **Console Logging**: Displays user-friendly messages during command execution.
-   **File Logging**: Saves structured and timestamped entries to a log file for later reference.

#### **Data Structure**

Each log entry includes:

-   **Timestamp**: Exact date and time when the entry was made.
-   **Project**: Project name for categorization.
-   **Task**: Task description for identification.
-   **Additional Fields** (varies by module):
    -   `estimate_task.py`: Time estimate.
    -   `report_task.py`: Status indicators (coded, tested, documented, committed) and actual time taken.

#### **Log Storage**

-   Log files are stored in a `logs` directory within the application's data folder.
-   File names are dynamically generated based on the module name to ensure clarity and separation.

---

### **Advantages of the Log Command Set**

1. **Centralized Task Management**:  
   Tracks tasks from estimation to completion, ensuring consistent record-keeping.

2. **Structured Data**:  
   Logs are formatted in dictionaries for easy parsing and analysis.

3. **Customizable Logging Levels**:  
   Developers can adjust log levels (e.g., `DEBUG`, `INFO`) as needed.

4. **Error Handling and Reporting**:  
   Captures exceptions and provides stack traces, aiding debugging efforts.

5. **Dual Output**:  
   Logs to both the console for real-time feedback and files for persistence.

---

### **Future Enhancements**

-   **Integration with Task Management Systems**:  
    Export logs to external systems or databases for comprehensive project tracking.

-   **Report Summaries**:  
    Generate periodic summaries of logged tasks and progress.

-   **Enhanced User Experience**:  
    Add options for command-line arguments to bypass interactive input.

---

### **Conclusion**

The `log` command set is a powerful tool for tracking and managing tasks efficiently. By offering modules for logging, estimation, and reporting, it provides a streamlined approach to project and task management while ensuring a structured and organized logging framework.
