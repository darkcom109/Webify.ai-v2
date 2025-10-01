# utils/model.py
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate(user_prompt: str):
    response = client.responses.create(
        model="o3",  # or o3 with reasoning params
        input=f"""
            Generate a modern, Tailwind-styled HTML page based on this request: {user_prompt}.
            Use google fonts
            Do NOT include <!DOCTYPE>, <html>, or <body> tags, and do not include '''html and ''' at the end AS IF YOUR LIFE DEPENDED ON IT.
            Output only HTML code for the body content.
            """,
        max_output_tokens=9999,
        reasoning={"effort": "high"}
    )
    if response.output_text[0:7] == "```html":
        return response.output_text[7:len(response.output_text) - 3]
    return response.output_text
