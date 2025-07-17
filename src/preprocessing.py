import re

def clean_html_text(data: str) -> str:
    """Remove HTML tags from text."""
    html_pattern = re.compile(r"<.*?>")
    return re.sub(html_pattern, " ", data)

def preprocess_text(data: str) -> str:
    """Lowercase, remove HTML and extra spaces."""
    data = clean_html_text(data)
    data = data.lower()
    data = re.sub(r"[^a-zA-Z0-9\s]", "", data)  # remove special chars
    data = re.sub(r"\s+", " ", data).strip()    # normalize whitespace
    return data
