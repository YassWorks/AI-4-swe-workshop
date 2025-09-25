# Workshop - **Error Insight Generator** Mini Project #1

This project is part of the "AI for software engineering" workshop scheduled for the 2025 IEEE CS Summer School event. And in this repo we break down one of the clever ways to use AI to learn and grow effectively as a software engineer without spoiling the learning experience.

#### Core Idea

Getting Immediate AI Insights on Errors. In this example, we focus on **C code**, but the helper function (`exec_file`) can be easily adapted to handle other programming languages.

## How to Use

1. Write your code in any C file
2. Use the `./get_help.bat` followed with the directory to the C file
3. If everything runs successfully, the output will print to the terminal as usual.  
4. If an error occurs, a file containing the full code, error message, and AI-generated insight will be created in the `/output` directory.  

## Inference Provider Used

We use **Cerebras** as the inference provider.  
It offers a generous free tier, making it well-suited for giving students access to powerful models such as **Qwen 3**.  
A different one can be used as long as it's compatible with LangChain (most are).

## Requirements

- **gcc** (for compiling C code)  
- **Cerebras API key** (for model inference)  
- **Python dependencies** listed in `requirements.txt`  

## Setup

```
python -m venv .venv

pip install -r requirements.txt
```
