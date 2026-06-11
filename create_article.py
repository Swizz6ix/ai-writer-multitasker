from task import apply_tone, expand_outline, generate_outline, proofread
import streamlit as st

progress_text = "Drafting.."
progress = st.progress(0)

def create_article(topic, tone):
    outline = generate_outline.generate_outline(topic)
    progress.progress(25)

    draft = expand_outline.expand_outline(outline)
    progress.progress(50)
    
    polished = apply_tone.apply_tone(draft, tone)
    progress.progress(75)

    final_version = proofread.proofread(polished)
    progress.progress(100)
    
    return {
        "outline": outline,
        "draft": draft,
        "polished": polished,
        "final": final_version
    }