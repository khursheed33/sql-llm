# Qwen/Qwen2.5-7B-Instruct
from transformers import AutoTokenizer, AutoModelForCausalLM

def get_qwen_model(model_id = "Qwen/Qwen2.5-7B-Instruct"):
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id)
    return tokenizer, model