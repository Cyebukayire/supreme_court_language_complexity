import os
from dotenv import load_dotenv
from openai import OpenAI
import json

# Load environment variables
load_dotenv()

# Setup client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def clean_data(text):
    prompt = f"""
    Clean the following text by removing all citations, abbreviations, page numbers, and any unnecessary information. 
    Only return the cleaned text with no additional commentary or metadata.

    Text: {text}

    Response format: <cleaned_text>
    """

    # Use GPT-4 to process the data
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    
    # Extract the response from GPT-4
    cleaned_data = response.choices[0].message.content

    return cleaned_data