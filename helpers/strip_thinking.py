def strip_thinking_block(response: str) -> str:
    return (
        response[response.find("</think>") + len("</think>") :].strip()
        if "</think>" in response
        else response.strip()
    )
