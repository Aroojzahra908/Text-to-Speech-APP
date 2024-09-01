from flask import Flask, request, jsonify, send_file
import io
from gtts import gTTS
from googletrans import Translator
from flask_cors import CORS 
from PIL import Image
import pytesseract
import fitz  # PyMuPDF

pytesseract.pytesseract.tesseract_cmd = r'D:\terractocr\tesseract.exe'

app = Flask(__name__)
CORS(app)

def text_to_speech(text, lang='ur'):
    tts = gTTS(text=text, lang=lang)
    audio_file = io.BytesIO()
    tts.write_to_fp(audio_file)
    audio_file.seek(0)
    return audio_file

def translate_text(text, dest_lang='ur'):
    translator = Translator()
    translated = translator.translate(text, dest=dest_lang)
    return translated.text

def extract_text_from_image(image):
    img = Image.open(image)
    text = pytesseract.image_to_string(img)
    return text

def extract_text_from_pdf(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and (file.filename.endswith('.png') or file.filename.endswith('.jpg') or file.filename.endswith('.jpeg')):
        text = extract_text_from_image(file)
    elif file and file.filename.endswith('.pdf'):
        text = extract_text_from_pdf(file)
    else:
        return jsonify({'error': 'Unsupported file type'}), 400

    return jsonify({'text': text})

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech_endpoint():
    data = request.json
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    text = data['text']
    lang = data.get('lang', 'ur')
    translated_text = translate_text(text, dest_lang=lang)
    audio_file = text_to_speech(translated_text, lang=lang)

    return send_file(
        audio_file,
        mimetype='audio/mpeg',
        as_attachment=False,
        download_name='output.mp3'
    )

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
