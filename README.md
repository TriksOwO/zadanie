# zadanie
zadanie rekrutacyjne<br>
program Python polegający na odczytaniu pliku tekstowego i przekazanie go do OpenAI wraz z promtem. Z wygenerowanego wyniku
tworzony jest kod HTML , który jest następnie zapisywany w pliku. Wygenerowana odpowiedź AI zapisywana jest w pliku artykul.html, dodatkowo jest szablon kodu HTML - szablon.html. odpowiedź wygenerowana przez AI dodawana jest automatycznie dzięki Pythonowi do szablonu w odpowiednie miejsce między elemantami "body" i nastepnie tworzony jest gotowy plik html - podglad.html z zastosowaniem prostych styli CSS

struktura plików wyjściowych:
1. artykul.html - Plik HTML zawierajacą samą odpowiedź od AI
2. szablon.html - Plik HTML zawierajacy szablon kodu HTML
3. podglad.html - Plik HTML zawierajacy gotowy wynik

struktura plików wejściowych:
1. secrets.env - plik z kluczem API do OpenAI
2. Zadanie dla JJunior AI Developera - tresc artykulu.txt - plik z trescia artykulu

aby uruchomić program nalezy:
1. Zainstalować bibliotekę openai
2. posiadać konto na OpenAI z kluczem API
3. klucz API  umieścić w pliku secrets.env w podany sposób -> OPENAI_API_KEY=klucz
4. uruchomić program w terminalu