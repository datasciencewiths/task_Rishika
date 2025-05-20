import streamlit as st
import requests

st.set_page_config(page_title="AI Prompt Styles", layout="wide")

user_id = "test_user_001"
st.title("AI Stylist: Casual vs Formal")
query = st.text_input("Ask anything:")

if st.button("Generate"):
    with st.spinner("Generating responses..."):
        resp = requests.post("http://localhost:8000/generate", json={"user_id": user_id, "query": query})
        if resp.status_code == 200:
            data = resp.json()
            st.subheader("🎈 Casual Response")
            st.write(data["casual_response"])
            st.subheader("📚 Formal Response")
            st.write(data["formal_response"])
        else:
            st.error("Failed to generate responses.")

st.sidebar.title("History")
history = requests.get(f"http://localhost:8000/history", params={"user_id": user_id}).json()
for h in history:
    with st.sidebar.expander(h["query"]):
        st.markdown(f"**Casual:** {h['casual_response']}")
        st.markdown(f"**Formal:** {h['formal_response']}")