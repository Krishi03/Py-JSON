# Document Converter

A Python-based document conversion tool that extracts text from images and PDFs, converting them into structured JSON format.

## Features

- Image to text conversion using Tesseract OCR
- PDF text extraction
- Structured JSON output
- Support for tables and key-value pairs

## Prerequisites

- Python 3.x
- Tesseract OCR
- Required Python packages:
  - pytesseract
  - Pillow (PIL)
  - PyMuPDF (for PDF processing)

## Installation

1. Install Tesseract OCR:
   - Download from [Tesseract GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
   - Install and add to system PATH

2. Install Python dependencies:
   ```bash
   pip install pytesseract Pillow PyMuPDF