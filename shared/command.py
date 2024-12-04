from enum import Enum

class Command(Enum):
    storage_read = ("storage_read", "Read storage, all records")
    storage_set = ("storage_set", "Set key value pair in sotorage")

    doc_site_validate = ("doc_site_validate", "Validate rules of doc_site")
    doc_site_index = ("doc_site_index", "Generate indexes for doc_site")
    doc_site_write = ("doc_site_write", "Write md file for doc_site")
    
    task_estimate = ("task_estimate", "Estimate the duration of tasks and automatically timestamp the start of each task when it begins")
    task_report  = ("task_report", "Report task real time")

    scene_read = ("scene_read", "Read scenes")
    scene_write  = ("scene_write ", "Write scene")

    test_ping = ("test_ping ", "Loggs ping to console")
    test_argparse = ("test_argparse", "Test of argparse")
    test_log  = ("test_log", "Test of log setup")

    vidmp3 = ("vidmp3", "Video to mp3")
    job_write = ("job_write", "Write job offer record")    
    vid_write = ("vid_write", "Write record on video")

    def __init__(self, cmd_name, desc):
        self.cmd_name = cmd_name
        self.desc = desc

    def __str__(self):
        return f"{self.cmd_name}: {self.desc}"
