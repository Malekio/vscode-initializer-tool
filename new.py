from os import makedirs 
from pathlib import Path 
from subprocess import run, CalledProcessError


def create_folder(path): 
    try:
        makedirs(path, exist_ok=True)
        print(f"Folder created at: {path}")
        return path
    except FileExistsError as e: 
        print("Folder exists, try with another name.")
        return None

def code_cmd(project_path): 
    try: 
        run(["code", str(project_path)], check=True)
        print("Opening project...")
    except FileNotFoundError as e: 
        print("VS code not found. Make sure 'code' is in your PATH")
    except CalledProcessError as e: 
        print("Failed to open VS Code")


if __name__=="__main__":
    
    # Enter the project name(folder name): 
    project = str(input())
    if not project: 
        raise ValueError("Name can not be empty! ")
    
    # "vscode_projects" can be changed to an existing folder on your machine.
    project_path = Path.home() / "vscode_projects" / project

    if create_folder(project_path): 
        code_cmd(project_path)
