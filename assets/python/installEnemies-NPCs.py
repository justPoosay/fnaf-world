import os
import requests
from bs4 import BeautifulSoup

# Lista postaci, których GIFy chcesz pobrać
character_names = [
    # Bosses Update 1
    "Auto-Chipper",
    "Bouncer",
    "Browboy",
    "Bubba",
    "Chipper's Revenge",
    "Mad Endo",
    "Overclock",
    "Gold Endo",
    "Eyesore",
    "Porkpatch",
    "Scott Cawthon",
    "Seagoon",
    "Security",
    "Snowcone",
    "Supergoon",

    # Update 2
    "Purplegeist",

    # Halloween Edition
    "Anchovy",
    "Party Hat A",
    "Party Hat B",
    "Purplegeist",

    # Enemies Update 1
    "!2222",
    "%25_^^%26(",
    "Ballboy",
    "Beartrap",
    "Blacktrap",
    "Bouncepot",
    "Boxbyte",
    "Chillax",
    "Chop 'N Roll",
    "Colossal",
    "Crabapple",
    "Dogfight",
    "Flan",
    "Gearrat",
    "Glitched Enemy 3",
    "Goldmine",
    "Graveweed",
    "Mechrab",
    "Meringue",
    "Metalman",
    "Prototype",
    "Quarry",
    "Redbear",
    "Seaweed",
    "Tangle",
    "Tombstack",
    "Totemole",
    "White Rabbit",

    # Update 2
    "Neon",
    "P.Goon",

    # Halloween Edition
    "Big Jack",
    "Brow Boy",
    "Cheesehead",
    "Half-Bake",
    "Madjack",
    "Mini P",
    "Mudpie",
    "Prototype",
    "Quad Endo",
    "Security",
    "Xangle",

    # NPCs Update 1
    "8-bit Fredbear",
    "DeeDee",
    "Desk Man",
    "Fredbear (Map)",
    "Lolbit",
    "Mendo"
]

def sanitize_filename(filename):
    return "".join(c if c.isalnum() or c in (' ', '_', '-') else '_' for c in filename)

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
                # Sprawdź, czy odpowiedź to GIF
                if image_url and (image_url.endswith('.gif') or 'image/gif' in requests.head(image_url).headers.get('Content-Type', '')):
                    gif_urls.append(image_url)  # Dodanie URL do listy
                    break  # Możesz usunąć to, jeśli chcesz zebrać więcej niż jeden GIF z danej postaci
        except Exception as e:
            print(f"Nie można pobrać strony postaci: {character_url}, błąd: {e}")

    return gif_urls

def download_image(image_url, folder, character_name):
    print(f"Próbuję pobrać: {image_url}")
    try:
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()

        file_name = sanitize_filename(character_name) + '.gif'  # Użycie nazwy postaci jako nazwy pliku
        file_path = os.path.join(folder, file_name)

        with open(file_path, 'wb') as f:
            f.write(response.content)

        print(f"Pobrano: {file_path}")
    except Exception as e:
        print(f"Błąd podczas pobierania obrazu: {image_url}, błąd: {e}")

if __name__ == "__main__":
    base_url = "https://five-nights-at-freddys-world.fandom.com/wiki/"
    folder_input = r'C:\Users\OscarStaniszewski\Desktop'  # Użyj folderu nadrzędnego
    gifs_folder = os.path.join(folder_input, 'pobrane_gify')  # Nowy folder dla GIF-ów

    if not os.path.exists(gifs_folder):
        os.makedirs(gifs_folder)

    # Tworzenie linków do postaci
    character_links = construct_character_links(base_url, character_names)
    print(f"Znaleziono {len(character_links)} postaci.")

    # Zbieranie URL GIF-ów
    gif_urls = gather_gif_urls(character_links)
    print(f"Znaleziono {len(gif_urls)} GIF-ów do pobrania.")

    # Pobieranie GIF-ów z nazwami postaci
    for character_name, gif_url in zip(character_names, gif_urls):
        # Upewniamy się, że gif_url i character_name są odpowiednio sparowane
        download_image(gif_url, gifs_folder, character_name)