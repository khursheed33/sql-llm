from datasets import load_dataset



def get_dataset():
    dataset = load_dataset(path="train.jsonl")
    print("Data: ", dataset)
    return dataset

def prepare_data(example):
    output_texts = []
    for i in range(len(example['query'])):
        text = f""" 
        Act as an assistant to a software engineer who is writing SQL query codes: 
        {example['prompt'][i]}\n ### The response query is: {example['query'][i]}
        """
        output_texts.append(text)
    return output_texts