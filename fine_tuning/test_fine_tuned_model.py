import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load the fine-tuned model and tokenizer
model_path = "../models/fine_tuned_model"
print(f"Loading fine-tuned model from {model_path}...")
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path)

# Add padding token if it doesn't exist
if tokenizer.pad_token is None:
    tokenizer.add_special_tokens({'pad_token': tokenizer.eos_token})
    model.resize_token_embeddings(len(tokenizer))

def test_model(prompt):
    """
    Generate a response from the fine-tuned model for a given prompt.
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
        max_length=150,
        do_sample=True,
        temperature=0.6,
        top_p=0.9,
        repetition_penalty=1.2,
        pad_token_id=tokenizer.pad_token_id,
    )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

def evaluate_response(prompt, response):
    """
    Evaluate the model's response for coherence, relevance, and ability to detect flaws.
    """
    # Assign example scores for evaluation
    relevance_score = 8  # Example: Replace with evaluation after response review
    coherence_score = 9  # Example: Replace with evaluation after response review
    flaw_detection_score = 7  # Example: Replace with evaluation after response review
    
    print(f"Prompt: {prompt}")
    print(f"Response: {response}\n")
    print("Evaluation:")
    print(f" - Relevance: [ ]")
    print(f" - Coherence: [ ]")
    print(f" - Flaw Detection Accuracy: [ ]\n")

# Testing prompts
prompts = [
    # Initial testing prompts
    "Explain the privacy policy in simple terms:",
    "What are the key principles of data protection?",
    "Summarize the terms and conditions of use:",
    
    # Specific prompts for policy flaw detection
    "Analyze if this policy contains unnecessary cross-references or redundant content: The policy states that staff must comply with the law, and they must refer to the Code of Conduct for further guidance.",
    "Does this policy contain procedural content? The policy specifies that all complaints should be directed to HR via email and follow a 3-step escalation process.",
    "Identify inconsistencies in this policy: The Privacy Policy mentions compliance with GDPR but does not outline how consent is obtained for data processing. It also includes unrelated information about AI usage.",
    "Is this policy structured correctly? The policy repeats the same information about grievance handling in two separate sections.",
]

# Run the model on each prompt
print("Testing Fine-Tuned Model...\n")
for prompt in prompts:
    response = test_model(prompt)
    evaluate_response(prompt, response)
