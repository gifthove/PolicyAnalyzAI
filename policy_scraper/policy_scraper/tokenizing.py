import spacy

# Load the SpaCy language model
nlp = spacy.load("en_core_web_sm")

def tokenize_text(text):
    """
    Tokenizes a given text into words and sentences using SpaCy.
    
    Args:
        text (str): The input text to tokenize.
        
    Returns:
        dict: A dictionary containing word tokens and sentence tokens.
    """
    doc = nlp(text)
    word_tokens = [token.text for token in doc]  # Extract individual words
    sentence_tokens = [sent.text for sent in doc.sents]  # Extract sentences
    return {
        "word_tokens": word_tokens,
        "sentence_tokens": sentence_tokens,
    }

# Example usage for testing
if __name__ == "__main__":
    sample_text = "This is a test sentence. SpaCy makes NLP easy!"
    tokens = tokenize_text(sample_text)
    print("Word Tokens:", tokens["word_tokens"])
    print("Sentence Tokens:", tokens["sentence_tokens"])
