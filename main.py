import os
import sys
from utils import file_utils, json_builder
from ingest import pdf_ingest, image_ingest, text_ingest
from extract import headline_split, kv_extract, table_extract

def process_file(file_path):
    ext = os.path.splitext(file_path)[-1].lower()
    text_content = ""

    # Step 1: Ingest
    if ext == ".pdf":
        text_content = pdf_ingest.extract_text(file_path)
    elif ext in [".jpg", ".jpeg", ".png", ".tiff"]:
        text_content = image_ingest.extract_text(file_path)
    elif ext == ".txt":
        text_content = text_ingest.extract_text(file_path)
    else:
        print(f"Unsupported file type: {ext}")
        return

    # Step 2: Extraction
    structured_data = {}
    structured_data["headlines"] = headline_split.split_by_headline(text_content)
    structured_data["key_values"] = kv_extract.extract_key_values(text_content)
    structured_data["tables"] = table_extract.extract_tables(text_content)

    # Step 3: JSON Assembly
    output_json = json_builder.build_json(structured_data)

    # Step 4: Save
    file_utils.save_json(file_path, output_json)


if __name__ == "__main__":
    input_folder = "input/"
    for file in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file)
        process_file(file_path)
