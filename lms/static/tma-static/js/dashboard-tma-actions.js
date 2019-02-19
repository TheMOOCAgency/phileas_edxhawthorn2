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

  //Enroll when click on vodeclic courses join because no course about page
  $('.vodeclick_register').on('click', function(){
    let course_id = $(this).data('vodeclic-id')
    $.post("/change_enrollment", {"enrollment_action": "enroll","course_id":course_id})
    ongoing_counter = parseInt($('#ongoin-counter-number').html());
    $('#ongoin-counter-number').html(ongoing_counter+1)
  });

  // Random banner display
  const randomBanner = function() {
    randomNumber = Math.floor(Math.random()*3); 
    if (randomNumber == 1) {
      $('video').hide();
      $('.gif-box').addClass('col-lg-6').css('position', 'initial');
      $('.header-box').show().css('padding', '0px').addClass('header-man');
    } else {
      if (randomNumber == 2) {
        $('video').hide();
        $('.gif-box').addClass('col-lg-6').css('position', 'initial');
        $('.header-box').show().css('padding', '0px').addClass('header-woman');
      } else {
        $('video').show();
        $('.gif-box').removeClass('col-lg-6').css({'position':'absolute', 'background-color':'transparent'});
        $('.header-box').hide();
      }
    }
  }();
});
