/*Toggle Menu*/
$('span.open-courseware-nav').on('click', function(){
  $('#tma-completion-nav').removeClass('folded');
  $('.open-courseware-nav').hide();
})
$('button.close-courseware-nav').on('click', function(){
  $('#tma-completion-nav').addClass('folded');
  $('.open-courseware-nav').show();
})


/*Prepare completion coursenav on pageload */
$(document).ready(function(){
  mark_started_subsections();
  get_course_completion()
})

/*Update completion coursenav between units*/
$(document).ajaxSuccess(function(e, xhr, settings) {
  if (settings.url.indexOf('get_completion')>-1) {
    response=JSON.parse(xhr.responseText);
    mark_started_subsections();
    if(response['complete']){
      unit_id=settings.data.replace('usage_key=','');
      mark_unit_completed(decodeURIComponent(unit_id));
    }
    get_course_completion()
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
