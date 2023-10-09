var starsContainer = document.querySelector('.stars');

for (var i = 0; i < 100; i++) {
    var star = document.createElement('div');
    star.className = 'star';
    star.style.top = Math.random() * 100 + '%';
    star.style.left = Math.random() * 100 + '%';
    var starSize = Math.random() * 5;
    star.style.width = starSize + 'px';
    star.style.height = starSize + 'px';
    starsContainer.appendChild(star);
}
