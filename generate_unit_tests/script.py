from dotenv import load_dotenv
from langchain_cerebras import ChatCerebras
from langgraph.prebuilt import create_react_agent
from tools import ALL_TOOLS
import os


load_dotenv()


def workflow() -> None:
    """
    Main workflow to generate unit tests for a project.

    Args:
        project_directory (str): path to the project
    """

    model_name = "qwen-3-32b"
    api_key = os.getenv("CEREBRAS_API_KEY")

    with open("prompts/system_prompt.md", "r") as f:
        system_prompt = f.read()

    with open("prompts/instructions.md", "r") as f:
        instructions = f.read()

    ##### YOUR CODE HERE #####
    pass
    ##########################


if __name__ == "__main__":

    workflow()
