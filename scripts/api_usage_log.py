import json
from datetime import datetime
import os

# Path to log file 
path = os.path.join("data")
LOG_FILE = os.path.join(path, 'api_usage_log.json')

# Pricing variables
COST_PER_1K_TOKENS_INPUT = 0.03  # $0.03 per 1,000 tokens (input)
COST_PER_1K_TOKENS_OUTPUT = 0.06  # $0.06 per 1,000 tokens (output)

# Initialize the JSON log file if it doesn't exist
def initialize_log():
    # Creat data folder if it's doesn't exist
    if not os.path.exists(path):
        os.makedirs(path)

    # Check if the log file exists
    if not os.path.isfile(LOG_FILE):
        # Define the initial structure for the log file
        initial_structure = {
            "gpt-4": {
                "log_requests": [],
                "total_count": {
                "total_number_of_requests":0,
                "total_input_tokens": 0,
                "total_output_tokens": 0,
                "total_tokens": 0,
                "total_cost": 0
                }
            }
        }

        # Write the initial structure to the log file
        with open(LOG_FILE, 'w') as file:
            json.dump(initial_structure, file, indent=4)

# Function to read JSON data from the log file
def read_log_file(file_path):
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    else:
        raise FileNotFoundError("File doens't exit: {LOG_FILE}")
    
# Method to save api's log history
def save_api_log(data:dict, task:str):
    # Check log file
    initialize_log()

    # Extract log details
    timestamp = datetime.fromtimestamp(data['created']).isoformat() + "Z"
    model = data['model']
    request_id = data['id']
    model_usage = data['usage']
    prompt_tokens = model_usage['prompt_tokens']
    response_tokens = model_usage['completion_tokens']
    total_tokens = model_usage['total_tokens']

    # Calculate cost based on the model and pricing details
    if model.startswith("gpt-4"):
        api = "gpt-4"
        prompt_cost = prompt_tokens / 1000 * COST_PER_1K_TOKENS_INPUT
        sampled_cost = response_tokens / 1000 * COST_PER_1K_TOKENS_OUTPUT

    else:
        raise ValueError("Log not recorded, model name: ", model)

    total_cost = prompt_cost + sampled_cost
    total_tokens = prompt_tokens + response_tokens

    # Prepare the data
    log_request = {
        "request_id":request_id,
        "timestamp": timestamp,
        "model": model,
        "request_id": request_id,
        "task":task,
        "input_tokens": prompt_tokens,
        "output_tokens": response_tokens,
        "total_tokens": total_tokens,
        "cost": total_cost,
    }

    # Record log data
    df = read_log_file(LOG_FILE)
    df[api]["log_requests"].append(log_request)
    df[api]["total_count"]["total_number_of_requests"] += 1
    df[api]["total_count"]["total_input_tokens"] += log_request["input_tokens"]
    df[api]["total_count"]["total_output_tokens"] += log_request["output_tokens"]
    df[api]["total_count"]["total_tokens"] += log_request["total_tokens"]
    df[api]["total_count"]["total_cost"] += log_request["cost"]

    # Save records
    with open(LOG_FILE, 'w') as log:
        json.dump(df, log, indent=4)

    return True
