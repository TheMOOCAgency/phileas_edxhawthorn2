/************ ON PAGELOAD ************/
$(document).ready(function(){
  get_user_grade();
  styleAlreadyAnsweredQuestions();
  highlightChoices();

  $(document).ajaxSuccess(function(e, xhr, settings) {
    /* Each time a problem is submitted */
    if (settings.url.indexOf('problem_check') > -1) {
      // Update student grade
      get_user_grade();
      // Style according to result
      var data = JSON.parse(xhr.responseText);
      styleQuizOnSubmit(data, settings.url);
      highlightChoices();
    }
    /* When passing from unit to another (no reload) */
    if (settings.url.indexOf('goto_position') > -1) {
      // Restyle buttons
      $(this).find('label').each(function(){
        restyleButtons($(this));
      });
      // If already answered question, style accordingly
      styleAlreadyAnsweredQuestions();
      highlightChoices();
    }
  });
});

/************ END DOCUMENT READY ************/

/************ FUNCTIONS ************/
function highlightChoices() {
  // Highlight selected multiple choices
  $('input[type="checkbox"]').on('click', function(e){
    if ($(this).prop('checked')) {
      $(this).parent().css({'backgroundColor':'#00A1E9','color': 'rgb(255, 255, 255)'});
      if ($(this).parent().children('.checkfail').is(':visible')) {
        $(this).parent().children('.checkfail').hide();
      }
      if ($(this).parent().children('.checksuccess').is(':visible')) {
        $(this).parent().children('.checksuccess').hide();
      }
    } else {
      $(this).parent().css({'backgroundColor':'transparent','color': '#313131'})
      if ($(this).parent().children('.checkfail').is(':visible')) {
        $(this).parent().children('.checkfail').hide();
      }
      if ($(this).parent().children('.checksuccess').is(':visible')) {
        $(this).parent().children('.checksuccess').hide();
      }
    }
  });
  
  // Highlight selected unique choice
  $('input[type="radio"]').on('change', function(e){
      $(this).prop('checked') ? $(this).parent().addClass('selected-tma') : $(this).parent().removeClass('selected-tma');
  });
};

function styleAlreadyAnsweredQuestions() {
  $('.problems-wrapper').each(function() {
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
      if ($(this).find('.tma-attempts').attr('data-remaining') <= 0){
        showAnswers(url, questionId);
        $(this).css('pointer-events', 'none');
      }
    } else {
      if (indicatorContainer.hasClass('correct')  || goodChoice.length > 0) {
        $(this).addClass('tma-success').addClass('tma-answered');
        problemTitle.html(problemTitle.html()+' <i style="color:#6ac259;" class="fas fa-check"></i>');
        $('#'+ questionId).find('label > input:checked ~ .checksuccess').show();
        showAnswers(url, questionId);
        if ($(this).find('.tma-attempts').attr('data-remaining') <= 0){
          $(this).css('pointer-events', 'none');
        }
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
    if (($('#'+ questionId).find('.tma-attempts').attr('data-remaining') <= 0) || ($('#'+ questionId).find('.tma-attempts').length == 0)) {
      showAnswers(url, questionId);
      $('#'+ questionId).css('pointer-events', 'none');
    }
  } else {
    // If correct answer : green icon
    if (data['success'] == 'correct') {
      problemTitle.html(problemTitle.html()+' <i style="color:#6ac259;" class="fas fa-check"></i>');
      $('#'+ questionId).find('label > input:checked ~ .checksuccess').show();
      // Mark question as answered and success
      $('#'+ questionId).addClass('tma-success').addClass('tma-answered');

      if ($('#'+ questionId).find('.tma-attempts').attr('data-remaining') <= 0) {
        $('#'+ questionId).css('pointer-events', 'none');
      }
    }
  }
  //Update progress to get points
  $('#'+questionId).attr('data-problem-score', data['current_score']);
}

function restyleButtons(element) {
  // Checkmarks only for inputs radio or checkboxes
  if (element.children().is('input[type="radio"]')) {
    element.append('<span class="checkmark"><svg height="30" width="30"><circle cx="15" cy="15" r="14" shape-rendering="crispEdges" stroke="#eee" stroke-width="1" fill="#eee" /></svg></span>');
    element.append("<span class='checkfail'><img src='/static/tma-static/images/checkfail.png' /></span>");
    element.append("<span class='checksuccess'><img src='/static/tma-static/images/checksuccess.png' /></span>");
  } else {
    if (element.children().is('input[type="checkbox"]')) {
      element.append('<span class="checkmark"><svg height="30" width="30"><rect x="2" y="2" height="25" width="25" shape-rendering="crispEdges" stroke="#eee" stroke-width="1" fill="#eee"></rect></svg></span>');
      element.append("<span class='checkfail'><img src='/static/tma-static/images/checkbox-fail.png' /></span>");
      element.append("<span class='checksuccess'><img src='/static/tma-static/images/checkbox-success.png' /></span>");
    }
  }
};

function showAnswers(url, id){
  $.ajax({
    url: url,
    type: 'POST',
    dataType: 'json',
    success : function(data){
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
        if($("#"+ id).find('.tma-attempts').attr('data-remaining') <= 0){
          $("#"+ id).addClass('show-detailed');
          $(this).css('pointer-events', 'none');
        }
    }
  });
};

function displayFinalFeedback(){
  var allAnswered = true;
  finalScore = {scoreUser: 0,scoreTotal: 0}
  $('.problems-wrapper').each(function(){
    if(!$(this).hasClass('tma-answered')){
      allAnswered = false;
    } else {
      // Count points
      finalScore.scoreUser += parseInt($(this).attr('data-problem-score'));
      finalScore.scoreTotal += parseInt($(this).attr('data-problem-total-possible'));
    }
  });
  if (allAnswered) {
    get_user_grade(finalScore);
    return true;
  } else {
    return false;
  }
}

function failedFeedback(response) {
  $('#tma-feedback-fail').show();
  $('#tma-feedback-success').hide();
  $('#tma-feedback-fail').css('border','2px solid red');
  $('#tma-feedback-fail .score-user-percent').text(Math.round(response['user_grade'] * 100));
  $('#tma-feedback-fail .score-percent').text(Math.round(response['required_score'] * 100));
};

function successFeedback(finalScore, response) {
  $('#tma-feedback-success').show();
  $('#tma-feedback-fail').hide();
  $('#tma-feedback-success').css('border','2px solid #008100');
  $('#tma-feedback-success .score-user').text(finalScore.scoreUser);
  $('#tma-feedback-success .score-total').text(finalScore.scoreTotal);
  $('#tma-feedback-success .score-percent').text(Math.round(response['user_grade'] * 100));
};

function get_user_grade(finalScore){
  url ='/tma_apps/'+ global_courseid +'/grade_tracking/get_user_grade'
  $.ajax({
    type: 'GET',
    url: url,
    success : function(response) {
      // Get grade for displaying final feedback message
      if (finalScore) {
        if (response['passed']) {
          successFeedback(finalScore, response);
        } else {
          failedFeedback(response);
        }
      } else {
        // Get user grade for tracking current score top of page
        if (response['status'] == 'success') {
          user_grade = Math.round(response['user_grade'] * 100);
          $('#tma-grade-value').html(user_grade)
        }
      }
    }
  });
};