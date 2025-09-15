from langchain_cerebras import ChatCerebras
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

def get_ai_insight(prompt: str) -> None:
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
            ("human", "{messages}"),
        ]
    )
    
    llm_chain = template | llm
    response = llm_chain.invoke({"human": prompt})
    if hasattr(response, "content"):
        return response.content
    else:
        return "[ERROR] Please retry, something went wrong."
