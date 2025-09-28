from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate():
    response = client.responses.create(
        model="gpt-4o",  # ✅ switch to gpt-4o (or gpt-4.1 / gpt-4o-mini)
        input="Output only html code and generate a modern looking website, do not add comments or explanations"
            "Just the HTML code itself, do not include the <DOCTYPE> etc just the code and i will insert this into the body of my html file"
    )

    return response.output_text[7:len(response.output_text) - 3]