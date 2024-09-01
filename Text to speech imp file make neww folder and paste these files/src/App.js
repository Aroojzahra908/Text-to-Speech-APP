// alll okkki final

import React, { useState } from 'react';
import axios from 'axios';
import Tesseract from 'tesseract.js';
import './App.css';

const API_URL = 'http://127.0.0.1:5000';

async function extractTextFromFile(file) {
  const fileExt = file.name.split('.').pop().toLowerCase();

  if (fileExt === 'pdf') {
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post(`${API_URL}/upload`, formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });
      return response.data.text;
    } catch (error) {
      console.error('Error during PDF text extraction:', error);
      throw new Error('Failed to extract text from PDF');
    }
  } else if (['png', 'jpg', 'jpeg'].includes(fileExt)) {
    const { data: { text } } = await Tesseract.recognize(file, 'eng');
    return text;
  } else if (fileExt === 'txt') {
    const text = await file.text();
    return text;
  } else {
    throw new Error('Unsupported file type');
  }
}

async function sendTextToSpeech(text) {
  try {
    const response = await axios.post(`${API_URL}/text-to-speech`, { text }, { responseType: 'blob' });
    return response.data;
  } catch (error) {
    console.error('Error during text-to-speech request:', error);
    throw new Error('Failed to convert text to speech');
  }
}

function FileUploadAndTextInputComponent() {
  const [file, setFile] = useState(null);
  const [text, setText] = useState('');
  const [audioUrl, setAudioUrl] = useState('');
  const [message, setMessage] = useState('');
  const [isProcessing, setIsProcessing] = useState(false);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleTextChange = (event) => {
    setText(event.target.value);
  };

  const handleSpeak = async () => {
    setIsProcessing(true);
    let extractedText = text.trim();
    if (file) {
      try {
        extractedText = await extractTextFromFile(file);
        if (!extractedText) {
          setMessage('No text found in file.');
          setIsProcessing(false);
          return;
        }
        setText(extractedText);
      } catch (error) {
        setMessage(`Error: ${error.message}`);
        setIsProcessing(false);
        return;
      }
    }

    if (!extractedText) {
      setMessage('Please enter text or upload a file with text.');
      setIsProcessing(false);
      return;
    }

    try {
      const audioBlob = await sendTextToSpeech(extractedText);
      const audioUrl = URL.createObjectURL(audioBlob);
      setAudioUrl(audioUrl);
      setMessage('Audio ready. Click Play to listen.');
    } catch (error) {
      setMessage(`Error: ${error.message}`);
    }
    setIsProcessing(false);
  };

  const handleAudioRemove = () => {
    setAudioUrl('');
  };

  return (
    <div className="app-container">
      <h1>Text-to-Speech APP </h1>

      <div>
        <input
          type="file"
          accept=".pdf, .png, .jpg, .jpeg, .txt"
          onChange={handleFileChange}
        />
        <textarea
          rows="4"
          cols="50"
          value={text}
          onChange={handleTextChange}
          placeholder="Enter text here..."
        />
        <div className="button-container">
          <button onClick={handleSpeak} disabled={isProcessing}>
            {isProcessing ? 'Processing...' : 'Speak'}
          </button>
        </div>
      </div>

      {audioUrl && (
        <div className="audio-container">
          <h2>Audio Ready:</h2>
          <audio controls src={audioUrl}></audio>
          <div className="button-container">
            <button onClick={handleAudioRemove}>Remove Audio</button>
          </div>
        </div>
      )}

      {message && <p>{message}</p>}
    </div>
  );
}

export default FileUploadAndTextInputComponent;
