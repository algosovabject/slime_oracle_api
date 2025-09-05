import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/oracle/query"

st.title("🔮 Slime Mold Oracle")

question = st.text_input("Ask the Oracle a question:")

if st.button("Consult the Oracle"):
    if question.strip():
        response = requests.post(API_URL, json={"question": question})
        if response.status_code == 200:
            data = response.json()
            st.subheader("Symbols")
            st.write(", ".join(data["symbols"]))
            st.subheader("Interpretation")
            st.write(data["interpretation"])
        else:
            st.error("API error: " + str(response.status_code))
    else:
        st.warning("Please enter a question.")

