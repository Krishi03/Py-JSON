import re

def get_research_paper_sections():
    return {
        'abstract': r'^(?:ABSTRACT|Abstract)',
        'introduction': r'^(?:INTRODUCTION|Introduction|1\.?\s*Introduction)',
        'objectives': r'^(?:OBJECTIVES|Objectives|Goals|Aims)',
        'related_work': r'^(?:RELATED\s+WORK|Related\s+Work|Literature\s+Review)',
        'methodology': r'^(?:METHODOLOGY|Methodology|Proposed\s+Framework)',
        'implementation': r'^(?:IMPLEMENTATION|Implementation|System\s+Design)',
        'results': r'^(?:RESULTS|Results|DISCUSSION|Discussion)',
        'conclusion': r'^(?:CONCLUSION|Conclusion)',
        'references': r'^(?:REFERENCES|References|Bibliography)',
        'acknowledgement': r'^(?:ACKNOWLEDGEMENT|Acknowledgements?)'
    }

def split_by_headline(text):
    sections = {}
    current_headline = "Introduction"
    sections[current_headline] = ""
    
    lines = text.split("\n")
    i = 0
    
    # Get research paper section patterns
    paper_sections = get_research_paper_sections()
    
    while i < len(lines):
        line = lines[i].strip()
        
        if not line:
            i += 1
            continue
            
        is_headline = False
        
        # Check for research paper sections
        for section_name, pattern in paper_sections.items():
            if re.match(pattern, line):
                is_headline = True
                current_headline = line
                break
        
        # Check other headline patterns if not a research section
        if not is_headline:
            if re.match(r"^[A-Z][A-Z\s0-9]{3,}$", line):
                is_headline = True
            elif re.match(r"^\d+(\.\d+)*\s+\S", line):
                is_headline = True
            elif re.match(r"^[IVXLCDM]+\.\s+\S", line):  # Roman numerals
                is_headline = True
            elif re.match(r"^[A-Z](\.|:)\s+\S", line):  # Capital letters
                is_headline = True
            elif (line.istitle() and len(line) > 10 and 
                  (i == 0 or not lines[i-1].strip()) and 
                  (i == len(lines)-1 or not lines[i+1].strip())):
                is_headline = True
            
        if is_headline:
            current_headline = line
            sections[current_headline] = ""
        else:
            sections[current_headline] += line + " "
            
        i += 1
    
    for headline in sections:
        sections[headline] = sections[headline].strip()
        
    return sections
