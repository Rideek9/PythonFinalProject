# PythonFinalProject

Aplikacja do samorozwoju  

Koncepcją aplikacji jest pomoc w nauce przy pomocy kilku narzędzi między innymi funkcji z fiszkami, modułem translatora, funkcji poprawiania spostrzegawczości, zapamiętywania, nauki szybkiego czytania.

Aplikacja będzie rozwijana w przyszłości o kolejne moduły, dzięki którym użytkownik będzie mógł w łatwy sposób doskonalić swoje umiejętności i wiedzie.

## Narzędzia aplikacji

1. Python 3.9
2. Flask - Jądro aplikacji
3. MySQL - wykorzystanie baz danych MySQL do przechowywania wszelkich informacji
4. HTML, CSS, JS - Stworzenie fron-endu aplikacji
5. plik requirements.txt - wszystkie infomracje o wykorzystywanych modułach python3


## Działanie

1. Użytkownik loguje sie do swojego konta przy pomocy loginu (maila) i hasła
2. W momencie kiedy użytkownik nie istnieje ma możliwość stworzenia swojego konta
3. Apliakcja przechowuje poniższe dane, które służą do identyfikacji użytkownika 
   * email
   * hasło
   * imie
4. Aplikacja tworzy personalizowane tabele baz danych w których są przechowywane odpowiednie informacje dotyczące odpowiednich funkcji
   * fiszki 
     * słowo w języku
     * nr pułki
   * spostrzegawczość
     * poziom doświadczenia
   * zapamiętywanie
     * poziom doświadczenia

### Funkcje aplikacji

1. (data: 09.07.2022) Translator - funkcja do tłumaczenia. Użytkownik po przetłumaczeniu słowa z jednego jezyka na drugie będzie miał możliwość dopisania do listy słów do nauki.
Słowo zapisze się w odpowiedniej tabeli bazy danych danego użytkownika z której słowa będą pobieranie do modułu fiszek
2. (data: 09:07.2022) Fiszki - funkcja wykorzystująca rozwiazanie do naki przy pomocy fiszek. Użytkownik dostanie pytanie dotyczące słowa które następnie będzie musiał przetłumaczyć i wpisać je w odpowiednie miejsce. jeśli użytkownik odpowie poprawnie dostanie kolejne słowo a poprawna odpowiedź przejdzie do kolejnego schowka. W puli będzie 5 schowków w momencie kiedy użytkownik dojdzie do 5 schowka i odpowie poprawnie słowo trafia na pułkę nauczone.
Po pewnym czasie użytkownik dostanie egzamin ze słówek w celu sprawdzenia czy nauczył się danych słów.
3. (data: nieznana) Spostrzegawczość - funkcja która ma na celu poprawienie spostrzegawczości użytkownika. Jest to jedna ze składowych poprawienia szybkości czytania. Użytkownik będzie zdobywać poziomy doświadczenia które będą odblokowywać kolejne etapuy rozwoju. 
4. (data: nieznana) Zapamiętywanie -  funkcja która ma na celu poprawienie zpamiętywania użytkownika. Jest to jedna ze składowych poprawienia szybkości czytania. Użytkownik będzie zdobywać poziomy doświadczenia które będą odblokowywać kolejne etapuy rozwoju. 

