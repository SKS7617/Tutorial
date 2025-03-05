function toggleMenu() {
    const navLinks = document.getElementById('navLinks');
    navLinks.classList.toggle('active');
}

/* for image swiping */ 
const swiper = new Swiper('.swiper', {
    loop: true, // Enable looping
    autoplay: {
        delay: 3000, // Auto-play every 3 seconds
    },
    pagination: {
        el: '.swiper-pagination', // Add pagination dots
        clickable: true,
    },
    navigation: {
        nextEl: '.swiper-button-next', // Next button
        prevEl: '.swiper-button-prev', // Previous button
    },
});