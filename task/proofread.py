from gemini_client import ask_gemini

def proofread(content, format_type):

    prompt = f"""
    Proofread and improve:

    {content}

    Fix:
    - Grammar
    - Clarity
    - Readability
    - Improve format: {format_type}
    - remove unnecessary academic words and cliches
    - humanize the conent
    - keep it concise

    Do not change meaning.
    """

    return ask_gemini(prompt)