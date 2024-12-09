import os
import requests
from bs4 import BeautifulSoup

# Lista postaci, których GIFy chcesz pobrać
character_names = [
    "Adventure Animdude",
    "Adventure Balloon Boy",
    "Adventure Bonnie",
    "Adventure Chica",
    "Adventure Coffee",
    "Adventure Crying Child",
    "Adventure Endo-01",
    "Adventure Endo-02",
    "Adventure Endoplush",
    "Adventure Foxy",
    "Adventure Fredbear",
    "Adventure Freddy Fazbear",
    "Adventure Funtime Foxy",
    "Adventure Golden Freddy",
    "Adventure Jack-O-Bonnie",
    "Adventure Jack-O-Chica",
    "Adventure JJ",
    "Adventure Mangle",
    "Adventure Marionette",
    "Adventure Mr. Chipper",
    "Adventure Nightmare",
    "Adventure Nightmare Balloon Boy",
    "Adventure Nightmare Bonnie",
    "Adventure Nightmare Chica",
    "Adventure Nightmare Foxy",
    "Adventure Nightmare Fredbear",
    "Adventure Nightmare Freddy",
    "Adventure Nightmarionne",
    "Adventure Paper Pals",
    "Adventure Paperpals",
    "Adventure Phantom Balloon Boy",
    "Adventure Phantom Chica",
    "Adventure Phantom Foxy",
    "Adventure Phantom Freddy",
    "Adventure Phantom Mangle",
    "Adventure Phantom Marionette",
    "Adventure Plushtrap",
    "Adventure PurpleGuy",
    "Adventure RWQFSFASXC",
    "Adventure Shadow Freddy",
    "Adventure Spring Bonnie",
    "Adventure Springtrap",
    "Adventure Toy Bonnie",
    "Adventure Toy Chica",
    "Adventure Toy Freddy",
    "Adventure Withered Bonnie",
    "Adventure Withered Chica",
    "Adventure Withered Foxy",
    "Adventure Withered Freddy",
]

def sanitize_filename(filename):
    return "".join(c if c.isalnum() else "_" for c in filename)

def construct_character_links(base_url, characters):
    return [f"{base_url}{character.replace(' ', '_')}" for character in characters]

def gather_gif_urls(character_links):
    gif_urls = []  # Lista do przechowywania URL GIF-ów

    for character_url in character_links:
        try:
            response = requests.get(character_url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            images = soup.find_all('img')

            for img in images:
                image_url = img.get('src')
                # Spójrzmy na wbudowane formaty GIF i rozszerzenia z obrazków
                if image_url and (image_url.endswith('.gif') or 'image/gif' in requests.head(image_url).headers.get('Content-Type', '')):
                    gif_urls.append(image_url)  # Dodajemy URL do listy
                    break  # Możesz usunąć to, jeśli chcesz zebrać więcej niż jeden GIF z danej postaci
        except Exception as e:
            print(f"Nie można pobrać strony postaci: {character_url}, błąd: {e}")

    return gif_urls

def download_image(image_url, folder, character_name):
    print(f"Próbuję pobrać: {image_url}")
    try:
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()

        file_name = sanitize_filename(character_name) + '.gif'  # Używamy nazwy postaci jako nazwy pliku
        file_path = os.path.join(folder, file_name)

        with open(file_path, 'wb') as f:
            f.write(response.content)

        print(f"Pobrano: {file_path}")
    except Exception as e:
        print(f"Błąd podczas pobierania obrazu: {image_url}, błąd: {e}")

if __name__ == "__main__":
    base_url = "https://five-nights-at-freddys-world.fandom.com/wiki/"
    folder_input = r'C:\Users\OscarStaniszewski\Desktop\gifs'

    if not os.path.exists(folder_input):
        os.makedirs(folder_input)

    # Tworzenie linków do postaci
    character_links = construct_character_links(base_url, character_names)
    print(f"Znaleziono {len(character_links)} postaci.")

    # Zbieranie URL GIF-ów
    gif_urls = gather_gif_urls(character_links)
    print(f"Znaleziono {len(gif_urls)} GIF-ów do pobrania.")

    # Pobieranie GIF-ów z nazwą postaci
    for character_name, gif_url in zip(character_names, gif_urls):
        download_image(gif_url, folder_input, character_name)