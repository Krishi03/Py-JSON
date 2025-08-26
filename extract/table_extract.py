import re

def extract_tables(text):
    """
    Dummy table extractor:
    For simplicity, treat multiple spaces as column separators.
    """
    tables = []
    for line in text.split("\n"):
        if re.search(r"\s{2,}", line):  # multiple spaces → possible table row
            row = [col.strip() for col in line.split("  ") if col.strip()]
            if len(row) > 1:
                tables.append(row)
    return tables
