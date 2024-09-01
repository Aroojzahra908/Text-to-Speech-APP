# Text-to-Speech and Text Extraction API

This Flask application provides endpoints for extracting text from image and PDF files, translating the text, and converting it to speech.

# Overview:
## Text-to-Speech Path

Here is an example of the text-to-speech functionality:

![Text to Speech Path](images/text%20to%20speech%20path.png)

## File Upload Example

Here is how the file upload functionality looks:

![File Upload path](images/file%20upload.png)

## Features

- Extract text from PNG, JPG, JPEG images, and PDF files.
- Translate text to Urdu.
- Convert translated text to speech in Urdu.

## Installation

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd <repository-directory>

## Install Dependencies
- pip install -r requirements.txt

## Setup Tesseract OCR
Ensure that Tesseract OCR is installed and the path is set correctly in the script. Modify pytesseract.pytesseract.tesseract_cmd if needed.

## Running the Application
Start the Flask Application
```python app.py

## API Endpoints

- Upload File
- URL: /upload
- Method: POST
-Form Data:
-file: The file to upload (image or PDF)

## Response:
-text: Extracted text from the file

## Text-to-Speech

-URL: /text-to-speech
-Method: POST
-JSON Body:
-text: The text to convert to speech
-lang: Optional language code (default is 'ur')

## Response:
- An audio file in MP3 format with the spoken text