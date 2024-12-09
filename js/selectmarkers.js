document.addEventListener("DOMContentLoaded", function () {
  const characterHeadshots = document.querySelectorAll(".character-headshot");
  const overlays = []; // Przechowuje aktywne nakładki
  const maxSelections = 8; // Maksymalna liczba wyborów

  // Preload GIF-ów
  const preloadGifs = [];
  for (let i = 1; i <= maxSelections; i++) {
    const gif = new Image();
    gif.src = `../assets/images/Headshots/${i}.gif`; // Ścieżka do animowanych GIF-ów
    preloadGifs.push(gif);
  }

  characterHeadshots.forEach((headshot) => {
    headshot.addEventListener("click", function () {
      if (overlays.length >= maxSelections) {
        console.log("Osiągnięto limit wyborów!");
        return;
      }

      // Sprawdź, czy nakładka już istnieje na tym headshocie
      if (headshot.querySelector(".overlay")) {
        console.log("Nakładka już istnieje dla tego headshota.");
        return;
      }

      // Tworzenie nowej nakładki
      const overlay = document.createElement("div");
      overlay.className = "overlay";
      overlay.style.backgroundImage = `url('../assets/images/Headshots/${overlays.length + 1}.gif')`; // Wybierz załadowany GIF

      // Debugowanie - sprawdzenie, czy nakładka jest dodana
      console.log(`Dodaję nakładkę na headshot: ${headshot}`);
      
      // Sprawdź, czy nakładka ma poprawny styl
      console.log(`Nakładka GIF: ../assets/images/Headshots/${overlays.length + 1}.gif`);

      // Dodaj nakładkę do headshota
      headshot.appendChild(overlay);

      // Dodaj nakładkę do listy aktywnych
      overlays.push(overlay);

      // Debugowanie - sprawdzenie długości listy nakładek
      console.log(`Liczba aktywnych nakładek: ${overlays.length}`);
    });
  });

  // Obsługa przycisku resetowania
  const resetButton = document.querySelector(".reset");
  if (resetButton) {
    resetButton.addEventListener("click", function () {
      // Usuń wszystkie nakładki z DOM
      overlays.forEach((overlay) => {
        overlay.parentElement.removeChild(overlay);
      });

      // Wyczyść listę nakładek
      overlays.length = 0;

      // Debugowanie - potwierdzenie resetu
      console.log("Zresetowano wszystkie nakładki.");
    });
  }

  console.log("Skrypt uruchomiony!");
});
