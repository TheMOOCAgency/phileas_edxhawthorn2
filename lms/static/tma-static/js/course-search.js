'Use strict'
const searchByFilter = function(coursesJson, query, filter) {
    var results = [];
    // if language
    if ((query == 'French' ) || (query == 'Français')) {
        query = 'fr';
    } else {
        if ((query == 'English') || (query == 'Anglais')) {
            query = 'en';
        }
    }
    var regexQuery = new RegExp(query, 'i');
    coursesJson.forEach(function(course){
        if (course[filter] && course[filter].search(regexQuery) > -1) {
            results.push(course);
        }
    });
    return results;
};

const searchByInput = function(coursesJson, query) {
    var results = [];
    var regexQuery = new RegExp(query, 'i');
    coursesJson.forEach(function(course){
        if (course.display_name && (course.display_name.search(regexQuery) > -1)) {
            results.push(course);
        } else {
            if (course.short_description && (course.short_description.search(regexQuery) > -1)) {
                results.push(course);
            }
        }
    });
    return results;
};

const searchByBool = function(coursesJson, query) {
    var results = [];
    switch(query) {
        case 'Vodeclic':
            coursesJson.forEach(function(course) {
                if (course.is_vodeclic) {
                    results.push(course);
                }
            });
            break;
        case 'Amundi':
            coursesJson.forEach(function(course) {
                if (!course.is_vodeclic) {
                    results.push(course);
                }
            });
            break;
        case 'New':
            coursesJson.forEach(function(course) {
                if (course.is_new) {
                    results.push(course);
                }
            });
            break;
    }
    return results;
};

const displayResults = function(results) {
    $('#cards-box').html('');
    results.forEach(function(item){
        var isMandatory = item.is_mandatory;
        var isManagerOnly = item.is_manager_only;
        var isVodeclic = item.is_vodeclic;
        var isFavorite = item.is_favorite;
        var isLiked = item.is_liked;
        var language = item.language;
        var isEnrolled = item.is_enrolled;
        var isBlocked = item.is_blocked;
        var courseId = item.id.split('+').join('').split(':').join('');
        var subjectTag = item.tag;

        var buttonText = function(){
            var buttonText;
            if (isManagerOnly || isBlocked) {
                buttonText = '<a class="enroll-btn no-enroll">'+item.button_text+'</a>';
            } else {
                if (isVodeclic) {
                    if (isEnrolled) {
                        buttonText = 'a href="'+item.vodeclic_link+'" target="_blank" class="enroll-btn">'+item.button_text+'</a>';
                    } else {
                        buttonText = '<a href="'+item.vodeclic_link+'" target="_blank" class="enroll-btn vodeclick_register" data-vodeclic-id="'+item.id+'">'+item.button_text+'</a>';
                    };
                } else {
                    if (isEnrolled) {
                        buttonText = '<a href="/courses/'+item.id+'/courseware/" class="enroll-btn">'+item.button_text+'</a>';
                    } else {
                        buttonText = '<a href="/courses/'+item.id+'/about" class="enroll-btn">'+item.button_text+'</a>';
                    };
                };
            };
            return buttonText;
        };

        var mandatoryTag = function() {
            var tag;
            if (isMandatory) {
                tag = '<div class="col mandatory-tag"><p class="text-center">Mandatory Course!</p></div>';
            } else {
                tag = '<div style="display:none"></div>';
            }
            return tag;
        };

        var tag = function() {
            var tag;
            if (subjectTag.indexOf(',') > -1) {
                tag = subjectTag.split(',', 1);
            } else {
                tag = subjectTag;
            }
            return tag;
        }
  
        $('#cards-box').append('<div class="col-lg-4 col-md-6 flip-container"><div class="flipper"><div class="course-card-sm front mb-3">'
        // ---------------  FRONT CARD ---------------
        // Is mandatory
        + mandatoryTag() + 
        '<div class="cover-image"><img src="'+item.course_image_url+'" alt="'+item.display_name_with_default+'"/></div><div class="container-fluid"><div class="container-fluid"><div class="row"><div class="course-name col"><div data-course-id="'+item.id+'" class="row pin-row '+courseId+'"><div><div class="category-tag">'+ tag() +'</div></div>' +
        // Manager Only or Blocked
        ((isManagerOnly || isBlocked) ? '<img src="/static/tma-static/images/cadenas.svg" data-toggle="tooltip" data-delay=\'{"show":"100", "hide":"100"}\' data-placement="top" title="Manager Only" class="pin">' : '') +
        // Is favorite
        (isFavorite ? '<span class="pin favorite favorite-on"></span>' : '<span class="pin favorite favorite-off"></span>') + '</div><div class="row course-title"><p>'+item.display_name+'</p></div><div class="pictos-box"><div data-course-id="'+item.id+'" class="row course-pictos '+courseId+'"><div data-course-id="'+item.id+'" class="col-4 text-center pl-2 pr-2 '+courseId+'">'+
        // Is liked
        (isLiked ? '<span class="pin like like-on"></span>' : '<span class="pin like like-off"></span>') +
        '<span class="like_count count-box" data-min="0" data-max="'+item.liked_total+'" data-delay="1" data-increment="'+(item.liked_total/3)+'">'+item.liked_total+'</span></div><div class="col-4 text-center pl-2 pr-2"><img src="/static/tma-static/images/Time.png"><span>'+item.effort+'<span></div><div class="col-4 text-center pl-2 pr-2">'+
        // Language
        ((language == "fr") ? '<img src="/static/tma-static/images/lang_fr.svg">' : '<img src="/static/tma-static/images/lang_en.svg">') +
        '<span class="text-uppercase">'+language+'</span></div></div></div><div class="row"><div class="col text-center"><a href="#"><img src="/static/tma-static/images/flechebas.png"></a></div></div></div></div></div></div></div>' +
  
        // ---------------  BACK CARD ---------------
        '<div class="course-card-sm back">' +
        // Is mandatory
        mandatoryTag() + 
        '<div class="cover-image"><img src="'+item.course_image_url+'" alt="'+item.display_name_with_default+'"/></div><div class="container-fluid"><div class="container-fluid"><div class="row"><div data-course-id="'+item.id+'" class="row pin-row '+courseId+'"><div class="category-tag">'+ tag() +'</div>'+
        // Manager Only or Blocked
        ((isManagerOnly || isBlocked) ? '<img src="/static/tma-static/images/cadenas.svg" data-toggle="tooltip" data-delay=\'{"show":"100", "hide":"100"}\' data-placement="top" title="Manager Only" class="pin">' : '') +
        // Is favorite
        (isFavorite ? '<span class="pin favorite favorite-on"></span>' : '<span class="pin favorite favorite-off"></span>') +
        // Is liked
        (isLiked ? '<span class="pin like like-on"></span>' : '<span class="pin like like-off"></span>') + '</div></div>' +
        '<div class="row course-title"><h3>'+item.display_name+'</h3></div></div><div class="row">'+
        (item.short_description ? '<p style="padding:15px;">'+item.short_description.substring(0,124)+'</p>' : '<p></p>') + '</div><div class="row"><div class="text-center course-btn">' +
        // Button
        buttonText() + 
        '</div></div></div></div></div></div></div>');
    });
};

function noResults() {
    $('#cards-box').html('<div class="row no-results text-center w-100 mt-5"><div class="col"><h3></h3><h3></h3><a class="discover-btn" href="/courses"></a></div></div>');
};