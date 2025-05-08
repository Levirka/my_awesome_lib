My awesome Lib

My Awesome Lib to biblioteka napisana w Pythonie, zawierająca zestaw funkcji pomocnych w przetwarzaniu danych, operacjach matematycznych oraz manipulacjach tekstowych. Biblioteka jest podzielona na trzy moduły:

1) data_utils - przetwarzanie danych (np. wyszukiwanie wartości maksymalnych i minimalnych).

2) math_tools - podstawowe operacje matematyczne (dodawanie, mnożenie).

3) text_processing - operacje na tekstach (odwracanie tekstu, liczenie samogłosek).

Instalacja:

1) Klonowanie repozytorium (bash):

            git clone https://github.com/Levirka/my_awesome_lib
   
            cd my_awesome_lib

2) Instalacja biblioteki:
Można skorzystać z ręcznej instalacji w trybie deweloperskim:

        pip install -e .


Przykłady użycia
1) Moduł data_utils

        from my_awesome_lib.data_utils import find_max, find_min

        print(find_max([1, 5, 3, 7]))  # Wynik: 7
        print(find_min([1, 5, 3, 7]))  # Wynik: 1

2) Moduł math_tools

        from my_awesome_lib.math_tools import add, multiply

        print(add(2, 3))       # Wynik: 5
        print(multiply(4, 5))  # Wynik: 20

3) Moduł text_processing

        from my_awesome_lib.text_processing import reverse_text, count_vowels

        print(reverse_text("hello"))      # Wynik: "olleh"
        print(count_vowels("awesome"))    # Wynik: 4

Uruchamianie testów:
Wszystkie moduły posiadają testy jednostkowe znajdujące się w katalogu tests. Aby uruchomić testy, wykonaj poniższe polecenie:

        python -m unittest discover -s tests

Licencja:

Ten projekt jest objety licencją MIT, która opisana jest w folderze "LICENSE.txt"

Autor:

Wiktoria Czernielewska

Wersja:

1.0.0

