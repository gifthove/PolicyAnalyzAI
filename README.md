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
After scraping, the data goes through several automated processing steps handled by the Scrapy pipelines. This processing ensures that the scraped content is structured and ready for model training.

**Processing Steps in Pipelines:**
1. Saving Raw HTML

The original scraped HTML is saved in data/raw/policies/.

2. Cleaning the Data
The HTML content is cleaned to remove unwanted tags, scripts, and formatting.
The cleaned text is saved in JSON format in:
```bash
data/processed/clean_json_files/
```

3. Tokenizing the Data:
The cleaned text is tokenized into words and sentences for detailed analysis.
Tokenized data is stored in:
```bash
data/processed/tokenized_json_files/
```

4. Indexing the Data
The cleaned text is indexed using Whoosh to allow for fast content searches.
Indexed data is stored in:
```bash
output/index/
```

5. Downloading and Saving Files (PDFs/Docs)
Downloadable files (e.g., PDFs, Word Docs) linked in the policies are saved into:
```bash
PDFs: data/raw/pdfs/
Other files: data/raw/files/
```
6. Data Consolidation
Cleaned and tokenized data is merged into a single file for training.
Consolidated file:
```bash
data/processed/consolidated_data.json
```


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
```bash
python test_fine_tuned_model.py
```

This script tests how well the model understands and summarizes policy content. Example prompts include:

```bash
"Explain the privacy policy in simple terms."
"Summarize the data protection policy."


PS C:\Developmentpython test_fine_tuned_model.pyng>
Loading fine-tuned model from ../models/fine_tuned_model...
Testing Fine-Tuned Model...

Prompt: Explain the privacy policy in simple terms:
Response: Explain the privacy policy in simple terms: What is your personal information for? How do I use it? Where can I find out more about what you are sharing with us, and how we collect that data. Why should this matter to me? If a user has shared their details online (for example via email or text message), they may wish not to be 
permitted access through our Services; however, if such an action was taken against them by another party who had reasonable grounds for believing there were other users of any particular website involved, then no liability will arise as long after these disclosures have been made – but even where those circumstances prevent some people 
from accessing certain websites at once, actions which could reasonably be expected to result in significant harm cannot normally

Prompt: What are the key principles of data protection?
Response: What are the key principles of data protection? Learn more about how to protect yourself and your personal information Privacy Accessibility Clear search Open menu Close Menu Toggle submenu Are you looking for... Return To previous menu Have a question, answered topic AskOtago Future Students Subjects Fees and scholarships Key 
dates Apply to Otago Academic Divisions Division Of Commerce Division OF Health Sciences Division About the university Residential colleges Otago University Press Library Jobs at Otahau Research DVC's welcome Our people at research and Enterprise OUSA Need help? Emergencies Human Resources Student health Our communities Current students 
Staff Alumni Māori ki Ōtōkou Pacific at Otawa International students Campuses and maps Auckland Centre Christchurch Campus Dunedin Campus Wellington Campus Inver

Prompt: Summarize the terms and conditions of use:
Response: Summarize the terms and conditions of use: The University will not be able to identify a student who is an academic adviser for purposes other than as part-time students. Students should consult with their school representative or contact Student Accommodation Adviser before making any changes, including changing your accommodation arrangements at home (if applicable). To ensure that you are familiar with all relevant policies relating in particular areas, please refer back below for more information on specific policy documents covering these topics. Policy Documents Responsible Officers Information about how university administrators can assist individuals affected by this type/divisional decision under section 4(a) above; Policies concerning research misconduct In relation specifically – when dealing directly with complaints from staff regarding workplace behaviour involving members thereof– it may be helpful
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