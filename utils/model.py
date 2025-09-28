from openai import OpenAI
from dotenv import load_dotenv

import os
import tiktoken

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
encoding = tiktoken.get_encoding("cl100k_base")

prompt = """Generate a modern, visually appealing website layout using only HTML code.
            Requirements:
            - Do NOT include <!DOCTYPE html>, <html>, or <body> tags. I will insert this into the body of my page.
            - Use the Inter font (assume it is already loaded).
            - You can use tailwind classes i imported them via the cdn
            - USE ONLY GOOGLE FONTS
            - Create a clean, professional layout with good spacing, rounded corners, and modern typography.
            - Include multiple sections such as:
            - A navbar with  navigation links.
            - A hero section with a headline, subheading, and call-to-action button.
            - A features section with cards or icons.
            - A testimonial or quote section.
            - A call-to-action section near the bottom.
            - A footer with copyright text and social links.
            - Make it fully responsive and visually balanced.
            - NO IMAGES only icons please
            - You only have 2000 tokens so make use of this
            - Focus on aesthetic design: use good color contrast, whitespace, and consistent spacing.
            - Do not include any explanations or comments. Output only the raw HTML code.
            - Make it long and detailed — generate enough content to produce a realistic, complete landing page.
        """

def generate():
    response = client.responses.create(
        model="o3",  # ✅ switch to gpt-4o (or gpt-4.1 / gpt-4o-mini)
        input=prompt,
        max_output_tokens=2000
    )
    tokens = encoding.encode(response.output_text)
    print(len(tokens))
    return response.output_text