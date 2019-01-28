
let change_social_attributes =  function(element, social_attribute){
  let courseId = element.parent().data('course-id');
  console.log(courseId)
  let courseSelector = courseId.split('+').join('').split(':').join('');
  console.log('.'+ courseSelector + ' > .'+social_attribute)

  $('.'+ courseSelector + ' > .'+social_attribute).each(function(){
    $(this).toggleClass(`${social_attribute}-off ${social_attribute}-on`);
  })
  if (element.hasClass(`${social_attribute}-on`)){
    status=true;
  }
  else{
    status=false;
  }
  $.ajax({
    type: 'POST',
    url: '/tma_apps/'+ courseId +'/'+social_attribute+'/update_'+social_attribute,
    dataType: 'json',
    data: {status: status, course_id: courseId},
    success: function(data){
    }
  });
}

$('.pin.favorite').on('click',function(){
  console.log('clicked favorite');
  change_social_attributes($(this),'favorite');
});

$('.pin.like').click(function(){
  console.log('clicked-like');
  change_social_attributes($(this),'like')
});
