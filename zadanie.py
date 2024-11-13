import openai
import os
from dotenv import load_dotenv

load_dotenv()
file_path = "D:\"Zadanie dla JJunior AI Developera - tresc artykulu.txt"
openai.api_key = os.getenv("OPENAI_API_KEY")

if os.path.exists(file_path):
    print("file found")
else:
    print("file not found")


def read_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()