import re

def extract_tables(text):
    """
    Enhanced table extractor:
    Detects tables based on consistent column alignment and structure.
    """
    lines = text.split("\n")
    tables = []
    current_table = []
    in_table = False
    
    # Look for potential table rows
    for i, line in enumerate(lines):
        # Skip empty lines
        if not line.strip():
            if in_table and current_table:
                tables.append(current_table)
                current_table = []
                in_table = False
            continue
        
        # Detect table rows by looking for aligned columns
        columns = re.findall(r'(\S+(?:\s+\S+)*)\s{2,}', line + "  ")
        
        # If we have multiple columns, this might be a table row
        if len(columns) >= 2:
            # If this is the first row of a potential table
            if not in_table:
                in_table = True
                current_table = []
            
            # Add the row to the current table
            current_table.append(columns)
        else:
            # Not a table row, but we were in a table
            if in_table and current_table:
                # If we have collected enough rows, consider it a table
                if len(current_table) >= 2:
                    tables.append(current_table)
                current_table = []
                in_table = False
    
    # Don't forget the last table if we're still processing one
    if in_table and current_table and len(current_table) >= 2:
        tables.append(current_table)
    
    return tables
