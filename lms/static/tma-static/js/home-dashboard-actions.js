// Like
$('.pin.like').click(function(){
  current_count=parseInt($(this).parent().find('.like_count').html());
  console.log(current_count)
  if($(this).hasClass('like-off')){
    $(this).parent().find('.like_count').html(current_count+1);
    //$(".like_count_"+enrolment_id).each(function(){$(this).html(current_count+1);});
  }else{
    $(this).parent().find('.like_count').html(current_count-1);
    //$(".like_count_"+enrolment_id).each(function(){$(this).html(current_count-1);});
  }
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
