from langchain_cerebras import ChatCerebras
from langchain_core.prompts import ChatPromptTemplate
from helpers.strip_thinking import strip_thinking_block
from dotenv import load_dotenv
import os


load_dotenv()


def get_ai_insight_solution(prompt: str) -> None:
    """
    Prints AI insight for help on a given error to a markdown file

    Args:
        prompt (str): full code + error message
    """

    model_name = "qwen-3-32b"
    api_key = os.getenv("CEREBRAS_API_KEY")
    
    llm = ChatCerebras(
        model=model_name,
        api_key=api_key,
        temperature=0,
    )
    
    with open("prompts/system_prompt.md", "r") as f:
        system_prompt = f.read()

    template = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{prompt}"),
        ]
    )
    
    llm_chain = template | llm
    response = llm_chain.invoke({"prompt": prompt}, )
    if hasattr(response, "content"):
        return strip_thinking_block(response.content)
    else:
        return "[ERROR] Please retry, something went wrong."
