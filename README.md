# PolicyAnalyzAI
PolicyAnalyzAI addresses one critical challenge: the management of large, constantly changing policy landscapes by big institutions. By automating policy analysis, this system helps large organizations enhance regulatory compliance

## 📖 Project Overview

**PolicyAnalyzAI** is an intelligent data pipeline that scrapes, processes, and analyzes university policy documents. The project uses a fine-tuned **GPT-2** language model to identify inconsistencies and provide summaries of policies in alignment with the **University of Otago’s Policy Framework**. 
By leveraging **Large Language Models (LLMs)** like **GPT-2**, along with **Exploratory Data Analysis (EDA)**, this system enhances **policy accessibility**, identifies **redundancies**, and **detects structural inconsistencies**.

### Key Features:
- 🕸️ **Web Scraping:** Automates the extraction of policy documents.  
- 🧹 **Data Preprocessing:** Cleans and tokenizes raw text for model training.  
- 🤖 **Model Fine-Tuning:** Customizes GPT-2 on institutional policies. Trains AI for policy document analysis.   
- 📊 **Exploratory Data Analysis (EDA):** Visualizes key insights from data.  
- ✅ **Model Testing:** Validates the model on real-world prompts.  

---

### **Step 1️⃣: Clone the Repository**
```bash
git clone https://github.com/gifthove/PolicyAnalyzAI.git
cd PolicyAnalyzAI
```


### **Step 2️⃣: Install Dependencies** 
Run the following command to install all required libraries:
```bash
pip install -r requirements.txt
```
If you encounter a Rust & Cargo error, install Rust:
```bash
winget install --id Rustlang.Rustup
```
This will display an interactive menu for running different components of the system.

### **🚀 Running PolicyAnalyzAI**
After installation, run main.py to start the console interface:
### 
If you encounter a Rust & Cargo error, install Rust:
```bash
python main.py
```

### **🕵 How Each Step Works**
### 1️⃣ Web Scraping & Preprocessing
- ✔ Extracts policy documents from the University of Otago’s website.
- ✔ Cleans data, removing HTML tags and redundant text.
- ✔ Tokenizes text for easier processing.
- ✔ Indexes documents for fast searches.

**📂 Files generated:**
```bash
data/raw/ → Stores original policy HTML files.
data/processed/ → Saves cleaned and tokenized policy data
``` 
Run via console (main.py → Option 1)

### 2️⃣ Fine-Tuning the GPT-2 Model
- ✔ Trains GPT-2 on institutional policy language.
- ✔ Optimizes summarization and flaw detection.

**💾 Output Model Location:**

```bash
models/fine_tuned_model/
``` 
⏯ Run via console (main.py → Option 2)

This script tests how well the model understands and summarizes policy content. Example prompts include:


### 3️⃣ Model Testing: Evaluating Policy Analysis Accuracy
- ✔ Tests model-generated summaries for relevance and clarity.
- ✔ Evaluates flaw detection accuracy in policies.
- ✔ Uses cosine similarity & scoring metrics to validate responses.

**📌 Example Evaluation Metrics:**

Prompt	Relevance (out of 10)	Coherence (out of 10)	Flaw Detection Accuracy (out of 10)	Readability Score
Explain the privacy policy in simple terms	5.6	5.03	6.46	55.17
Summarize the terms and conditions of use	2.06	5.23	5.26	29.79

Export to Sheets
⏯ Run via console (main.py → Option 3) 

```bash
"Explain the privacy policy in simple terms."
"Summarize the data protection policy."


PS C:\Developmentpython test_fine_tuned_model.pyng
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