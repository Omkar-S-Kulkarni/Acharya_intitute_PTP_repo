import streamlit as st
import os
from modules.ai_client import ask_model, summarize_text, extract_insights
from modules.utils import save_uploaded_file, read_file_content

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Renewable Energy AI", layout="wide")
UPLOAD_FOLDER = "data"
MODELS = {
    "Phi3 Mini": "phi3:mini",
    "Insights Extractor": "phi3:mini"
}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# ---------------- HEADER ----------------
st.title("🌱 Renewable Energy & Carbon AI Dashboard")

# Sidebar: select AI model
model_choice = st.sidebar.selectbox("Select AI Model", list(MODELS.keys()))

# Tab selection
tab = st.sidebar.radio("Select Task", ["Chat / Q&A", "Upload & Summarize", "Insights"])

# ------------------ Chat / Q&A ------------------
if tab == "Chat / Q&A":
    user_input = st.text_area("Ask AI about renewable energy or carbon emissions:")
    if st.button("Submit"):
        if user_input.strip() == "":
            st.warning("Please enter a question!")
        else:
            with st.spinner("Generating response..."):
                response = ask_model(MODELS.get(model_choice, "phi3:mini"), user_input)
                st.success("✅ Response generated")
                st.write(response)

# ------------------ Upload & Summarize ------------------
elif tab == "Upload & Summarize":
    uploaded_file = st.file_uploader("Upload a CSV or TXT file", type=["csv", "txt"])
    if uploaded_file:
        file_path = save_uploaded_file(uploaded_file, UPLOAD_FOLDER)
        st.success(f"File saved to {file_path}")

        # Read file content
        text_content = read_file_content(file_path)

        if text_content.strip() == "":
            st.warning("Uploaded file is empty.")
        else:
            with st.spinner("Summarizing content..."):
                summary = summarize_text(text_content, model_name=MODELS.get(model_choice, "phi3:mini"))
                st.subheader("📄 Summary")
                st.write(summary)

# ------------------ Insights ------------------
elif tab == "Insights":
    user_input = st.text_area("Provide text, policy, or local data to analyze:")
    if st.button("Generate Insights"):
        if user_input.strip() == "":
            st.warning("Please provide some text or data to analyze!")
        else:
            with st.spinner("Analyzing..."):
                insights = extract_insights(user_input, model_name=MODELS.get(model_choice, "phi3:mini"))
                st.subheader("💡 Key Insights")
                st.text(insights)
