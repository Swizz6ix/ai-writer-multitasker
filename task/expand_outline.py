from gemini_client import ask_gemini

def expand_outline(outline, tone, audience, format_type):

    prompt = f"""
    ROLE: 
    You are a professional writing assistant.

    CONTEXT"
    I do alot of writing work, I want to increase 
    my writing speed, efficiency and accuracy.

    TASK:
    Expand the following outline into
    a complete well structured article.
    Outline: {outline}

    CONSTRAINTS:
    - Do not make up facts, details or events, If you don't know "say I don't know"
    - Keep conversation/writeup within the outline
    - Keep writeup within the tone: {tone} and audience: {audience}
    - Avoid unnecessary edge cases
    - Keep it concise and striaght to point
    - Avoid cliches and unnecessary academic words

    OUTPUT:
    Format the output according to the format type: {format_type}
    Use bullet points where necessary.
    """

    return ask_gemini(prompt)