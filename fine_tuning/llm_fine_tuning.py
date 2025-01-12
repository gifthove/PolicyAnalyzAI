import os
import json
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments, TextDataset, DataCollatorForLanguageModeling

def prepare_dataset(data_file, output_file):
    """
    Converts consolidated JSON data to a plain text dataset for fine-tuning.
    Args:
        data_file (str): Path to the consolidated JSON file.
        output_file (str): Path to save the plain text dataset.
    """
    with open(data_file, "r", encoding="utf-8") as f:
        consolidated_data = json.load(f)

    with open(output_file, "w", encoding="utf-8") as f:
        for entry in consolidated_data:
            text = entry["cleaned_content"]
            f.write(f"{text}\n\n")  # Add line breaks between documents
    print(f"Dataset saved to {output_file}")

def fine_tune_model(dataset_path, output_dir):
    """
    Fine-tunes GPT-2 using the provided dataset.
    Args:
        dataset_path (str): Path to the text dataset.
        output_dir (str): Directory to save the fine-tuned model.
    """
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")

    # Prepare dataset
    dataset = TextDataset(
        tokenizer=tokenizer,
        file_path=dataset_path,
        block_size=128,
    )

    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False,  # GPT-2 does not use masked language modeling
    )

    # Training arguments
    training_args = TrainingArguments(
        output_dir=output_dir,
        overwrite_output_dir=True,
        num_train_epochs=3,
        per_device_train_batch_size=8,
        save_steps=500,
        save_total_limit=2,
        prediction_loss_only=True,
    )

    # Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=dataset,
    )

    trainer.train()
    trainer.save_model()
    tokenizer.save_pretrained(output_dir)
    print(f"Fine-tuned model saved to {output_dir}")

# if __name__ == "__main__":
#     # Paths
#     consolidated_data = "policy_scraper/consolidated_data.json"
#     text_dataset = "policy_scraper/fine_tuning/text_dataset.txt"
#     fine_tuned_model_dir = "policy_scraper/fine_tuning/fine_tuned_model"

    # Prepare dataset and fine-tune
    prepare_dataset(consolidated_data, text_dataset)
    fine_tune_model(text_dataset, fine_tuned_model_dir)

if __name__ == "__main__":
    # Correct Paths in the Project Structure
    consolidated_data = "data/processed/consolidated_data.json"
    text_dataset = "fine_tuning/text_dataset.txt"
    fine_tuned_model_dir = "models/fine_tuned_model"

    # Prepare dataset and fine-tune
    prepare_dataset(consolidated_data, text_dataset)
    fine_tune_model(text_dataset, fine_tuned_model_dir)

