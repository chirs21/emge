var sticky = document.querySelector('.sticky-top');

if (sticky.style.position !== 'sticky') {
  var stickyTop = sticky.offsetTop;

  document.addEventListener('scroll', function () {
    window.scrollY >= 58 ?
      sticky.classList.add('fixedd') :
      sticky.classList.remove('fixedd');
  });
}

