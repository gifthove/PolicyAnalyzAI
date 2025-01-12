import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load the fine-tuned model and tokenizer
model_path = "policy_scraper/fine_tuning/fine_tuned_model"
print(f"Loading fine-tuned model from {model_path}...")
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path)

# Add padding token if it doesn't exist
if tokenizer.pad_token is None:
    tokenizer.add_special_tokens({'pad_token': tokenizer.eos_token})
    model.resize_token_embeddings(len(tokenizer))

def test_model(prompt):
    """
    Function to generate a response from the fine-tuned model for a given prompt.
    """
    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=512,
    )
    
    outputs = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=150,  # Shorter max length
        do_sample=True,  # Sampling for diversity
        temperature=0.6,  # Adjusted temperature
        top_p=0.9,  # Nucleus sampling
        repetition_penalty=1.2,  # Penalize repetition
        pad_token_id=tokenizer.pad_token_id,  # Ensure padding is handled
    )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

def summarize_document(file_path):
    """
    Reads a document and generates a summary or response for its content.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            document_content = file.read()
        print(f"\nGenerating response for document: {file_path}\n")
        response = test_model(f"Summarize this document: {document_content}")
        print(f"Response: {response}\n")
    except Exception as e:
        print(f"Error reading document: {e}")

# Test the fine-tuned model with prompts
print("Testing Fine-Tuned Model...\n")

# Prompts for testing
test_prompts = [
    "Explain the privacy policy in simple terms:",
    "What are the key principles of data protection?",
    "Summarize the terms and conditions of use:",
]

for prompt in test_prompts:
    print(f"Prompt: {prompt}")
    response = test_model(prompt)
    print(f"Response: {response}\n")


