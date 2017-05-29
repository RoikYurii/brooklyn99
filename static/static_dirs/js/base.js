$(document).ready(function() {
  $('.hamburger').click(function(e) {
      $('.nav').toggleClass('nav--mobile')
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
