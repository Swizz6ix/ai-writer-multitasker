from create_article import create_article
import streamlit as st
from gemini_client import ask_gemini
from prompt_builder import build_prompt

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


progress = st.progress(0)

# Generate Button
if st.button("Generate Content"):
    if not user_input.strip():
        st.warning("Please enter some content.")
    else:
        with st.spinner("Generating..."):
            prompt = build_prompt(user_input, tone, audience, format_type)
            results = create_article(prompt, tone)

        st.subheader("Outline")
        st.write(results["outline"])
        progress.progress(25)

        st.subheader("Draft")
        st.write(results["draft"])
        progress.progress(50)

        st.subheader("Final Version")
        st.write(results["final"])
        progress.progress(100)