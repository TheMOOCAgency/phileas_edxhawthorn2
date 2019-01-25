$(document).ready(function() {
  // Get favorite + like counters
  $('#fav-counter').html(counter+`<img src="${etoile_src}"/>`);

  // Flip cards effect
  $('.flip-container').hover(function(){
    $(this).toggleClass("applyflip");
  });
  // Dropdown filter behavior
  $('.dropdown-container > button').click(function(){
    $('.dropdown').toggleClass("is-down");
  });

  // Click favorite pin
  $('.pin.favorite').click(function(){
    var courseId = $(this).parent().attr('class').split(' ')[2];
    // Escape special characters for jQuery selecting
    var courseSelector = courseId.replace(':', '\\:').replace(/\+/gi,'\\+');
    // Change pins color
    $('.'+ courseSelector + ' > .favorite').toggleClass('fav-off fav-on');
    // New status
    var status;
    if ($(this).hasClass('fav-on')) {
      status = true;
      counter++
      $('#fav-counter').html(counter+`<img src="${etoile_src}"/>`);
    } else {
      status = false;
      counter--
      $('#fav-counter').html(counter+`<img src="${etoile_src}"/>`);
    }

    // Send new favorite status to update db
    if(status){
    $.ajax({
      type: 'POST',
      url: '/tma_apps/'+ courseId +'/favourite/update_favourite',
      dataType: 'json',
      data: {status: status, course_id: courseId},
      success: function(data){
      }
    });

    }
  });

  // Click like pin
  $('span.like').click(function(){
    var courseId = $(this).parent().attr('class').split(' ')[2];
    // Escape special characters for jQuery selecting
    var courseSelector = courseId.replace(':', '\\:').replace(/\+/gi,'\\+');
    // Change pins class
    $('.'+ courseSelector + ' > .like').toggleClass('like-false like-true');

    var status;
    var likeCounter = $('.'+ courseSelector + ' .like-count').text()
    if ($(this).hasClass('like-true')) {
      status = true;
      likeCounter++;
      $('.'+ courseSelector + ' .like-count').text(likeCounter);
    } else {
      status = false;
      likeCounter--;
      $('.'+ courseSelector + ' .like-count').text(likeCounter);
    }
        $.ajax({
          type: 'POST',
          url: '/tma_apps/'+ courseId +'/like/update_like',
          dataType: 'json',
          data: {status: status, course_id: courseId},
          success: function(data){
          }
        });
  });


  //Enroll when click on vodeclic courses join because no course about page
  $('.vodeclick_register').on('click', function(){
    let course_id=$(this).data('vodeclic-id')
    $.post("/change_enrollment", {"enrollment_action": "enroll","course_id":course_id})
  })

});
