from langchain_core.tools import tool
import os


@tool
def read_file(file_path: str) -> str:
    """
    Read the contents of a file.
    
    Args:
        file_path (str): The path to the file to be read.
        
    Returns:
        str: The contents of the file or an error message if the file cannot be read.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        return f"Error: {str(e)}"


@tool
def write_file(file_path: str, content: str) -> str:
    """
    Write content to a file.
    
    Args:
        file_path (str): The path to the file where content will be written.
        content (str): The content to write to the file.
        
    Returns:
        str: A success message or an error message if the file cannot be written.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        return "File written successfully."
    except Exception as e:
        return f"Error: {str(e)}"


@tool
def create_wd(directory_path: str) -> str:
    """
    Create a new working directory.
    
    Args:
        directory_path (str): The path to the directory to be created.
        
    Returns:
        str: A success message or an error message if the directory cannot be created.
    """
    try:
        os.makedirs(directory_path, exist_ok=True)
        return "Directory created successfully."
    except Exception as e:
        return f"Error: {str(e)}"


ALL_TOOLS = [read_file, write_file, create_wd]
