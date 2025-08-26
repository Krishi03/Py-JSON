import re

def split_by_headline(text):
    """
    Splits text into sections based on headlines (like in research papers).
    Headlines = lines in ALL CAPS or numbered headings.
    """
    sections = {}
    current_headline = "Introduction"
    sections[current_headline] = ""

    for line in text.split("\n"):
        if re.match(r"^[A-Z][A-Z\s0-9]{3,}$", line.strip()):  # ALL CAPS headlines
            current_headline = line.strip()
            sections[current_headline] = ""
        elif re.match(r"^\d+(\.\d+)*\s", line.strip()):  # Numbered sections like 1.1, 2.0
            current_headline = line.strip()
            sections[current_headline] = ""
        else:
            sections[current_headline] += line + " "

    return sections
