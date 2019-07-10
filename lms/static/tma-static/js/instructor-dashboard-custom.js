"use strict";

const getLightDashboard = function() {
    window.location.hash = '#view-membership';
    $('#course_info, #cohort_management, #discussions_management, #student_admin, #data_download, #instructor_analytics').removeClass('active-section');
    $('#membership').addClass('active-section');
    $('.course_info, .cohort_management, .discussions_management, .student_admin, .data_download, .instructor_analytics').hide();
    $('.role, .enroll-option, .enrollment-button[data-action="unenroll"], .batch-beta-testers, .member-lists-management, hr.divider').hide();
};

$(document).ready(function(){
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
        $('.role, .enroll-option, .enrollment-button[data-action="unenroll"], .batch-beta-testers, .member-lists-management, hr.divider').show();
        }
    });
});