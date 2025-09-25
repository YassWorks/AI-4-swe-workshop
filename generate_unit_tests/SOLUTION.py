from dotenv import load_dotenv
from langchain_cerebras import ChatCerebras
from langgraph.prebuilt import create_react_agent
from tools import ALL_TOOLS
import os


load_dotenv()


def workflow_solution() -> None:
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

    llm = ChatCerebras(
        model=model_name,
        api_key=api_key,
        temperature=0,
    )

    agent = create_react_agent(
        model=llm,
        tools=ALL_TOOLS,
        prompt=system_prompt,
    )

    response = agent.invoke({"messages": [instructions]})

    if response.get("messages"):
        last_message = response["messages"][-1]
        print(last_message.content)
    else:
        print("Generation done without output.")
