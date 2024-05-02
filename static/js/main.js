let currentSlide = 0;
let slideInterval;

function startSlider() {
  slideInterval = setInterval(nextSlide, 7000);
}

function stopSlider() {
  clearInterval(slideInterval);
}

function showSlide(index) {
  const slider = document.querySelector('.slider');
  const slideWidth = document.querySelector('.slide').offsetWidth;
  currentSlide = index;
  slider.style.transform = `translateX(${-currentSlide * slideWidth}px)`;
  updateDots();
}

function nextSlide() {
  const totalSlides = document.querySelectorAll('.slide').length;
  currentSlide = (currentSlide + 1) % totalSlides;
  showSlide(currentSlide);
}

function prevSlide() {
  const totalSlides = document.querySelectorAll('.slide').length;
  currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
  showSlide(currentSlide);
}

function updateDots() {
  const dots = document.querySelectorAll('.dot');
  dots.forEach((dot, index) => {
    dot.classList.toggle('active-dot', index === currentSlide);
  });
}

let sliderContainer = document.querySelector('.slider-container');
sliderContainer.addEventListener('mouseenter', stopSlider);
sliderContainer.addEventListener('mouseleave', startSlider);

startSlider();
