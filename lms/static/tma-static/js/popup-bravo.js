
  $(document).ajaxSuccess(function(e, xhr, settings) {
  if (settings.url.indexOf('get_user_grade')>-1) {
    response=JSON.parse(xhr.responseText);
    if(response['popup_text'] && response['popup_title']){
      console.log('bravo')
      certificate_url ='/tma_apps/'+global_courseid+"/certificate/render"
      $('#tma_course_end_popup a').attr("href",certificate_url)
      $('#tma_course_end_popup .modal-body h5').html(response['popup_title'])
      $('#tma_course_end_popup .modal-body p').html(response['popup_text'])
      $('#tma_course_end_popup').modal('show')
      mark_popup_as_displayed();
    }
  }
});

  function mark_popup_as_displayed(){
    url ='/tma_apps/'+global_courseid+'/grade_tracking/message_displayed'
    $.ajax({
      type:'post',
      url:url,
      data:{
        'message_displayed_status':'True'
      },
    })
  }
