import pandas as pd

def get_dataset(csv_path='data.csv', num_samples=10000):
    """
    Load dataset from a CSV file.
    
    Args:
        csv_path (str): Path to the CSV file. Defaults to 'data.csv' in the root directory.
        num_samples (int): Number of samples to load. Defaults to 10000.
    
    Returns:
        pandas.DataFrame: Loaded dataset
    """
    try:
        # Read the CSV file
        df = pd.read_csv(csv_path)
        
        # Validate columns
        required_columns = ['question', 'query']
        for col in required_columns:
            if col not in df.columns:
                raise ValueError(f"CSV must contain a '{col}' column")
        
        # Limit number of samples if needed
        if num_samples < len(df):
            df = df.head(num_samples)
        
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def prepare_data(dataset):
    """
    Prepare data for model training by formatting prompts.
    
    Args:
        dataset (pandas.DataFrame): Dataframe with 'question' and 'query' columns
    
    Returns:
        list: Formatted text prompts
    """
    output_texts = []
    for _, row in dataset.iterrows():
        text = f""" 
        Act as an assistant to a software engineer who is writing SQL query codes: 
        {row['question']}\n ### The response query is: {row['query']}
        """
        output_texts.append(text)
    return output_texts
