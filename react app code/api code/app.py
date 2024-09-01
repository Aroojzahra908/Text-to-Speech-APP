import os
import io
import PyPDF2
import pygame
from gtts import gTTS
from tkinter import Tk, filedialog
from googletrans import Translator

def text_to_speech(text, lang='ur'):
    tts = gTTS(text=text, lang=lang)
    with io.BytesIO() as audio_file:
        tts.write_to_fp(audio_file)
        audio_file.seek(0)
        pygame.mixer.init()
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue

def get_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

def translate_text(text, dest_lang='ur'):
    translator = Translator()
    translated = translator.translate(text, dest=dest_lang)
    return translated.text

def main():
    Tk().withdraw()  # Hide the root window
    choice = input("Choose an option (1: Write text, 2: Upload PDF): ")

    if choice == '1':
        text = input("Enter text: ")
        translated_text = translate_text(text, dest_lang='ur')
        text_to_speech(translated_text)

    elif choice == '2':
        pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if pdf_path:
            text = get_text_from_pdf(pdf_path)
            translated_text = translate_text(text, dest_lang='ur')
            text_to_speech(translated_text)
        else:
            print("No file selected.")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()