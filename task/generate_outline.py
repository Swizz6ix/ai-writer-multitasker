from gemini_client import ask_gemini

def generate_outline(topic):

    prompt = f"""
    Create a detailed outline for:
    {topic}
    
    Include:
    - Introduction
    - Main sections
    - Conclusion

    Return only the outline.
    """

    return ask_gemini(prompt)