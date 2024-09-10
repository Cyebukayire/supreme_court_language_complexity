```markdown
# Supreme Court Language Analysis

This project analyzes the **language used in Supreme Court oral arguments and opinions** to study how it has changed over time. The main focus is on measuring the complexity of language using:

- **Sentence length**
- **Word length**
- **Vocabulary sophistication**

The project uses different NLP tools to clean and preprocess the text data, removing irrelevant information, and then computes metrics like the number of sentences and word length.

## Installation and Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/Cyebukayire/supreme_court_language_complexity.git
    cd supreme_court_language_complexity/src
    ```

2. Create a Conda environment and install dependencies:

    ```bash
    conda create --name sc_complexity python=3.12
    conda activate sc_complexity
    pip install -r requirements.txt
    ```

3. Run the text processing pipeline:

    ```bash
    python src/data_processing.py
    ```

This will generate a cleaned dataset with added sentence counts and cleaned text.

```