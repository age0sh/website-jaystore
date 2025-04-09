document.addEventListener("DOMContentLoaded", () => {
        let currentBanner = 0;
        const banners = document.querySelectorAll('.banner-img');
    
        setInterval(() => {
            banners[currentBanner].classList.remove('active');
            currentBanner = (currentBanner + 1) % banners.length;
            banners[currentBanner].classList.add('active');
        }, 5000); // Cambia de imagen cada 5 segundos
    });
    
    document.addEventListener('DOMContentLoaded', function () {
        const menuToggle = document.getElementById('menu-toggle');
        const menuItems = document.getElementById('MenuItems');
      
        menuToggle.addEventListener('click', function () {
          menuItems.classList.toggle('active');
        });
      });