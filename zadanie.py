import openai
import os
from dotenv import load_dotenv

script_path = os.path.dirname(os.path.realpath(__file__))
secrets_path = os.path.join(script_path, 'secrets.env')
file_path = os.path.join(script_path, 'Zadanie dla JJunior AI Developera - tresc artykulu.txt')
szablon_path = os.path.join(script_path, 'szablon.html')
load_dotenv(secrets_path)
api_key = os.getenv("OPENAI_API_KEY")


if os.path.exists(file_path):
    print("znaleziono plik")
else:
    print("nie znalezionmo pliku")
    exit()


def read_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        if not text:
            print(f"plik {file_path} jest pusty")
            exit()
        return text
    
article_text = read_article(file_path)




def text_article_process(article_text):
    print("oczekiwanie na odpowiedz AI")
    prompt_parts = [
        "Proszę przekonwertować poniższy artykuł na kod HTML, używając odpowiednich tagów HTML do strukturyzacji treści. ",
        "Zidentyfikuj miejsca, w których warto dodać grafiki i oznacz je tagiem <img> z atrybutem src='image_placeholder.jpg'. ",
        "Dodaj atrybut alt do każdego obrazka z dokładnym promptem, który możemy użyć do wygenerowania grafiki. ",
        "Wstaw podpisy pod obrazkami używając tagu <figcaption> lub odpowiedniego tagu HTML. ",
        "Proszę wygenerować kod HTML, w którym każdy tag HTML będzie umieszczony na osobnej linii.",
        "Kod HTML nie powinien zawierać żadnych \n w jednej linii. Każdy element HTML, taki jak <h1>, <p>, <img> lub <footer>,",
        "powinien być umieszczony na osobnej linii. Użyj wcięć, aby kod był czytelny i łatwy do edytowania.",
        "Proszę nie używać \n między elementami w jednej linii (np. <h1>\nText</h1>), tylko w osobnych liniach dla każdego tagu HTML. ",
        "kod HTML musi zawierać jedynie treść między bez html doctype i head i body.nie doączaj znaczinków <head> <html> i <body>",
        "*Tekst opracowany przez AI... powienien być zapisany w elemencie <footer>",
        "Artykuł: {article_text}"
    ]
    prompt = "".join(prompt_parts).format(article_text=article_text)
    
    response = openai.chat.completions.create(
        messages = [{"role": "user", "content": prompt}],
        model = "gpt-4",
        max_tokens = 2048
    )
    
    if response.choices:
        format_html_content(response.choices[0].message.content)
        
    else:
        print("brak odpowiedzi od AI")
        exit()
        
    
   
def format_html_content(html_content):
    with open("artykul.html", "w", encoding='utf-8') as file:
       file.write(html_content)
    print("HTML zapisany w pliku artykul.html")
    write_podglad(szablon_path, html_content)
         
def write_podglad(szablon_path, artykul_content):
    with open(szablon_path, "r", encoding='utf-8')  as file:
        szablon = file.read()
    podglad_content = szablon.replace('<!--miejsce na artykul.html-->', artykul_content)
    with open("podglad.html", "w", encoding='utf-8') as file:
        file.write(podglad_content)
    print("podgląd stworzony")
        
      

if api_key:
    openai.api_key = api_key
    text_article_process(article_text)
else:
    print("API klucz nie znaleziony")
    exit()