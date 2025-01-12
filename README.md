# PolicyAnalyzAI
PolicyAnalyzAI addresses one critical challenge: the management of large, constantly changing policy landscapes by big institutions. By automating policy analysis, this system helps large organizations enhance regulatory compliance

## 📖 Project Overview

**PolicyAnalyzAI** is an intelligent data pipeline that scrapes, processes, and analyzes university policy documents. The project uses a fine-tuned **GPT-2** language model to identify inconsistencies and provide summaries of policies in alignment with the **University of Otago’s Policy Framework**.

### Key Features:
- 🕸️ **Web Scraping:** Automates the extraction of policy documents.  
- 🧹 **Data Preprocessing:** Cleans and tokenizes raw text for model training.  
- 🤖 **Model Fine-Tuning:** Customizes GPT-2 on institutional policies.  
- 📊 **Exploratory Data Analysis (EDA):** Visualizes key insights from data.  
- ✅ **Model Testing:** Validates the model on real-world prompts.  

---
### Setting up and Running 
git clone https://github.com/gifthove/PolicyAnalyzAI.git
cd PolicyAnalyzAI


**Command to run the scraper:**
```bash
cd policy_scraper
scrapy crawl policy_spider
```

**Cleaning and Tokenizing the Data:**
After scraping, the HTML content is cleaned to remove unnecessary tags and formatting, and then tokenized into word and sentence tokens.

The cleaned JSON files are saved in:
```bash
data/processed/clean_json_files/
```

**Tokenized data is stored in:**

```bash
data/processed/tokenized_json_files/
```
**Consolidating the Data:**
Both the cleaned and tokenized files are consolidated into a single dataset for easy processing. The consolidated JSON is saved to:

```bash
data/processed/consolidated_data.json
```

This step ensures that all the relevant content is ready for fine-tuning the language model.


**Fine-Tuning the GPT-2 Model:**
The cleaned and consolidated data is used to fine-tune a GPT-2 model using Hugging Face's Transformers library.

Command to run fine-tuning:

```bash
cd fine_tuning
python llm_fine_tuning.py
```
The fine-tuned model is saved to:

```bash
models/fine_tuned_model/
```

**Testing the Fine-Tuned Model:**
I created a script to test the model's performance by running prompts and evaluating the generated responses.

Command to run testing:
Command to run testing:

```bash
python test_fine_tuned_model.py
```

This script tests how well the model understands and summarizes policy content. Example prompts include:

```bash
"Explain the privacy policy in simple terms."
"Summarize the data protection policy."
```

**Exploratory Data Analysis (EDA):**
To gain deeper insights into the structure and content of the scraped data, I performed Exploratory Data Analysis (EDA). This includes:

Word frequency analysis
Sentence length distribution
Keyword clustering

Command to run EDA:

```bash
jupyter notebook
```

Open and run:

```bash
notebooks/eda.ipynb
```

**Interactive Model Testing**
For more in-depth testing, I created a Jupyter notebook to interactively query the fine-tuned model.