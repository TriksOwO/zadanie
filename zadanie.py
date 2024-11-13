import openai
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="D:\\zadanie\\secrets.env")

file_path = "Zadanie dla JJunior AI Developera - tresc artykulu.txt"
print(f"aktualny katalog roboczy: {os.getcwd()}")
print(f"ścieżka pliku: {os.path.abspath(file_path)}")
api_key = os.getenv("OPENAI_API_KEY")


if os.path.exists(file_path):
    print(openai.api_key)
else:
    print("file not found")


def read_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        if not text:
            print(f"file {file_path} is empty")
            return  None
        return text
    
article_text = read_article(file_path)
if api_key:
    openai.api_key = api_key
    print(f"API key: {openai.api_key}")
else:
    print("API key not found")