$(document).ready(function() {

  $('.hamburger').click(function(e) {
     let startHeight = $('.start').innerHeight()
      $('.start').removeClass('start--min')
      $('.nav').toggleClass('nav--mobile')
      if (startHeight < 515) {
        $('.start').addClass('start--min')
      };
      e.preventDefault();
    });

  $(function () {
    let location = window.location.href;
    $('.nav__link').each(function () {
      let link = this.href;
      if(location == link) {
        $(this).addClass('nav__link--current');
      }
    });
    $('.header__btn').each(function () {
      let link = this.href;
      if(location == link) {
        $(this).addClass('header__btn--current');
      }
    });

  });
});
