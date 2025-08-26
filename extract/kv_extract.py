import re

def extract_key_values(text):
    """
    Extracts key-value pairs (useful for forms and bills).
    Looks for patterns like: Key: Value or Key = Value
    """
    kv_pairs = {}
    for line in text.split("\n"):
        if ":" in line:
            parts = line.split(":", 1)
            kv_pairs[parts[0].strip()] = parts[1].strip()
        elif "=" in line:
            parts = line.split("=", 1)
            kv_pairs[parts[0].strip()] = parts[1].strip()
    return kv_pairs
