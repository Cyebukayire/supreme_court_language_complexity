from models import openai
import pandas as pd

# Load the dataset
input_file = 'data/updated_casetext2022_for_gpt.csv'
output_file = 'data/new_processed_152_rows_with_gpt_4_casetext2022.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(input_file)

# Apply to only first 10 rows
df = df.iloc[52:202]

# Initialize columns for the processed data
df['n_sentence'] = 0
df['llm_text'] = ""

# Process each cell in the 'text' column
def process_cell(text):
    if len(text) > 2:  # Skip text cells of two characters or fewer
        cleaned_text = openai.clean_data_with_gpt_4(text)
        sentence_count = openai.count_sentences_with_gpt_4(text)
        return sentence_count, cleaned_text
    return 0, ""  # Default values for skipped cells

# Apply the processing function to the 'text' column
df[['n_sentence', 'llm_text']] = df['text'].apply(lambda text: pd.Series(process_cell(text)))

# Save the processed DataFrame to a new CSV file
# df.to_csv(output_file, mode='a', header =False, index=False)
df.to_csv(output_file, index=False)
print(f"Processed data has been appended to {output_file}.")

""""
TODO:
Process and append next 150 rows to processed data file
Research about Llama3
"""