$(document).ready(function() {
  // Flip cards effect
  $('.flip-container').hover(function(){
    $(this).toggleClass("applyflip");
  });

  // Dropdown filter behavior
  $('.dropdown-container > button').click(function(){
    $('.dropdown').toggleClass("is-down");
  });

  //Enroll when click on vodeclic courses join because no course about page
  $('.vodeclick_register').on('click', function(){
    let course_id=$(this).data('vodeclic-id')
    $.post("/change_enrollment", {"enrollment_action": "enroll","course_id":course_id})
    ongoing_counter=parseInt($('#ongoin-counter-number').html());
    $('#ongoin-counter-number').html(ongoing_counter+1)
  })
});
