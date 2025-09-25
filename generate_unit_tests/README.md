# Workshop - **Unit Test Generator** Mini Project #2

This project is part of the "AI for software engineering" workshop scheduled for the 2025 IEEE CS Summer School event. And in this repo we break down one of the clever ways to use AI to learn and grow effectively as a software engineer without spoiling the learning experience.

#### Core Idea

Automatically generate comprehensive unit tests for existing code. In this example, we focus on **JavaScript code**, but the approach can be easily adapted to handle other programming languages.

## How to Use

1. Place your code in the `app/` directory
2. Use the `./generate_tests.bat` to run the test generation
3. AI-generated unit tests will be created for your codebase

## Inference Provider Used

We use **Cerebras** as the inference provider.  
It offers a generous free tier, making it well-suited for giving students access to powerful models such as **Qwen 3**.  
A different one can be used as long as it's compatible with LangChain (most are).

## Requirements

- **Cerebras API key** (for model inference)  
- **Python dependencies** listed in `requirements.txt`  

## Setup

```
python -m venv .venv

pip install -r requirements.txt
```
