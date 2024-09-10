import os
from dotenv import load_dotenv
from openai import OpenAI
import json

# Load environment variables
load_dotenv()

# Setup client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def process_data(text):
    prompt = f"""
    You are tasked with analyzing the following paragraph. Please provide the following:
    
    1. The total number of sentences, excluding citations, abbreviations, and page numbers.
    2. A cleaned version of the text with all irrelevant content like citations, abbreviations, and page numbers removed.
    
    Return the result in a JSON-like dictionary format with:
    - "sentence_count": [the number of sentences]
    - "cleaned_data": [the cleaned text]
    
    Here's the paragraph: {text}
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
    processed_data = response.choices[0].message.content
    # return processed_data
    
    # Convert the response into a Python dictionary
    try:
        # result = eval(processed_data)  
        result_dict = json.loads(process_data)
        
    except:
        raise ValueError("The response is not in the expected dictionary format: \n", result_dict)
    
    return result_dict

text = "Hello there, the article from, works well. It eraly does. I got the news from News Corp., 235 F.3d 18, 21-23 (C.A.1 2000) which CONFIRMS IT."
print(process_data(text))