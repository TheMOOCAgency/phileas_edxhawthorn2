// THIS SCRIPT IS ALSO USED IN COURSES.HTML

$(document).ready(function() {
  // Flip cards effect
  $('.flip-container').hover(function(){
    $(this).toggleClass("applyflip");
  });
  // Dropdown filter behavior
  $('.dropdown-container > button').click(function(){
    $('.dropdown').toggleClass("is-down");
  });
});
