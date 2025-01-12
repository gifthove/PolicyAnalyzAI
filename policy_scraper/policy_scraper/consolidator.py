import os
import json

def consolidate_data(clean_dir="data/processed/clean_json_files", 
                     tokenized_dir="data/processed/tokenized_json_files", 
                     output_file="data/processed/consolidated_data.json"):
    """
    Consolidates cleaned and tokenized data into a single dataset.

    Args:
        clean_dir (str): Directory containing cleaned JSON files.
        tokenized_dir (str): Directory containing tokenized JSON files.
        output_file (str): Output file for the consolidated dataset.
    """
    consolidated_data = []

    try:
        # Get filenames in both directories
        clean_files = {f for f in os.listdir(clean_dir) if f.endswith(".json")}
        tokenized_files = {f for f in os.listdir(tokenized_dir) if f.endswith(".json")}

        # Intersect filenames to ensure matching pairs
        common_files = clean_files & tokenized_files

        for filename in common_files:
            # Load cleaned data
            clean_path = os.path.join(clean_dir, filename)
            with open(clean_path, "r", encoding="utf-8") as f:
                cleaned_data = json.load(f)

            # Load tokenized data
            tokenized_path = os.path.join(tokenized_dir, filename)
            with open(tokenized_path, "r", encoding="utf-8") as f:
                tokenized_data = json.load(f)

            # Consolidate data
            consolidated_entry = {
                "title": cleaned_data["title"],
                "url": cleaned_data["url"],
                "cleaned_content": cleaned_data["cleaned_content"],
                "word_tokens": tokenized_data["word_tokens"],
                "sentence_tokens": tokenized_data["sentence_tokens"],
            }

            consolidated_data.append(consolidated_entry)

        # Save consolidated data
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(consolidated_data, f, ensure_ascii=False, indent=4)

        print(f"Consolidated data saved to {output_file}")

    except Exception as e:
        print(f"Error consolidating data: {e}")

