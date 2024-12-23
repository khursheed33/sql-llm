import pandas as pd
import json

# Path to your CSV file
csv_path = "data.csv"  # Replace with your CSV file path
jsonl_path = "output.jsonl"   # Desired output JSONL file path

# Load CSV
df = pd.read_csv(csv_path)

# Convert DataFrame to JSONL
with open(jsonl_path, 'w', encoding='utf-8') as jsonl_file:
    for record in df.to_dict(orient='records'):
        jsonl_file.write(json.dumps(record, ensure_ascii=False) + '\n')

print(f"JSONL file saved to {jsonl_path}")
