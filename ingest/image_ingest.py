import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image_path):
    try:
        # Verify image exists
        if not os.path.exists(image_path):
            return "Error: Image file not found"
            
        # Open and verify image
        img = Image.open(image_path)
        
        # Print image details for debugging
        print(f"Image size: {img.size}")
        print(f"Image mode: {img.mode}")
        
        # Extract text
        text = pytesseract.image_to_string(img)
        
        # Print extracted text for debugging
        print(f"Extracted text length: {len(text)}")
        print("First 100 characters:", text[:100])
        
        if not text.strip():
            return "No text was extracted from the image"
        return text.strip()
    except Exception as e:
        return f"Error processing image: {str(e)}"
