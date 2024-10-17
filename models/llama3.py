import os
from together import Together

# Setup client
client = Together()

def clean_data_with_llama3(text: str):
    prompt = f"""
    Rewrite the following paragraph(s) word for word except: (i) removing the periods from *all* abbreviations (for example: "e.g." becomes eg, "i.e." becomes ie, Mr. becomes Mr); (ii) removing brief parentheticals such as “(emphasis deleted)” “(emphasis added)” “(cleaned up)” “(STEVENS, J, dissenting)” (iii) replacing *all* citations with "[citation]" (example: "Smith v. Jones, 666 F.3d 18, 21-23 (C.A.1 2000)." becomes "[citation].") (example: “Ante, at 1341 (internal quotation marks omitted).” becomes "[citation].") (example: "in the earlier case of Western Union Telegraph Co. v. Pennsylvania, 368 U.S. 71, 72, 82 S.Ct. 199, 7 L.Ed.2d 139 (1961), we held" becomes "in the earlier case of [citation], we held") (example: "see, eg, Smith Co., 123 US, at 999, 135 S.Ct. 7807" becomes "[citation]") (example: "Smith v. Jones 123 F.3d. 45, 48 (C.A.9 2005)(In the end we are all goldfish.)" becomes [citation] In the end we are all goldfish."; (iv) all references to statutes become just “[statute]” (example “Copyright Act of 1976, 17 U. S. C. § 107 (1988 ed. and Supp. IV).” becomes "[statute].") (example: “§ 107(1)F” becomes "[statute]")(example: "Art. I, ¬ß 10, cl. 2." becomes "[statute]."; (iv) all footnotes in the form “[12]” become simply “[footnote]” (example: "The department did not respond.[3]” becomes “The department did not respond.[footnote]”. Final notes: Don't write [citation] or [statute] if there is no citation or statute. Don’t paraphrase. Don’t begin with “Text:” just give me the text. Try to preserve the periods at the end of sentences:
    
    {text}
    """

    # Use Together to process the data
    response = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        messages=[{"role": "user", "content": prompt}],
        stream=False  # No need to stream for this task
    )

    result = response.choices[0].message.content

    return result


def count_sentences_with_llama3(text: str):
    prompt = f"""
        Please analyze the following text and return the number of sentences, ignoring any citations, abbreviations, page numbers, or any extraneous information.

        Text: {text}

        Response format: Provide only a single integer representing the number of sentences, with no additional commentary, explanations, or formatting.

        Important: The response should be a plain integer and nothing else.
    """

    # Use Together to process the data
    response = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        messages=[{"role": "user", "content": prompt}],
        stream=False  # No need to stream for this task
    )

    result = response.choices[0].message.content

    return result



# # Example usage
# text_sample = "This is a test paragraph. Mr. John Smith said, 'It's great!' See Smith v. Jones, 123 F.3d 45 (1999)."

# cleaned_text = clean_data_with_llama3(text_sample)
# sentence_count = count_sentences_with_llama3(text_sample)

# print(f"Cleaned Text: {cleaned_text}")
# print(f"Sentence Count: {sentence_count}")
