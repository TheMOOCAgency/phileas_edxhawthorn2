// Like
$('.like_picto').click(function(){
  var enrolment_id = 0;
  var classList = $(this).attr('class').split(/\s+/);
  $.each(classList, function(index, item) {
      if (item.indexOf('like_picto_') > -1) {
          enrolment_id = item.split('_')[2];
      }
  });
  var courseId =$(this).attr('data-course-id');
  var current_count = parseInt($(".like_count_"+enrolment_id).first().html());
  var status = $(this).hasClass('like_false');
  if($(this).hasClass('like_false')){
    $(".like_count_"+enrolment_id).each(function(){$(this).html(current_count+1);});
    $(".like_picto_"+enrolment_id).each(function(){$(this).toggleClass("like_false like_true");});
  }else{
    $(".like_count_"+enrolment_id).each(function(){$(this).html(current_count-1);});
    $(".like_picto_"+enrolment_id).each(function(){$(this).toggleClass("like_true like_false");});
  }
  $.ajax({
    type: 'POST',
    url: '/tma_apps/'+ courseId +'/like/update_like',
    dataType: 'json',
    data: {status: status, course_id: courseId},
    success: function(data){
    }
  });
});

function popupOpenClose(popup) {
    /* Add div inside popup for layout if one doesn't exist */
    if ($(".wrapper").length == 0){
        $(popup).wrapInner("<div class='wrapper'></div>");
    }
    /* Open popup */
    $(popup).show();
    /* Close popup if user clicks on background */
    $(popup).click(function(e) {
        if ( e.target == this ) {
            if ($(popup).is(':visible')) {
                $(popup).hide();
            }
        }
    });

    /* Close popup and remove errors if user clicks on cancel or close buttons */
    $(popup).find("button[name=close]").on("click", function() {
        if ($(".formElementError").is(':visible')) {
            $(".formElementError").remove();
        }
        $(popup).hide();
    });
}

$(document).ready(function () {
    $("[data-js=open]").on("click", function() {
        popupOpenClose($(".popup"));
    });
    $(".tma_unenroll_student").on("click", function() {
        course_id=$(this).data('course-to-uneroll')
        $.post("/change_enrollment", {"enrollment_action": "unenroll","course_id":course_id})
    });
    //Enroll when click on vodeclic courses join because no course about page -> USEFUL FOR FAVORITES which are not always active enrollments
    $('.vodeclick_register').on('click', function(){
      let course_id=$(this).data('vodeclic-id')
      $.post("/change_enrollment", {"enrollment_action": "enroll","course_id":course_id})
    })
});
