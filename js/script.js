document.addEventListener("DOMContentLoaded", function () {
  const characterHeadshots = document.querySelectorAll(".character-headshot");
  const infoPanel = document.querySelector(".info-panel");

  // Tworzymy elementy do wyświetlania GIF-a postaci oraz trzech ataków
  const gifImage = document.createElement("img");
  const attackImage1 = document.createElement("img");
  const attackImage2 = document.createElement("img");
  const attackImage3 = document.createElement("img");

  gifImage.className = "gif"; // Dodaj klasę dla stylów GIF-a postaci
  attackImage1.className = "attack"; // Dodaj klasę dla stylów pierwszego GIF-a ataku
  attackImage2.className = "attack"; // Dodaj klasę dla stylów drugiego GIF-a ataku
  attackImage3.className = "attack"; // Dodaj klasę dla stylów trzeciego GIF-a ataku

  // Dodajemy elementy do info-panel
  infoPanel.appendChild(gifImage);
  infoPanel.appendChild(attackImage1);
  infoPanel.appendChild(attackImage2);
  infoPanel.appendChild(attackImage3);

  // Funkcja ukrywania wszystkich GIF-ów
  function hideAllGifs() {
    gifImage.classList.remove("visible");
    attackImage1.classList.remove("visible");
    attackImage2.classList.remove("visible");
    attackImage3.classList.remove("visible");
  }

  // Obsługa zdarzeń na elementach headshot
  characterHeadshots.forEach((headshot) => {
    headshot.addEventListener("mouseenter", () => {
      // Pobieramy GIF-a postaci oraz ataki
      const gifURL = headshot.getAttribute("data-gif");
      const attackURL1 = headshot.getAttribute("data-attack1");
      const attackURL2 = headshot.getAttribute("data-attack2");
      const attackURL3 = headshot.getAttribute("data-attack3");

      // Ustawiamy źródła GIF-ów
      gifImage.src = gifURL;
      attackImage1.src = attackURL1;
      attackImage2.src = attackURL2;
      attackImage3.src = attackURL3;

      // Pokazujemy GIF-y
      gifImage.classList.add("visible");
      attackImage1.classList.add("visible");
      attackImage2.classList.add("visible");
      attackImage3.classList.add("visible");
    });

    headshot.addEventListener("mouseleave", hideAllGifs);
  });

  // Ukrywamy GIF-y na starcie
  hideAllGifs();
});
