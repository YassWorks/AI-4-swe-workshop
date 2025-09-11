import subprocess
import os


def exec_file(file_path: str) -> tuple[int, str]:
    """
    Execute a C file.
    
    Args:
        file_path (str): path to the C file
    
    Returns:
        tuple(int, str): return code and output
    """
    result = subprocess.run(
        ["gcc", file_path, "-o", "output/output"], capture_output=True, text=True
    )
    if result.returncode != 0:
        return result.returncode, result.stderr

    result = subprocess.run(["./output/output"], capture_output=True, text=True)
    return result.returncode, result.stdout


def get_ai_insight(prompt: str) -> None:
    """
    Prints AI insight for help on a given error to a markdown file
    
    Args:
        prompt (str): full code + error message
    """
    ...


if __name__ == "__main__":

    os.makedirs("output", exist_ok=True)
    file_path = "app.c"
    
