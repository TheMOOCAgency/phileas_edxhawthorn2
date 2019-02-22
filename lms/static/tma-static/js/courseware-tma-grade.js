/*Get user grade on pageload */
$(document).ready(function(){
  get_user_grade()

  /*
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
      }
    })
  });
  */
});

/*Update user grade when submitting exercise*/
$(document).ajaxSuccess(function(e, xhr, settings) {
  if (settings.url.indexOf('problem_check')>-1) {
    get_user_grade()
  }
});


function get_user_grade(){
  url ='/tma_apps/'+global_courseid+'/grade_tracking/get_user_grade'
  $.ajax({
    type:'get',
    url:url,
    success : function(response) {
      if(response['status']=='success'){
        user_grade=Math.round(response['user_grade']*100)
        $('#tma-grade-value').html(user_grade)
      }
    }
  })
}
