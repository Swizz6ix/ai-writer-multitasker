from gemini_client import ask_gemini

def proofread(content):

    prompt = f"""
    Proofread and improve:

    {content}

    Fix:
    - Grammar
    - Clarity
    - Readability

    Do not change meaning.
    """

    return ask_gemini(prompt)