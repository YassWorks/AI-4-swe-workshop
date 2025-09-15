from datetime import datetime
import subprocess
import os


def exec_file(file_path: str, time: str) -> tuple[int, str]:
    """
    Execute a C file.

    Args:
        file_path (str): path to the C file

    Returns:
        tuple(int, str): return code and output
    """
    output_file = f"executables/output-{time}"
    result = subprocess.run(
        ["gcc", file_path, "-o", output_file], capture_output=True, text=True
    )
    if result.returncode != 0:
        return result.returncode, result.stderr

    result = subprocess.run([output_file], capture_output=True, text=True)
    return result.returncode, result.stdout


def get_ai_insight(prompt: str) -> None:
    """
    Prints AI insight for help on a given error to a markdown file

    Args:
        prompt (str): full code + error message
    """
    ##### YOUR CODE HERE #####
    return "it worked"
    ##########################


def workflow(file_path: str, time: str) -> None:
    """
    Main workflow to execute a C file and get AI insight if it fails.

    Args:
        file_path (str): path to the C file
    """
    return_code, output = exec_file(file_path, time)
    if return_code != 0:

        with open(file_path, "r") as f:
            code = f.read()

        payload = f"Code:\n\n{code}\n\n{'#' * 50}\n\nError:\n\n{output}\n\n{'#' * 50}"
        with open("instructions.md", "r") as f:
            instructions = f.read()

        insight = get_ai_insight(payload + instructions)
        insight_file = f"output/insight-{time}.md"
        with open(insight_file, "w") as f:
            f.write(payload + "\n\n" + insight)

        print("\n[Execution failed]. Error message:\n")
        print(output)
    else:
        print("\n[Execution successful]. Output:\n")
        print(output)


if __name__ == "__main__":

    time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    os.makedirs("executables", exist_ok=True)
    os.makedirs("output", exist_ok=True)
    file_path = "app.c"
    workflow(file_path, time)
