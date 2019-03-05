/*Get user grade on pageload */
$(document).ready(function(){
  get_user_grade()
});

/*Update user grade and get Phileas styling when submitting exercise*/
$(document).ajaxSuccess(function(e, xhr, settings) {
  if (settings.url.indexOf('problem_check') >- 1) {
    get_user_grade();
    var data = JSON.parse(xhr.responseText);
    var questionId ="problem_"+settings.url.split('block@')[1].split('/');
    var problemTitle=$('#'+questionId).find('.problem-header');
    var url = settings.url.replace('/problem_check','')+'/problem_show'
    
    // If wrong answer, update quiz status as failed and show right answer(s)
    if (data['success'] == 'incorrect') {
      if (problemTitle.html().indexOf('<i') < 0){
        problemTitle.html(problemTitle.html()+' <i style="color:red;" class="fa fa-times"></i>').addClass('failed_quiz');
        $('#'+ questionId).addClass('failed_quiz').addClass('answered_tma');
      }
      if (($('#'+ questionId).find('.attempts_tma').attr('data-remainingattp') <= 0) || ($('#'+ questionId).find('.attempts_tma').length == 0)){
        showAnswers(url, questionId);
      }
    }
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

function showAnswers(url, id){
  $.ajax({
    url: url,
    type: 'POST',
    dataType: 'json',
    success : function(data){
      console.log(data)
      // prepare answers
      answers = data['answers'];
        $.each(answers, function(key, value) {
          if ($.isArray(value)) {
            for (i = 0, len = value.length; i < len; i++) {
              $('#'+ id).find('input[value='+value[i]+']').parent('label').addClass('choicegroup_correct');
            }
          } else {
            if (key.indexOf('solution') > 0){
              $('#'+ id).find('.problem').after(value);
            }
          }
        });
        //All other answers are false
        $('#'+ id).find('label').each(function(){
          if(!$(this).hasClass('choicegroup_correct') && $(this).find('input').is(':checked')){
            $(this).addClass('choicegroup_incorrect');
          }
        })
        //Disable submit button
        $('#'+ id).find('.action .check').addClass('is-disabled');
        //Display detailed solution if last attempt
        if($("#"+ id).find('.attempts_tma').attr('data-remainingattp')<=0){
          $("#"+ id).addClass('show-detailed');
        }
    }
  });
}