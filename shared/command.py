from enum import Enum

class Command(Enum):
    doc_site_validate = ("doc_site_validate", "Validate rules of doc_site project")
    
    def __init__(self, cmd_name, desc):
        self.cmd_name = cmd_name
        self.desc = desc

    def __str__(self):
        return f"{self.cmd_name}: {self.desc}"
