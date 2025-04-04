document.addEventListener('DOMContentLoaded', function() {
    const bannerImages = document.querySelectorAll('.banner-image');
    let currentIndex = 0;
    const intervalTime = 5000; // 5 segundos

    function showNextImage() {
        // Oculta la imagen actual
        bannerImages[currentIndex].classList.remove('active');

        // Calcula el índice de la siguiente imagen
        currentIndex = (currentIndex + 1) % bannerImages.length;

        // Muestra la siguiente imagen
        bannerImages[currentIndex].classList.add('active');
    }

    // Inicia el carrusel al cargar la página
    setInterval(showNextImage, intervalTime);
});