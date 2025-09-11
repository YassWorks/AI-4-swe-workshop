import subprocess
import os


def exec_file(file_path: str) -> str:

    result = subprocess.run(
        ["gcc", file_path, "-o", "output/output"], capture_output=True, text=True
    )
    if result.returncode != 0:
        return result.stderr

    result = subprocess.run(["./output/output"], capture_output=True, text=True)
    return result.stdout


if __name__ == "__main__":

    os.makedirs("output", exist_ok=True)
    file_path = "app.c"
    output = exec_file(file_path)
    print(output)
