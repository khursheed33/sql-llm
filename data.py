from datasets import load_dataset, Dataset
import pandas as pd
import json
 
def get_dataset(file_path, file_type):
    """
    Load dataset from local CSV or JSONL file
   
    Parameters:
    file_path (str): Path to the data file
    file_type (str): Either "csv" or "jsonl"
   
    Returns:
    dataset: Dataset object
    """
    if file_type == "csv":
        df = pd.read_csv(file_path)
        dataset = Dataset.from_pandas(df)
   
    elif file_type == "jsonl":
        with open(file_path, 'r') as f:
            data = [json.loads(line) for line in f]
        dataset = Dataset.from_list(data)
   
    else:
        raise ValueError("file_type must be either 'csv' or 'jsonl'")
   
    return dataset
 
def prepare_data(example):
    """
    Prepare data by formatting examples into training text
    """
    output_texts = []
    for i in range(len(example['query'])):
        text = f"""
        Act as an assistant to a software engineer who is writing SQL query codes:
        {example['question'][i]}\n ### The response query is: {example['query'][i]}
        """
        output_texts.append(text)
    return output_texts