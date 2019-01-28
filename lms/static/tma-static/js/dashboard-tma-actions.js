$(document).ready(function() {
  // Get favorite + like counters
  //$('#fav-counter').html(counter+`<img src="${etoile_src}"/>`);

  // Flip cards effect
  $('.flip-container').hover(function(){
    $(this).toggleClass("applyflip");
  });
  // Dropdown filter behavior
  $('.dropdown-container > button').click(function(){
    $('.dropdown').toggleClass("is-down");
  });
});


$(document).ajaxSuccess(function(e, xhr, settings) {
  if (settings.url.indexOf('update_favorite')>-1) {
    response=JSON.parse(xhr.responseText);
    counter=parseInt($('#favorite-counter-number').html());
    if(response['status']){
      counter++;
    }
    else{
      counter--
    }
    $('#favorite-counter-number').html(counter);
  }
});

$(document).ajaxSuccess(function(e, xhr, settings) {
  if (settings.url.indexOf('update_like')>-1) {
    response=JSON.parse(xhr.responseText);
    counter=parseInt($('.pictos-box .'+response['course_id'].replace(':','').replace('+','')+' .like-count').html());
    if(response['status']){
      counter++;
    }
    else{
      counter--
    }
    $('.pictos-box .'+response['course_id'].replace(':','').replace('+','')+' .like-count').html(counter);
  }
});
