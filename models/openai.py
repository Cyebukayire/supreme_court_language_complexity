import os
from dotenv import load_dotenv
from openai import OpenAI
import json

# Load environment variables
load_dotenv()

# Setup client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def clean_data_with_gpt_4(text: str):
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


def count_sentences_with_gpt_4(text: str):
    prompt = f"""
        Please analyze the following text and return the number of sentences, ignoring any citations, abbreviations, page numbers, or any extraneous information.

        Text: {text}

        Response format: Provide only a single integer representing the number of sentences, with no additional commentary, explanations, or formatting.

        Important: The response should be a plain integer and nothing else.
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
    sentence_count = response.choices[0].message.content.strip()

    # Ensure the response is an integer
    try:
        return int(sentence_count)
    
    except ValueError:
        raise ValueError("GPT-4 did not return a valid integer.")
    

def clean_data_with_gpt_3_5_turbo(text: str):
    prompt = f"""
    Clean the following text by removing all citations, abbreviations, page numbers, and any unnecessary information. 
    Only return the cleaned text with no additional commentary or metadata.

    Text: {text}

    Response format: <cleaned_text>
    """

    # Use GPT-3.5 Turbo to process the data
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    
    # Extract the response from GPT-3.5 Turbo
    cleaned_data = response.choices[0].message.content

    return cleaned_data


def count_sentences_with_gpt_3_5_turbo(text: str):
    prompt = f"""
        Please analyze the following text and return the number of sentences, ignoring any citations, abbreviations, page numbers, or any extraneous information.

        Text: {text}

        Response format: Provide only a single integer representing the number of sentences, with no additional commentary, explanations, or formatting.

        Important: The response should be a plain integer and nothing else.
        """
    
    # Use GPT-3.5 Turbo to process the data
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    
    # Extract the response from GPT-3.5 Turbo
    sentence_count = response.choices[0].message.content.strip()

    # Ensure the response is an integer
    try:
        return int(sentence_count)
    
    except ValueError:
        raise ValueError("GPT-3.5 Turbo did not return a valid integer.")
