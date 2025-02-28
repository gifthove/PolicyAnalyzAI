import os
import subprocess
from fine_tuning.llm_fine_tuning import fine_tune_model, prepare_dataset


def run_policy_scraper():
    """Runs the Scrapy Policy Spider."""
    print("Starting policy scraper...")
    try:
        subprocess.run(["scrapy", "crawl", "policy_spider"], cwd="policy_scraper", check=True)
        print("✅ Policy scraping completed.")
    except Exception as e:
        print(f"❌ Error in policy scraping: {e}")


def run_fine_tuning():
    """Runs the fine-tuning process for GPT-2."""
    print("Starting fine-tuning...")
    try:
        data_file = os.path.join(os.getcwd(), "data", "processed", "consolidated_data.json")
        output_file = os.path.join(os.getcwd(), "fine_tuning", "text_dataset.txt")
        output_dir = os.path.join(os.getcwd(), "models", "fine_tuned_model")
        
        # Prepare dataset and fine-tune
        prepare_dataset(data_file, output_file)
        fine_tune_model(output_file, output_dir)
        print("✅ Fine-tuning completed.")
    except Exception as e:
        print(f"❌ Error in fine-tuning: {e}")


def run_model_testing():
    """Runs the model testing script."""
    print("Starting model testing...")
    try:
        fine_tuning_dir = os.path.join(os.getcwd(), "fine_tuning")
        subprocess.run(["python", "test_fine_tuned_model.py"], cwd=fine_tuning_dir, check=True)
        print("✅ Model testing completed.")
    except Exception as e:
        print(f"❌ Error in model testing: {e}")


def run_eda_notebook():
    """Launches the Exploratory Data Analysis (EDA) Jupyter Notebook."""
    print("Launching EDA notebook...")
    try:
        eda_path = os.path.join(os.getcwd(), "notebooks", "eda.ipynb")
        subprocess.run(["jupyter", "notebook", eda_path], check=True)
        print("✅ EDA notebook launched.")
    except Exception as e:
        print(f"❌ Error launching EDA: {e}")


def main():
    while True:
        print("\n=== PolicyAnalyzAI Console Menu ===")
        print("1. Run Policy Scraper (Includes Preprocessing and Consolidation)")
        print("2. Run Fine-Tuning")
        print("3. Run Model Testing")
        print("4. Run EDA")
        print("5. Exit")
        
        try:
            choice = int(input("Select an option: "))
            if choice == 1:
                run_policy_scraper()
            elif choice == 2:
                run_fine_tuning()
            elif choice == 3:
                run_model_testing()
            elif choice == 4:
                run_eda_notebook()
            elif choice == 5:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
