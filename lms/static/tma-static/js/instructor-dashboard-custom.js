"use strict";

const getLightDashboard = function() {
    // Relocate
    window.location.hash = '#view-membership';
    // Remove active class on all sections except membership
    $('#course_info, #cohort_management, #discussions_management, #student_admin, #data_download, #instructor_analytics').removeClass('active-section');
    // Add active class on membership
    $('#membership').addClass('active-section');
    // Hide section titles + membership titles + other stuff
    $('.course_info, .cohort_management, .discussions_management, .student_admin, .data_download, .instructor_analytics').hide();
    $('.role, .enroll-option, .enrollment-button[data-action="unenroll"], .batch-beta-testers, .member-lists-management, hr.divider, #header-membership, #heading-batch-enrollment').hide();
};

$(document).ready(function(){
    const date = new Date()
    // Autofill reason field for membership section
    $('#reason-field-id').text('User enrolled - '+ date.getDate()+'-'+(date.getMonth()+1)+'-'+date.getFullYear())

    // Light dashboard by default
    window.location.hash = '#view-membership';
    $('.switch-instructor > input[type="checkbox"]').prop('checked', true);
    getLightDashboard();

    // On click get light or full dashboard
    $('.switch-instructor').on('click', function(){
        $('.switch-instructor > input[type="checkbox"]').prop('checked', !$('.switch-instructor > input[type="checkbox"]').prop('checked'));

        if ($('.switch-instructor > input[type="checkbox"]').prop('checked')) {
        getLightDashboard();
        } else {
        $('.course_info, .cohort_management, .discussions_management, .student_admin, .data_download, .instructor_analytics').show();
        $('.role, .enroll-option, .enrollment-button[data-action="unenroll"], .batch-beta-testers, .member-lists-management, hr.divider, #header-membership, #heading-batch-enrollment').show();
        }
    });
});