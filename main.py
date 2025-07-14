import os
from helper import get_openai_api_key
from openai import OpenAI
from pydantic import BaseModel
from typing import Optional

KEY = get_openai_api_key()

# How to Use Structured Outputs
client = OpenAI(
    api_key=KEY
)

# Define structure with Pydantic
class User(BaseModel):
    name: str
    age: int
    email: Optional[str] = None

completion = client.beta.chat.completions.parse(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Make up a user."},
    ],
    response_format=User,
)
user = completion.choices[0].message.parsed
print(user)