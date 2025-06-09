let slideIndex = 0;
let slides;

function showSlide(index) {
    for (let i = 0; i < slides.length; i++) {
        slides[i].classList.remove("active");
    }
    slideIndex = (index + slides.length) % slides.length;
    slides[slideIndex].classList.add("active");
}

function plusSlides(n) {
    showSlide(slideIndex + n);
}

function autoSlide() {
    plusSlides(1);
    setTimeout(autoSlide, 4000);
}

document.addEventListener("DOMContentLoaded", () => {
    slides = document.getElementsByClassName("slide");
    showSlide(slideIndex);
    setTimeout(autoSlide, 4000);

    // Pridanie eventov pre šípky, ak ich chceš priamo ovládať aj JS-om:
    const prev = document.querySelector(".prev");
    const next = document.querySelector(".next");
    if (prev && next) {
        prev.addEventListener("click", () => plusSlides(-1));
        next.addEventListener("click", () => plusSlides(1));
    }
});
