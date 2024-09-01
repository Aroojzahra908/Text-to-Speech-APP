### Text-to-Speech App
A simple web application that extracts text from various file types (PDFs, images, and text files) and converts the extracted text into speech. The app also supports displaying extracted text in Urdu.

## how we create new project 
npx create-react-app my-text-to-speech-app

## Screenshot
![App Screenshot](images\Demo.png)
The above image shows the main interface of the application.

## Features
- Extract text from PDFs, images (PNG, JPG, JPEG), and text files.
- Convert extracted text to speech.
-Supports displaying text in Urdu.
-User-friendly interface with file upload and text input options.

## Prerequisites
Before running the application, ensure you have the following installed:

-Node.js (version 14 or higher)
-npm (Node Package Manager)
-Python (version 3.7 or higher)
-Flask (Python web framework)
-Tesseract.js (JavaScript library for OCR)
-axios (JavaScript library for making HTTP requests)

## Installation and Setup
Follow these steps to set up and run the application:

1. Clone the Repository
git clone https://github.com/your-username/text-to-speech-app.git
cd text-to-speech-app

2. Install Frontend Dependencies
Navigate to the frontend directory and install the required dependencies:
- npm install

3. Install Backend Dependencies
Navigate to the backend directory and install the required Python packages:
- pip install -r requirements.txt

4. Start the Backend Server
Run the Flask server to handle file uploads and text extraction:
 - python app.py
The backend server will start at http://127.0.0.1:5000/upload
The backend server will start at http://127.0.0.1:5000/text-to-speech  
e.g : to check postman 
{
  "text": "Hello, world!"
}


5. Start the Frontend Server
Navigate back to the frontend directory and start the React application:
- npm start
- The frontend server will start at http://localhost:3000.

### Usage
- Upload Files: Use the "Upload" button to select a PDF, image (PNG, JPG, JPEG), or text file from your computer.
- Extract Text: The app will automatically extract text from the uploaded file.
- Convert to Speech: Click the "Speak" button to convert the extracted text to speech.
- Play Audio: Use the audio controls to play the generated speech.
- Remove Audio: Click "Remove Audio" to delete the generated audio file
