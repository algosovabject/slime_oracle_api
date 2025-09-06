# Slime Mold Oracle API Reference

**Version:** 0.1  
**Base URL:** `http://127.0.0.1:8000`  
**Format:** JSON  
**Spec:** Auto-generated OpenAPI available at `/openapi.json`

---

## Overview

The **Slime Mold Oracle API** accepts human questions and whispers back symbols and interpretations.  
It is written in [FastAPI](https://fastapi.tiangolo.com/) and follows REST conventions.  
Think of it as a fungal divination engine—an experiment in machine intelligence, horror aesthetics, and biological metaphor.

For full interactive docs:  
- Swagger UI: `/docs`  
- ReDoc: `/redoc`

---

## Endpoints

### `GET /`

👁️ **Purpose**: A heartbeat. Confirms the Oracle is alive.  

**Request:**  
```http
GET /


###Response (200):
{
  "message": "Slime Mold Oracle API is alive!"
}
json

POST /oracle/query

🔮 Purpose: Ask the Oracle a question.

Request:

POST /oracle/query
Content-Type: application/json

Body Parameters:

Field	Type	Required	Description
question	string	Yes	The query whispered into the void.


Example Request:

{
  "question": "Will I ever escape this labyrinth?"
}
json

Response (200):

{
  "input": "Will I ever escape this labyrinth?",
  "symbols": ["The Spark of Life", "The Serpent", "The Mirror"],
  "interpretation": "This is a dummy response. Real slime mold magic goes here."
}

json

Notes from the Crypt

Requests must be JSON-formatted.

Responses always include:

input: echo of your question (so you can’t deny you asked it)

symbols: an array of arcane emblems

interpretation: the Oracle’s divinatory output

If you receive silence (error codes), it may mean:

The mold is dormant (server is down)

Your payload was malformed (check JSON format)

Or, the Oracle simply refuses to answer you.


Visual Appendix

Below are example screenshots from the auto-generated documentation:


License of Shadows

This is an experimental artifact, not intended for production use.
The Oracle accepts no responsibility for misinterpretation of its whispers.
All prophecies are for entertainment and abjection only.
