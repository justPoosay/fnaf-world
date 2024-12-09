import requests
from bs4 import BeautifulSoup
import os
import re

# Funkcja do czyszczenia nazwy pliku
def clean_filename(name):
    # Usunięcie białych znaków i zamiana niedozwolonych znaków na podkreślnik
    name = re.sub(r'[<>:"/\\|?*]', '_', name)  # Zamiana niedozwolonych znaków
    name = name.replace('\n', '').replace('\r', '').strip()  # Usunięcie nowej linii
    return name

# URL strony z gifami
url = "https://five-nights-at-freddys-world.fandom.com/wiki/Party_Members"

# Wysłanie żądania HTTP do strony
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Tworzenie folderu do zapisu gifów
if not os.path.exists("AttackAnimations"):
    os.makedirs("AttackAnimations")

# Znajdowanie tabeli za pomocą odpowiednich klas
table = soup.find("table", class_="article-table")
rows = table.find_all("tr")[1:]  # Pomiń pierwszy wiersz (nagłówki)

# Iteracja po wierszach tabeli i pobieranie gifów
for row in rows:
    cells = row.find_all("td")
    
    # Uzyskiwanie gifów ataków (trzeci element w komórkach)
    attack_gif = cells[2].find("a")["href"]
    
    # Uzyskiwanie nazwy postaci odnośnie do gifów
    character_name = clean_filename(cells[0].text)  # Użyj funkcji do czyszczenia nazwy

    # Zapis gifów
    gif_response = requests.get(attack_gif)
    with open(f"giphy_attacks/{character_name}_attack.gif", "wb") as gif_file:
        gif_file.write(gif_response.content)

    print(f"Pobrano: {character_name}_attack.gif")

print("Pobieranie zakończone.")