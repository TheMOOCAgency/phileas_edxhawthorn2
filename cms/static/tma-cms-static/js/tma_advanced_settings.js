// JSON VALIDATOR
const jsonValidator = function(json) {
    try {
        JSON.parse(json);
    } catch (e) {
        return false;
    }
    return true;
};

// REQUIREJS FUNCTION FOR FEEDBACK
(function() {
    'use strict';
    define(["js/views/validation",
            "jquery",
            "underscore",
            "gettext",
            "js/views/modals/validation_error_modal",
            'edx-ui-toolkit/js/utils/html-utils'],
    function(ValidatingView, $, _, gettext, ValidationErrorModal, HtmlUtils)  {
        var title = gettext("Your policy changes have been saved.");
        var message = gettext("No validation is performed on policy keys or value pairs. If you are having difficulties, check your formatting.");
        var error_message = gettext("Please enter valid JSON content.");
        var validationView = new ValidatingView();

         $(document).ready(function() {
            // Amundi settings update function
            const updateSettings = function(){
                var formData = $('#settings').serializeArray();
                var custom_settings = {};
                for (var i = 0; i < formData.length; i++) {
                    custom_settings[formData[i]['name']] = formData[i]['value']
                }

                // Update course info only if course_about JSON is valid 
                if (!jsonValidator(custom_settings.course_about)) {
                    $('#error-json').text(error_message).show();
                } else {
                    console.log(custom_settings)
                    var course_id = window.location.href.split('amundi/')[1].split('/')[0];
                    $.ajax({
                        url: '/settings/amundi/'+ course_id,
                        type: 'POST',
                        dataType: 'json',
                        data: {
                            is_new: custom_settings.is_new,
                            invitation_only: custom_settings.invitation_only,
                            is_graded: !custom_settings.is_graded,
                            manager_only: custom_settings.manager_only,
                            is_mandatory: custom_settings.is_mandatory,
                            has_menu: custom_settings.has_menu,
                            tag: custom_settings.tag,
                            onboarding: custom_settings.onboarding,
                            course_about: custom_settings.course_about
                        },
                        success : function(data){
                            validationView.showSavedBar(title, message);
                        }
                    });
                }
            };

            // When clicking for saving changes
            $('#submit-settings').on('click', function(){
                $('#error-json').hide();
                updateSettings();
            });
         });
  }); // function
})();