import streamlit as st
import time

from gemini_client import ask_gemini
from prompt_builder import build_prompt
from task import apply_tone, expand_outline, generate_outline, proofread

st.set_page_config(page_title="AI Writing Assistant", layout="centered")

st.title("✍️ AI Writing Assistant")

# User Input
user_input = st.text_area("Enter your content or idea:")

# Controls
tone = st.selectbox(
    "Select Tone",
    ["Professional", "Casual", "Persuasive", "Friendly", "Formal"]
)

audience = st.selectbox(
    "Target Audience",
    ["General Public", "Beginners", "Experts", "Business Executives"]
)

format_type = st.selectbox(
    "Content Format",
    ["Email", "Blog Post", "Social Media Post", "Report", "Product Description"]
)

progress_text = f"Drafting {format_type}. Please wait"
progress = st.progress(0, text=progress_text)

# Generate Button
if st.button("Generate Content"):
    if not user_input.strip():
        st.warning("Please enter some content.", icon = "⚠️")
    else:
        with st.spinner("Generating...", show_time=True):
            # time.sleep(30)
            outline = generate_outline.generate_outline(user_input)
            progress.progress(25)
            st.write(f'Getting the outlines for "{user_input}"..')

            draft = expand_outline.expand_outline(outline, tone, audience, format_type)
            progress.progress(50)
            st.write(f"drafting the {format_type}")
    
            polished = apply_tone.apply_tone(draft, tone)
            progress.progress(75)
            st.write(f"Polishing the {format_type}")

            final_version = proofread.proofread(polished, format_type)
            progress.progress(100)
            st.write("Here is the final version")

        list = st.expander("Outline")
        list.write(outline)

        expander = st.expander("Draft")
        expander.write(draft)

        expander = st.expander("Polished")
        expander.write(polished)

        st.subheader("Final Version")
        st.write(final_version)

        st.success("Done!")