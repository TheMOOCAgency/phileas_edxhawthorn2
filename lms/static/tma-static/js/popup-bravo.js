$(document).ajaxSuccess(function(e, xhr, settings) {
  // Course with quiz or SCORM
  if (settings.url.indexOf('get_user_grade') >- 1) {
    response = JSON.parse(xhr.responseText);
    console.log(response)
    // If course is completed
    if (response['has_completed'] && !response['has_displayed_message']) {
      // If course is graded & success
      if (response['graded_success']) {
        console.log('cours noté - bravo')
        certificate_url = '/tma_apps/'+global_courseid+"/certificate/render"
        $('.modal-graded-success a').attr("href",certificate_url)
        $('.modal-graded-success .score').html(response['user_grade']*100)
        $('.modal-graded-success').show();
        $('#tma_course_end_popup').modal('show')
        mark_popup_as_displayed('True');
      } else {
        // If failure
        console.log('cours noté - sorry')
        reset_url = ""
        $('.modal-graded-fail a').attr("href",reset_url)
        $('.modal-graded-fail .score').html(response['user_grade']*100)
        // If quiz has limited attempts : no retry possible
        if (!canRetry) {
          $('#try_again').hide();
        }
        $('.modal-graded-fail').show();
        $('#tma_course_end_popup').modal('show')
        mark_popup_as_displayed('True');
      }
    } else {
      // If course is not graded && completed
      if (response['not_graded_success'] && !response['has_displayed_message']) {
        console.log('cours non noté - bravo');
        $('.modal-not-graded-success').show();
        $('#tma_course_end_popup').modal('show');
        mark_popup_as_displayed('True');
      }
    }
  }
});


$('button.mark-as-done').on('click', function(e){
  e.preventDefault();
  mark_as_done();
  $('#tma_course_end_popup').modal('hide');
});

// If student has failed clicks "Start over" button
$('#try_again').on('click', function(e){
  e.preventDefault();
  $.ajax({
    type:'POST',
    url: '/tma_apps/'+global_courseid+'/grade_tracking/try_again',
    data: {
      'message_displayed_status': 'False'
    },
    success : function(response) {
      console.log(response);
      $('#tma_course_end_popup').modal('hide');
      mark_popup_as_displayed('False');
      location.reload();
    }
  })
});

function mark_popup_as_displayed(status){
  url ='/tma_apps/'+global_courseid+'/grade_tracking/message_displayed'
  $.ajax({
    type:'post',
    url:url,
    data:{
      'message_displayed_status': status
    }
  });
}

function mark_as_done() {
  url ='/tma_apps/'+global_courseid+'/grade_tracking/mark_as_done'
  $.ajax({
    type: 'POST',
    url: url,
    data: {
      'marked_as_done':'True'
    },
    success: function(){
      window.location.assign("/tma_apps/dashboard/home/");
    }
  });
}

