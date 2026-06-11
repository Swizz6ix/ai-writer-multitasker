from task import apply_tone, expand_outline, generate_outline, proofread


def create_article(topic, tone):
    outline = generate_outline.generate_outline(topic)
    draft = expand_outline.expand_outline(outline)
    polished = apply_tone.apply_tone(draft, tone)
    final_version = proofread.proofread(polished)
    
    return {
        "outline": outline,
        "draft": draft,
        "final": final_version
    }