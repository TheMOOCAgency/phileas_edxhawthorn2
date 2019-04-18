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
        var validationView = new ValidatingView();

         $(document).ready(function() {
            const updateSettings = function(){
                var formData = $('#settings').serializeArray();
                var custom_settings = {};
                for (var i = 0; i < formData.length; i++) {
                    custom_settings[formData[i]['name']] = formData[i]['value']
                }
                console.log(custom_settings)
                var course_id = window.location.href.split('amundi/')[1].split('/')[0];
                $.ajax({
                    url: '/settings/amundi/'+ course_id,
                    type: 'POST',
                    dataType: 'json',
                    data: {
                        is_new: custom_settings.is_new,
                        invitation_only: custom_settings.invitation_only,
                        is_graded: !custom_settings.is_graded
                    },
                    success : function(data){
                        validationView.showSavedBar(title, message);
                    }
                });
            };

            $('#submit-settings').on('click', function(){
                updateSettings();
            });
         });
  });  // function
})();