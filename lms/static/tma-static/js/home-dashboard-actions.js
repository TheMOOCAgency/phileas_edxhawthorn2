// Load finished courses 5 by 5
var currentIndex = 5
// Only show 5
$('.finished').hide();
$('.finished').slice(0, 5).show();
// On click, show 5 more, and if no more to show, hide button
function loadMore() {
    $('.finished').slice(0, currentIndex + 5).show();
    currentIndex += 5;
    if ($('.finished:hidden').length == 0) {
        $('.more-btn').hide();
    }
};

function popupOpenClose(popup) {
    /* Add div inside popup for layout if one doesn't exist */
    if ($(".wrapper").length == 0){
        $(popup).wrapInner("<div class='wrapper'></div>");
    }
    /* Open popup */
    $(popup).show();
    /* Close popup if user clicks on background */
    $(popup).click(function(e) {
        if (e.target == this) {
            if ($(popup).is(':visible')) {
                $(popup).hide();
            }
        }
    });

    /* Close popup and remove errors if user clicks on cancel or close buttons */
    $(popup).find("img.close-box").on("click", function() {
        if ($(".formElementError").is(':visible')) {
            $(".formElementError").remove();
        }
        $(popup).hide();
    });
}

$(document).ready(function () {
    $("[data-js=open]").on("click", function() {
        popupid = $(this).data('popup-id');
        popupOpenClose($(".popup-"+popupid));
    });

    // Unenroll button
    $(".tma_unenroll_student").on("click", function() {
        course_id=$(this).data('course-to-uneroll');
        // also remove from favorites
        let update_info = change_social_attributes($(this),'favorite');
        $.post("/change_enrollment", {"enrollment_action": "unenroll","course_id":course_id}, function(){window.location.reload()})
        console.log(update_info)
    });

    // Remove from favorites button
    $(".tma_unfav").on("click", function() {
        course_id=$(this).data('course-to-unfav');
        let update_info = change_social_attributes($(this),'favorite');
        console.log(update_info)
    });
});
