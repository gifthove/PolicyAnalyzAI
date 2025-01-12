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


### Cleaning and Tokenizing the Data
After scraping, the HTML content is cleaned to remove unnecessary tags and formatting, and then tokenized into word and sentence tokens.

The cleaned JSON files are saved in: