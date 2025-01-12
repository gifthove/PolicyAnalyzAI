from bs4 import BeautifulSoup

def clean_html(html_content):
    """
    Extracts and cleans text content from an HTML document.
    
    Args:
        html_content (str): The raw HTML content as a string.
        
    Returns:
        str: Cleaned plain text content.
    """
    soup = BeautifulSoup(html_content, "html.parser")

    # Remove script and style elements
    for script_or_style in soup(["script", "style"]):
        script_or_style.decompose()

    # Extract text and normalize spaces
    text = soup.get_text(separator=" ").strip()
    return ' '.join(text.split())
