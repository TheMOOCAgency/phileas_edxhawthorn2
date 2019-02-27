$('#cards-box').on('click', '.pin.favorite' ,function(){
  let update_info = change_social_attributes($(this),'favorite');
  let favorite_counter=$('#favorite-counter-number');
  if(favorite_counter.length>0){
    update_counter(favorite_counter, update_info['status']);
  }
});

$('#cards-box').on('click', '.pin.like', function(){
  let update_info = change_social_attributes($(this), 'like');
  let like_counter= $('.'+update_info['courseSelector']+' .like_count');
  /*console.log('.'+update_info['courseSelector']+' .like_count');
  console.log(like_counter);*/
  update_counter(like_counter, update_info['status']);
});

let change_social_attributes =  function(element, social_attribute){
  let courseId = element.parent().data('course-id');
  let courseSelector = courseId.split('+').join('').split(':').join('');

  $('.'+ courseSelector + ' > .'+ social_attribute).each(function(){
    /*console.log('.'+ courseSelector + ' > .'+ social_attribute)*/

    $(this).toggleClass(`${social_attribute}-on ${social_attribute}-off`);
  });
  if (element.hasClass(`${social_attribute}-on`)){
    status = true;
  } else {
    status = false;
  }

  $.ajax({
    type: 'POST',
    url: '/tma_apps/'+ courseId +'/'+social_attribute+'/update_'+social_attribute,
    dataType: 'json',
    data: {status: status, course_id: courseId},
    success: function(data){
      console.log(data)
    }
  });

  return {
    status: status,
    courseSelector: courseSelector
  };
}

let update_counter = function(counter, status){
  let current_count=parseInt(counter.html());
  if (status=="true") {
    let new_count= current_count+1
    counter.html(new_count);
  } else {
    let new_count= current_count-1
    counter.html(new_count);
  }
}
