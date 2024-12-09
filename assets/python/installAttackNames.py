import os
import requests
from bs4 import BeautifulSoup

# URL strony z listą ataków
URL = "https://five-nights-at-freddys-world.fandom.com/wiki/Party_Members"

# Nagłówki przeglądarki, aby uniknąć blokowania przez serwer
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

# Folder do zapisu gifów
DOWNLOAD_FOLDER = "gifs2"

# Lista wybranych ataków
SELECTED_ATTACKS = [
    "4th Wall", "Bash Jam", "Bubble Breath", "Endo Army", "Esc Key", "Happy Jam", "Hocus Pocus", 
    "Mega Virus", "Mic Toss", "Mimic Ball", "Mystery Box 2", "Neon Wall 2", "Prize Ball"
]

# Tworzenie folderu na pliki
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

# Zbiór do przechowywania liczby pobrań dla każdej nazwy
download_count = {}

# Funkcja do pobrania gifów ataków
def download_attack_gifs():
    # Pobierz stronę HTML
    response = requests.get(URL, headers=HEADERS)
    if response.status_code != 200:
        print(f"Błąd pobierania strony: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Znajdź wszystkie obrazki na stronie
    gifs = soup.find_all("img")
    
    # Pobieraj tylko obrazy z atakami
    for img in gifs:
        img_url = img.get("src")  # Pobierz URL obrazka
        if img_url and ".gif" in img_url:  # Sprawdź, czy to gif
            # Sprawdź, czy nazwa ataku jest w URL
            for attack_name in SELECTED_ATTACKS:
                formatted_name = attack_name.replace(" ", "_")  # Zamiana spacji na podkreślenia
                if formatted_name in img_url:  # Dopasowanie nazwy ataku w URL
                    try:
                        # Sprawdzenie, jak często już pobrano ten atak
                        if formatted_name not in download_count:
                            download_count[formatted_name] = 1
                        else:
                            download_count[formatted_name] += 1

                        # Ustaw nazwę pliku z liczbą, jeśli atak się powtarza
                        if download_count[formatted_name] > 1:
                            file_name = f"{formatted_name}_{download_count[formatted_name]}.gif"
                        else:
                            file_name = f"{formatted_name}.gif"

                        # Pobierz zawartość pliku
                        img_response = requests.get(img_url, headers=HEADERS)
                        if img_response.status_code == 200:
                            # Zapisz plik
                            file_path = os.path.join(DOWNLOAD_FOLDER, file_name)
                            with open(file_path, "wb") as f:
                                f.write(img_response.content)
                            print(f"Pobrano: {file_name}")
                        else:
                            print(f"Błąd pobierania {img_url}: {img_response.status_code}")
                    except Exception as e:
                        print(f"Błąd: {e} przy pobieraniu {img_url}")
                    break  # Jeśli znaleziono pasujący atak, przejdź do następnego obrazu

# Uruchom funkcję
download_attack_gifs()
