import os
from dotenv import load_dotenv
from openai import OpenAI
import json
from datetime import datetime
from scripts.api_usage_log import save_api_log

# Load environment variables
load_dotenv()

# Setup client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def clean_data_with_gpt_4(text: str):
    prompt = f"""
    Rewrite the following paragraph(s) word for word except: (i) removing the periods from *all* abbreviations (for example: "e.g." becomes eg, "i.e." becomes ie, Mr. becomes Mr); (ii) removing brief parentheticals such as “(emphasis deleted)” “(emphasis added)” “(cleaned up)” “(STEVENS, J, dissenting)” (iii) replacing *all* citations with "[citation]" (example: "Smith v. Jones, 666 F.3d 18, 21-23 (C.A.1 2000)" becomes [citation]) (example: “Ante, at 1341 (internal quotation marks omitted).” becomes [citation]) (example: "Western Union Telegraph Co. v. Pennsylvania, 368 U.S. 71, 72, 82 S.Ct. 199, 7 L.Ed.2d 139 (1961)" becomes [citation] (example: see, eg, Smith Co., 123 US, at 999, 135 S.Ct. 7807 becomes [citation]; (iv) all references to statutes become just “[statute]” (for example “Copyright Act of 1976, 17 U. S. C. § 107 (1988 ed. and Supp. IV)” becomes [statute] and “§ 107(1)F” becomes [statute]); all footnotes in the form “[12]” become simply “[footnote]” (example “[3]” becomes “[footnote]”. Do not write [citation] or [statute] if there is no citation or statute. Don’t paraphrase. Don’t begin with “Text:” just give me the text:

    {text}

    Important: The response should be a plain text and nothing else.
    """

    # Use GPT-4 to process the data
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    # Save log history
    save_api_log(data=response.to_dict(), task="clean text")

    # Return clean data
    return response.choices[0].message.content


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

    # Save log history
    save_api_log(data=response.to_dict(), task="count sentences")
    
    # Return sentence count
    return response.choices[0].message.content.strip()
