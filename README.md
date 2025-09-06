🔮 Slime Mold Oracle API

The Slime Mold Oracle API is a small FastAPI project that blends machine learning aesthetics with occult horror. It accepts a user’s question and returns symbols and an interpretation, like consulting a digital divination system.

This project serves two purposes:

Portfolio Sample – an example of API documentation and technical writing.

Conceptual Experiment – art/tech fusion inspired by philosophy, horror, and the aesthetics of abjection.


🚀 Features

FastAPI backend with auto-generated Swagger and ReDoc docs.

POST /oracle/query endpoint that returns symbols + interpretation.

Example UI (Streamlit) for interacting with the Oracle.


📖 Documentation

Full API reference (with request/response examples) is available here:
👉 Slime Mold Oracle API Reference

Screenshots of the live docs (Swagger UI & ReDoc) can be found in /images/.


🧪 Run Locally

# Install dependencies
pip install -r requirements.txt

# Start the API
uvicorn main:app --reload

# Visit Swagger UI
http://127.0.0.1:8000/docs


⚠️ Note

This project is not a production service. It’s a writing + technical demo to showcase API documentation and playful horror aesthetics.


🕷️ “The mold whispers… but do you listen?”