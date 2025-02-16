import streamlit as st
import google.generativeai as genai
import os

# Set Gemini API Key
os.environ["GEMINI_API_KEY"] = "AIzaSyBrdSkMThJ0c1gIWVZcydaSHpey8dCO1dQ"  # Replace with your actual API key
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# System prompt for the AI
sys_prompt = """
You are an AI Code Reviewer, an expert in Python code. Review and analyze submitted code to provide:
1. ## 🔹Bug Report: Identify potential bugs, syntax errors, and logical flaws, with explanations.
2. ## 🔹Fixed Code: Suggest corrections or optimizations with explanations.
3. ## 🔹Instruction: Offer helpful, understandable, and concise feedback for developers at all skill levels.
Keep the tone professional, clear, and focused on improving coding practices.
"""

def review_code(code_snippet):
    """Calls Gemini AI model to review the provided code."""
    prompt = f"""
{sys_prompt}

### Submitted Code:
```python
{code_snippet}
```
"""
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text if response else "No response from AI."
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="🤖 AI Code Reviewer", layout="wide")

# Custom CSS for white background and improved UI
st.markdown(
    """
    <style>
        body {
            background-color: #FFFFFF;
            color: #000000;
        }
        .stTextArea, .stButton, .stTitle, .stMarkdown {
            font-family: 'Arial', sans-serif;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🧑‍💻 AI Code Reviewer")
st.markdown(
    """
    <div style="display: flex; align-items: center; justify-content: space-between;">
        <div style="flex: 1; text-align: left;">
            <h1>📝 "Code review is an opportunity to learn and teach."</h1>
            <h4 style="color: gray;">let AI enhance it with expert insights!</h4>
        </div>
        <div style="flex: 1; text-align: right;">
            <img src="https://media.licdn.com/dms/image/v2/D4E12AQF5I_CLljCSMA/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1707967901561?e=1745452800&v=beta&t=3fbDBP6Bt4oHkUrLaCD_ncoho9oQC767_egIR6azTHY" width="400">
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# User input section with code area
code_input = st.text_area("🔹 Paste your code here: ⬇️", height=300, placeholder="# Write or paste your Python code here...")

if st.button("🔍 Review Code"):
    if code_input.strip():
        with st.spinner("⏳Analyzing code..."):
            review_result = review_code(code_input)
        st.subheader("💡 AI Review & Suggestions:")
        st.write(review_result)
    else:
        st.warning("⚠️ Please enter some code for review!")

# Footer
st.markdown("""
    <div class='footer'style='text-align: center;'>
        Developed by <b>Suneel Gangapuram</b> | Built with ❤️ using Streamlit
    </div>
    """, unsafe_allow_html=True)