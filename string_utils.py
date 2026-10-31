"""String utility functions."""

import re

def slugify(text: str) -> str:
    """Convert text to URL-friendly slug."""
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    return re.sub(r'[-\s]+', '-', text)

def truncate(text: str, max_length: int = 50, suffix: str = "...") -> str:
    """Truncate text to max_length with suffix."""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix
