import openai
import os
from dotenv import load_dotenv

load_dotenv()

file_path = "Zadanie dla JJunior AI Developera - tresc artykulu.txt"
print(f"aktualny katalog roboczy: {os.getcwd()}")
print(f"ścieżka pliku: {os.path.abspath(file_path)}")
openai.api_key = os.getenv("OPENAI_API_KEY")

if os.path.exists(file_path):
    print("file found")
else:
    print("file not found")


def read_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        if text:
            print(f"file text: {text}")
        else:
            print("file is empty")
        
        return text
    
article_text = read_article(file_path)