from gemini_client import ask_gemini

def expand_outline(outline):

    prompt = f"""
    Expand the following outline into
    a complete article.
    Outline:
    {outline}
    Write detailed paragraphs.
    """

    return ask_gemini(prompt)