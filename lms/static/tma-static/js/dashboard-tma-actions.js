// THIS SCRIPT IS ALSO USED IN COURSES.HTML
const flipEffect = function() {
  $('.flip-container').hover(function(){
    $(this).toggleClass("applyflip");
  });
};

$(document).ready(function() {
  // Flip effect
  flipEffect();

  // Dropdown filter behavior
  $('.dropdown-container > button').click(function(){
    $('.dropdown').toggleClass("is-down");
  });

  // Random banner display
  const randomBanner = function() {
    randomNumber = Math.floor(Math.random()*3); 
    if (randomNumber == 1) {
      $('video').hide();
      $('.gif-box').addClass('col-lg-6').css('position', 'relative');
      $('.header-box').show().css('padding', '0px').addClass('header-man');
    } else {
      if (randomNumber == 2) {
        $('video').hide();
        $('.gif-box').addClass('col-lg-6').css('position', 'relative');
        $('.header-box').show().css('padding', '0px').addClass('header-woman');
      } else {
        $('video').show();
        $('.gif-box').removeClass('col-lg-6').css({'position':'absolute', 'background-color':'transparent'});
        $('.header-box').hide();
      }
    }
  }();
});
