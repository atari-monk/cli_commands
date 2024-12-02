import os

class PathTool:
    @staticmethod
    def list_first_level_folders(path: str) -> list[str]:
        if not os.path.isdir(path):
            raise ValueError(f"Provided path '{path}' is not a valid directory.")
        
        return [folder for folder in os.listdir(path) if os.path.isdir(os.path.join(path, folder))]