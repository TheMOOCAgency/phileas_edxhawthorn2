/* Hide Previous & Next buttons if has_menu = false */
if (hasMenu == 'False') {
  $('button.sequence-nav-button.button-previous').hide();
  $('button.sequence-nav-button.button-next').hide();
}

/*Toggle Menu*/
$('span.open-courseware-nav').on('click', function(){
  $('#tma-completion-nav').removeClass('folded');
  $('.open-courseware-nav').addClass('tma-visibility-hidden');
})
$('button.close-courseware-nav').on('click', function(){
  $('#tma-completion-nav').addClass('folded');
  $('.open-courseware-nav').removeClass('tma-visibility-hidden');
})
$('.xmodule_display.xmodule_SequenceModule .sequence-bottom .sequence-nav-button').on('click',function(){
  $('#tma-completion-nav').addClass('folded');
  $('.open-courseware-nav').removeClass('tma-visibility-hidden');
  close_all_subsections();
})

/*Prepare completion coursenav on pageload */
$(document).ready(function(){
  // Open menu when landing on page if coming from course_about
  if ((document.referrer.indexOf('/about') > -1) && hasMenu == 'True') {
    $('#tma-completion-nav').removeClass('folded');
    $('.open-courseware-nav').addClass('tma-visibility-hidden');
  };
  mark_started_subsections();
  get_course_completion();
  // Check user completion status for popup bravo, for ungraded courses with no exercises
  get_user_grade()
  close_all_subsections();
})

/*Update completion coursenav between units*/
$(document).ajaxSuccess(function(e, xhr, settings) {
  if (settings.url.indexOf('publish_completion')>-1 || settings.url.indexOf('goto_position')>-1) {
    response=JSON.parse(xhr.responseText);
    mark_started_subsections();
    unit_id=$('.xblock.xblock-student_view.xblock-student_view-vertical.xblock-initialized').data('usage-id');
    mark_unit_completed(unit_id);
    get_course_completion()

    // Check user completion status for popup bravo, for ungraded courses with no exercises
    get_user_grade()
  }
});

function mark_started_subsections(){
  $('.subsection.accordion').each(function(){
    subsection_started=false;
    $(this).find('.accordion-panel .vertical-title').each(function(){
      if($(this).hasClass('tma_completed')){
        subsection_started=true;
      }
    })
    if(subsection_started && !$(this).find('.subsection-title').hasClass('tma_completed')){
      $(this).find('.subsection-title').addClass('tma_started')
    }
  })
}

function mark_unit_completed(unit_id){
  $('#' + unit_id.replace(/([$%&()*+,./:;<=>?@\[\\\]^\{|}~])/g,'\\$1')).find('.vertical-title').addClass('tma_completed');
}


function get_course_completion(){
  url ='/tma_apps/'+global_courseid+'/completion/get_course_completion'
  $.ajax({
    type:'get',
    url:url,
    success : function(response) {
      completion_rate =Math.round(response.completion_rate*100)
      $('#tma-completion-value').html(completion_rate+'%')
      if (completion_rate!=0){
        $('#tma-completion-progress').css('width',completion_rate+'%').addClass('primary-color-bg')
      }
    }
  })
}

// On  Menu close close all subsections - On menu open open current subsection
$('#tma-completion-nav .close-courseware-nav').on('click', function(){
  close_all_subsections();
})

function close_all_subsections(){
  $('#tma-completion-nav .subsection .outline-item.accordion-panel').each(function(){
    $(this).addClass('is-hidden');
  })
  $('#tma-completion-nav .fa-chevron-right').each(function(){
    $(this).removeClass('fa-rotate-90');
  })
  $('.tma-current-unit').each(function(){
    $(this).removeClass('tma-current-unit')
  })
}

$('.open-courseware-nav').on('click', function(){
  highlight_current_unit();
})

function highlight_current_unit(){
  unit_id=$('.xblock.xblock-student_view.xblock-student_view-vertical.xblock-initialized').data('usage-id');
  $('#' + unit_id.replace(/([$%&()*+,./:;<=>?@\[\\\]^\{|}~])/g,'\\$1')).addClass('tma-current-unit');
  $('#' + unit_id.replace(/([$%&()*+,./:;<=>?@\[\\\]^\{|}~])/g,'\\$1')).parents('.accordion-panel').removeClass('is-hidden');
  $('#' + unit_id.replace(/([$%&()*+,./:;<=>?@\[\\\]^\{|}~])/g,'\\$1')).parents('li.accordion').find('.fa-chevron-right ').addClass('fa-rotate-90');
}
