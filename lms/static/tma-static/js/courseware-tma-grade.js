/************ ON PAGELOAD ************/
$(document).ready(function(){
  get_user_grade();
  styleAlreadyAnsweredQuestions();

  /* Update user grade and get Phileas styling when submitting exercise */
  $(document).ajaxSuccess(function(e, xhr, settings) {
    if (settings.url.indexOf('problem_check') >- 1) {
      get_user_grade();
      var data = JSON.parse(xhr.responseText);
      styleQuizOnSubmit(data, settings.url);
    }
  });

  // Color highlight of questions choices - TO FIX: WHY DOUBLE CLICK ?
  $('span.checkmark').on('click', function(){
    $(this).parents('.problem').find('label').each(function(){
      $(this).removeClass('selected-tma');
    });
    $(this).parent('label').addClass('selected-tma');
  });
  $('label').on('click', function(){
    $(this).parents('.problem').find('label').each(function(){
      $(this).removeClass('selected-tma');
    });
    $(this).addClass('selected-tma');
  });


});
/************ END DOCUMENT READY ************/

/************ FUNCTIONS ************/
function styleAlreadyAnsweredQuestions(){
  $('.problems-wrapper').each(function(){
    indicatorContainer = $(this).find('.indicator-container span');
    wrongChoice = $(this).find('.choicegroup_incorrect');
    goodChoice = $(this).find('.choicegroup_correct');
    problemTitle = $(this).find('.problem-header');
    questionId = $(this).attr('id');
    url = $(this).attr('data-url')+ "/problem_show";

    // Restyle buttons
    $(this).find('label').each(function(){
      restyleButtons($(this));
    });

    if (indicatorContainer.hasClass('incorrect') || wrongChoice.length > 0) {
      $(this).addClass('tma-fail').addClass('tma-answered');
      problemTitle.html(problemTitle.html()+ ' <i style="color:red;" class="fa fa-times"></i>');
      $('#'+ questionId).find('label > input:checked ~ .checkfail').show();

      // For failed quiz only show answers on last attempts
      if ($(this).find('.submission-feedback').attr('data-remaining') <= 0){
        showAnswers(url, questionId);
      }
    } else {
      if (indicatorContainer.hasClass('correct')  || goodChoice.length > 0) {
        $(this).addClass('tma-success').addClass('tma-answered');
        problemTitle.html(problemTitle.html()+' <i style="color:green;" class="fas fa-check"></i>');
        $('#'+ questionId).find('label > input:checked ~ .checksuccess').show();
        showAnswers(url, questionId);
      }
    }
  });
};

function styleQuizOnSubmit(data, url) {
  var questionId = "problem_"+ url.split('block@')[1].split('/');
  var problemTitle = $('#'+ questionId).find('.problem-header');
  url = url.replace('/problem_check','')+'/problem_show';

  //Add custom checkmark
  $("#"+ questionId).find('label').each(function(){
    restyleButtons($(this));
  });

  // If incorrect answer : red icon on title
  if (data['success'] == 'incorrect') {
    problemTitle.html(problemTitle.html() + ' <i style="color:red;" class="fa fa-times"></i>');
    $('#'+ questionId).find('label > input:checked ~ .checkfail').show();
    // Mark question as answered and failed
    $('#'+ questionId).addClass('tma-fail').addClass('tma-answered');

    // If no more attempts available OR illimited attempts : show right answers
    if (($('#'+ questionId).find('.submission-feedback').attr('data-remaining') <= 0) || ($('#'+ questionId).find('.submission-feedback').length == 0)) {
      showAnswers(url, questionId);
    }
  } else {
    // If correct answer : green icon
    if (data['success'] == 'correct') {
      problemTitle.html(problemTitle.html()+' <i style="color:green;" class="fas fa-check"></i>');
      $('#'+ questionId).find('label > input:checked ~ .checksuccess').show();
      // Mark question as answered and success
      $('#'+ questionId).addClass('tma-success').addClass('tma-answered');
    }
  }
}

function restyleButtons(that) {
  that.append('<span class="checkmark"><svg height="30" width="30"><circle cx="15" cy="15" r="14" shape-rendering="crispEdges" stroke="#eee" stroke-width="1" fill="#eee" /></svg></span>');
  that.append("<span class='checkfail hide'><img src='/static/tma-static/images/checkfail.png' /></span>");
  that.append("<span class='checksuccess hide'><img src='/static/tma-static/images/checksuccess.png' /></span>");
};

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
        if($("#"+ id).find('.submission-feedback').attr('data-remaining')<=0){
          $("#"+ id).addClass('show-detailed');
        }
    }
  });
};

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
};