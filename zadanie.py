import openai
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="D:\\zadanie\\secrets.env")
file_path = "Zadanie dla JJunior AI Developera - tresc artykulu.txt"
api_key = os.getenv("OPENAI_API_KEY")


if os.path.exists(file_path):
    print("file found")
else:
    print("file not found")
    exit()


def read_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        if not text:
            print(f"file {file_path} is empty")
            return  None
        return text
    
article_text = read_article(file_path)




def text_article_process(article_text):
    prompt_parts = [
        "Proszę przekonwertować poniższy artykuł na kod HTML, używając odpowiednich tagów HTML do strukturyzacji treści. ",
        "Zidentyfikuj miejsca, w których warto dodać grafiki i oznacz je tagiem <img> z atrybutem src='image_placeholder.jpg'. ",
        "Dodaj atrybut alt do każdego obrazka z dokładnym promptem, który możemy użyć do wygenerowania grafiki. ",
        "Wstaw podpisy pod obrazkami używając tagu <figcaption> lub odpowiedniego tagu HTML. ",
        "Proszę wygenerować kod HTML, w którym każdy tag HTML będzie umieszczony na osobnej linii.",
        "Kod HTML nie powinien zawierać żadnych \n w jednej linii. Każdy element HTML, taki jak <h1>, <p>, <img> lub <footer>, ",
        "powinien być umieszczony na osobnej linii. Użyj wcięć, aby kod był czytelny i łatwy do edytowania.",
        "Proszę nie używać \n między elementami w jednej linii (np. <h1>\nText</h1>), tylko w osobnych liniach dla każdego tagu HTML. ",
        "Artykuł: {article_text}"
    ]
    prompt = "".join(prompt_parts).format(article_text=article_text)
    
    response = openai.chat.completions.create(
        messages = [{"role": "user", "content": prompt}],
        model = "gpt-4",
        max_tokens = 2048
    )
    print(f" responses {response}")
    if response.choices:
        html_content = response.choices[0].message.content
        print(f"AI before convert: \n {html_content}")
        formated_html = format_html_content(html_content)
        print(f"Text after format: \n {formated_html}")
        return formated_html
    else:
        print("No response from AI")
        return None
    
   
def format_html_content(html_content):
    formated_html = html_content.replace('>', '>\n')
    return formated_html.strip();        
        

if api_key:
    openai.api_key = api_key
    processed_text = text_article_process(article_text)
else:
    print("API key not found")
    exit()