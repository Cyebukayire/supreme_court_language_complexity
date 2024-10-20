from models import openai, llama3
import pandas as pd

# Load the dataset
input_file = 'data/casetext2022_for_gpt.csv'
output_file = 'data/new_processed_200_300_rows_with_Llama_3.2_11B_Vision_Instruct_Turbo_casetext2022_v2.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(input_file)

# Apply to only first 10 rows
df = df.iloc[200:301]

# Initialize columns for the processed data
df['n_sentence'] = 0
df['llm_text'] = ""

# Process each cell in the 'text' column
def process_cell(text):
    if len(text) > 2:  # Skip text cells of two characters or fewer
        # cleaned_text = openai.clean_data_with_gpt_4(text)
        # sentence_count = openai.count_sentences_with_gpt_4(text)
        cleaned_text = llama3.clean_data_with_llama3(text)
        sentence_count = llama3.count_sentences_with_llama3(text)
        return sentence_count, cleaned_text
    return 0, ""  # Default values for skipped cells

# Apply the processing function to the 'text' column
df[['n_sentence', 'llm_text']] = df['text'].apply(lambda text: pd.Series(process_cell(text)))

# Save the processed DataFrame to a new CSV file
# df.to_csv(output_file, mode='a', header =False, index=False)
df.to_csv(output_file, index=False)
print(f"Processed data has been appended to {output_file}.")
