from gemini_client import ask_gemini

def apply_tone(content, tone):
    prompt = f"""
    adjust and re-enforce the tone to the content below.

    Desired tone: {tone}

    Content: {content}
    """

    return ask_gemini(prompt)