document.addEventListener("DOMContentLoaded", () => {
    let slideIndex = 0;
    let slides = document.getElementsByClassName("slide");
    let dots = document.getElementsByClassName("dot");
    let autoSlideInterval;

    function showSlide(index) {
        if (slides.length === 0) return;
        slideIndex = (index + slides.length) % slides.length;
        for (let i = 0; i < slides.length; i++) {
            slides[i].classList.remove("active");
            if (dots[i]) dots[i].classList.remove("active");
        }
        slides[slideIndex].classList.add("active");
        if (dots[slideIndex]) dots[slideIndex].classList.add("active");
    }

    function plusSlides(n) {
        showSlide(slideIndex + n);
        resetAutoSlide();
    }

    function currentSlide(n) {
        showSlide(n);
        resetAutoSlide();
    }

    function autoSlide() {
        plusSlides(1);
        autoSlideInterval = setTimeout(autoSlide, 4000);
    }

    function resetAutoSlide() {
        clearTimeout(autoSlideInterval);
        autoSlideInterval = setTimeout(autoSlide, 4000);
    }

    window.plusSlides = plusSlides;
    window.currentSlide = currentSlide;

    showSlide(slideIndex);
    autoSlide();
});
