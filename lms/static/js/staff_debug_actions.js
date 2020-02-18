// Build StaffDebug object
var StaffDebug = (function() {
  /* global getCurrentUrl:true */
  var getURL = function(action) {
    var pathname = this.getCurrentUrl();
    return (
      pathname.substr(0, pathname.indexOf("/courseware")) +
      "/instructor/api/" +
      action
    );
  };

  var sanitizeString = function(string) {
    return string.replace(/[.*+?^:${}()|[\]\\]/g, "\\$&");
  };

  var getUser = function(locationName) {
    var sanitizedLocationName = sanitizeString(locationName);
    var uname = $("#sd_fu_" + sanitizedLocationName).val();
    if (!uname) {
      uname = $("#sd_fu_" + sanitizedLocationName).attr("placeholder");
      if (!uname) {
        // ADDED FOR STUDENT DELETE STATE MODULE
        uname = JSON.parse($("#user-metadata").html())["username"];
      }
    }
    return uname;
  };

  var getScore = function(locationName) {
    var sanitizedLocationName = sanitizeString(locationName);
    var score = $("#sd_fs_" + sanitizedLocationName).val();
    if (score === "") {
      score = $("#sd_fs_" + sanitizedLocationName).attr("placeholder");
    }
    return score;
  };
  var count = 0;
  var doInstructorDashAction = function(action) {
    var pdata = {
      problem_to_reset: action.location,
      unique_student_identifier: getUser(action.locationName),
      delete_module: action.delete_module,
      only_if_higher: action.only_if_higher,
      score: action.score
    };
    $.ajax({
      type: "POST",
      url: getURL(action.method),
      data: pdata,
      success: function(data) {
        var text = _.template(action.success_msg, {
          interpolate: /\{(.+?)\}/g
        })({ user: data.student });
        var html = _.template('<p id="idash_msg" class="success">{text}</p>', {
          interpolate: /\{(.+?)\}/g
        })({ text: text });
        $("#result_" + sanitizeString(action.locationName)).html(html);
        count++;
        console.log(count);
        // reload after student clears attempts
        if (count === action.length) {
          // count = 0;
          return window.location.reload();
        }
      },
      error: function(request, status, error) {
        var responseJSON;
        try {
          responseJSON = $.parseJSON(request.responseText);
        } catch (e) {
          responseJSON = "Unknown Error Occurred.";
        }
        var text = _.template("{error_msg} {error}", {
          interpolate: /\{(.+?)\}/g
        })({
          error_msg: action.error_msg,
          error: gettext(responseJSON)
        });
        var html = _.template('<p id="idash_msg" class="error">{text}</p>', {
          interpolate: /\{(.+?)\}/g
        })({ text: text });
        $("#result_" + sanitizeString(action.locationName)).html(html);
      },
      dataType: "json"
    });
  };

  var reset = function(locname, location) {
    this.doInstructorDashAction({
      locationName: locname,
      location: location,
      method: "reset_student_attempts",
      success_msg: gettext("Successfully reset the attempts for user {user}"),
      error_msg: gettext("Failed to reset attempts for user."),
      delete_module: false
    });
  };

  var deleteStudentState = function(locname, location, length) {
    this.doInstructorDashAction({
      locationName: locname,
      location: location,
      length: length,
      method: "reset_student_attempts",
      success_msg: gettext(
        "Successfully deleted student state for user {user}"
      ),
      error_msg: gettext("Failed to delete student state for user."),
      delete_module: true
    });
  };

  var rescore = function(locname, location) {
    this.doInstructorDashAction({
      locationName: locname,
      location: location,
      method: "rescore_problem",
      success_msg: gettext("Successfully rescored problem for user {user}"),
      error_msg: gettext("Failed to rescore problem for user."),
      only_if_higher: false
    });
  };

  var rescoreIfHigher = function(locname, location) {
    this.doInstructorDashAction({
      locationName: locname,
      location: location,
      method: "rescore_problem",
      success_msg: gettext(
        "Successfully rescored problem to improve score for user {user}"
      ),
      error_msg: gettext(
        "Failed to rescore problem to improve score for user."
      ),
      only_if_higher: true
    });
  };

  var overrideScore = function(locname, location) {
    this.doInstructorDashAction({
      locationName: locname,
      location: location,
      method: "override_problem_score",
      success_msg: gettext("Successfully overrode problem score for {user}"),
      error_msg: gettext("Could not override problem score for {user}."),
      score: getScore(locname)
    });
  };

  getCurrentUrl = function() {
    return window.location.pathname;
  };

  return {
    reset: reset,
    deleteStudentState: deleteStudentState,
    rescore: rescore,
    rescoreIfHigher: rescoreIfHigher,
    overrideScore: overrideScore,

    // export for testing
    doInstructorDashAction: doInstructorDashAction,
    getCurrentUrl: getCurrentUrl,
    getURL: getURL,
    getUser: getUser,
    getScore: getScore,
    sanitizeString: sanitizeString
  };
})();

// Register click handlers
$(document).ready(function() {
  var $courseContent = $(".course-content");
  $courseContent.on("click", ".staff-debug-reset", function() {
    StaffDebug.reset(
      $(this)
        .parent()
        .data("location-name"),
      $(this)
        .parent()
        .data("location")
    );
    return false;
  });
  $courseContent.on("click", ".staff-debug-sdelete", function() {
    StaffDebug.deleteStudentState(
      $(this)
        .parent()
        .data("location-name"),
      $(this)
        .parent()
        .data("location")
    );
    return false;
  });
  // IN ORDER TO DELETE ALL XBLOCKS STATE IN A SINGLE PAGE, BY STUDENT HIMSELF
  $courseContent.on("click", ".staff-debug-all-sdelete", function() {
    let getXblocks = $(".xblock-student_view-library_content");
    if (getXblocks.length === 0) {
      getXblocks = $(".xblock-student_view-problem");
    }
    let xBlocks = [];
    for (let i = 0; i < getXblocks.length; i++) {
      if (xBlocks.indexOf($(getXblocks[i]).data("usage-id")) === -1) {
        console.log($(getXblocks[i]).data("usage-id"));
        xBlocks.push($(getXblocks[i]).data("usage-id"));
      }
    }

    let location = "";
    let locName = "";
    let index = 0;
    for (i = 0; i < xBlocks.length; i++) {
      console.log(xBlocks.length);
      location = xBlocks[i];
      index = location.lastIndexOf("@") + 1;
      locName = location.slice(index);

      StaffDebug.deleteStudentState(locName, location, xBlocks.length);
    }
    return false;
  });
  $courseContent.on("click", ".staff-debug-rescore", function() {
    StaffDebug.rescore(
      $(this)
        .parent()
        .data("location-name"),
      $(this)
        .parent()
        .data("location")
    );
    return false;
  });
  $courseContent.on("click", ".staff-debug-rescore-if-higher", function() {
    StaffDebug.rescoreIfHigher(
      $(this)
        .parent()
        .data("location-name"),
      $(this)
        .parent()
        .data("location")
    );
    return false;
  });

  $courseContent.on("click", ".staff-debug-override-score", function() {
    StaffDebug.overrideScore(
      $(this)
        .parent()
        .data("location-name"),
      $(this)
        .parent()
        .data("location")
    );
    return false;
  });
});
