// Sélectionnez toutes les diapositives
const slides = document.querySelectorAll('.slides');
// Initialisez un index pour la diapositive active
let currentSlide = 0;

// Fonction pour activer une diapositive spécifique
function setActiveSlide(index) {
  // Parcours toutes les diapositives pour les désactiver
  slides.forEach(slide => {
    slide.classList.remove('active');
  });
  // Active la diapositive spécifiée par l'index
  slides[index].classList.add('active');
}

// Fonction pour passer à la prochaine diapositive
function nextSlide() {
  // Incrémentez l'index de la diapositive
  currentSlide++;
  // Si l'index dépasse le nombre de diapositives, revenez à la première diapositive
  if (currentSlide >= slides.length) {
    currentSlide = 0;
  }
  // Activez la diapositive suivante
  setActiveSlide(currentSlide);
}

// Démarrez l'intervalle pour changer de diapositive toutes les 5 secondes
setInterval(nextSlide, 8000);


