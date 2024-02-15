let currentSlide = 0;
let slideInterval;

function startSlider() {
  slideInterval = setInterval(nextSlide, 7000); // Вызываем nextSlide каждые 7 секунд (7000 миллисекунд)
}

function stopSlider() {
  clearInterval(slideInterval); // Останавливаем интервал, чтобы прекратить автоматическое переключение слайдов
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

// Добавляем обработчики событий для начала и остановки слайдера при наведении мыши
const sliderContainer = document.querySelector('.slider-container');
sliderContainer.addEventListener('mouseenter', stopSlider);
sliderContainer.addEventListener('mouseleave', startSlider);

// Запускаем слайдер
startSlider();