/********************** ACTIONS **********************/
/* HIDE PREVIOUS & NEXT BUTTONS IF HAS_MENU = TRUE */
if (!hasMenu) {
  $("button.sequence-nav-button.button-previous").hide();
  $("button.sequence-nav-button.button-next").hide();
}

/* TOGGLE MENU */
$("span.open-courseware-nav").on("click", function() {
  $("#tma-completion-nav").removeClass("folded");
  $(".open-courseware-nav").addClass("tma-visibility-hidden");
});
$("button.close-courseware-nav").on("click", function() {
  $("#tma-completion-nav").addClass("folded");
  $(".open-courseware-nav").removeClass("tma-visibility-hidden");
});
$(
  ".xmodule_display.xmodule_SequenceModule .sequence-bottom .sequence-nav-button"
).on("click", function() {
  $("#tma-completion-nav").addClass("folded");
  $(".open-courseware-nav").removeClass("tma-visibility-hidden");
  close_all_subsections();
});

/* OPEN & CLOSE MENU */
$("#tma-completion-nav .close-courseware-nav").on("click", function() {
  close_all_subsections();
});
$(".open-courseware-nav").on("click", function() {
  highlight_current_unit();
});

/* GET COMPLETION ON PAGE LOAD */
$(document).ready(function() {
  // Open menu when landing on page if coming from course_about
  if (document.referrer.indexOf("/about") > -1 && hasMenu == "True") {
    $("#tma-completion-nav").removeClass("folded");
    $(".open-courseware-nav").addClass("tma-visibility-hidden");
  }

  mark_started_subsections();
  close_all_subsections();

  // Get course completion to feed progress bar
  get_course_completion();

  // Check user grade for popup bravo, for ungraded courses with no exercises
  get_user_grade();

  // Get completion per xblock
  currentUnit = $(
    ".xblock.xblock-student_view.xblock-student_view-vertical.xblock-initialized"
  ).data("usage-id");
  get_unit_completion(currentUnit, isLinear);

  if (isLinear) {
    isUnitAvailable(currentUnit);
  }
});

/* GET COMPLETION WHEN CLICKING ON NEXT OR WHEN ANSWERING A PROBLEM */
$(document).ajaxSuccess(function(e, xhr, settings) {
  if (
    settings.url.indexOf("goto_position") > -1 ||
    settings.url.indexOf("problem_check") > -1
  ) {
    response = JSON.parse(xhr.responseText);
    mark_started_subsections();

    // Get course completion to feed progress bar
    get_course_completion();

    // Check user grade for popup bravo, for ungraded courses with no exercises
    get_user_grade();

    // Get completion per xblock
    currentUnit = $(
      ".xblock.xblock-student_view.xblock-student_view-vertical.xblock-initialized"
    ).data("usage-id");
    get_unit_completion(currentUnit, isLinear);

    if (isLinear) {
      isUnitAvailable(currentUnit);
    }
  }
});

/* GET COMPLETION WHEN XBLOCK IS CONSIDERED AS VIEWED */
$(document).ajaxSuccess(function(e, xhr, settings) {
  if (settings.url.indexOf("publish_completion") > -1) {
    currentUnit = $(
      ".xblock.xblock-student_view.xblock-student_view-vertical.xblock-initialized"
    ).data("usage-id");
    get_unit_completion(currentUnit, isLinear);

    if (isLinear) {
      isUnitAvailable(currentUnit);
    }
  }
});

/********************** FUNCTIONS **********************/
function mark_started_subsections() {
  $(".subsection.accordion").each(function() {
    subsection_started = false;
    $(this)
      .find(".accordion-panel .vertical-title")
      .each(function() {
        if ($(this).hasClass("tma_completed")) {
          subsection_started = true;
        }
      });
    if (
      subsection_started &&
      !$(this)
        .find(".subsection-title")
        .hasClass("tma_completed")
    ) {
      $(this)
        .find(".subsection-title")
        .addClass("tma_started");
    }
  });
}

function mark_unit_completed(unit_id) {
  $("#" + unit_id.replace(/([$%&()*+,./:;<=>?@\[\\\]^\{|}~])/g, "\\$1"))
    .find(".vertical-title")
    .addClass("tma_completed");
}

// Get course completion to provide data for top-right progress bar
function get_course_completion() {
  url = "/tma_apps/" + global_courseid + "/completion/get_course_completion";
  $.ajax({
    type: "get",
    url: url,
    success: function(response) {
      completion_rate = Math.round(response.completion_rate * 100);
      $("#tma-completion-value").html(completion_rate + "%");
      if (completion_rate != 0) {
        $("#tma-completion-progress")
          .css("width", completion_rate + "%")
          .addClass("primary-color-bg");
      }
    }
  });
}

// Get unit completion to provide data for left menu and Next button
function get_unit_completion(currentUnit, isLinear) {
  url =
    "/tma_apps/" +
    global_courseid +
    "/" +
    currentUnit +
    "/completion/get_unit_completion";
  $.ajax({
    type: "get",
    url: url,
    success: function(response) {
      allBlocksCompleted = true;
      response.unit_blocks.children.forEach(function(block) {
        if (!block.complete) {
          allBlocksCompleted = false;
        }
      });
      if (allBlocksCompleted) {
        mark_unit_completed(currentUnit);
        if (isLinear) {
          isUnitAvailable(currentUnit);
        }
      }
    }
  });
}

function close_all_subsections() {
  $("#tma-completion-nav .subsection .outline-item.accordion-panel").each(
    function() {
      $(this).addClass("is-hidden");
    }
  );
  $("#tma-completion-nav .fa-chevron-right").each(function() {
    $(this).removeClass("fa-rotate-90");
  });
  $(".tma-current-unit").each(function() {
    $(this).removeClass("tma-current-unit");
  });
}

function highlight_current_unit() {
  unit_id = $(
    ".xblock.xblock-student_view.xblock-student_view-vertical.xblock-initialized"
  ).data("usage-id");
  $(
    "#" + unit_id.replace(/([$%&()*+,./:;<=>?@\[\\\]^\{|}~])/g, "\\$1")
  ).addClass("tma-current-unit");
  $("#" + unit_id.replace(/([$%&()*+,./:;<=>?@\[\\\]^\{|}~])/g, "\\$1"))
    .parents(".accordion-panel")
    .removeClass("is-hidden");
  $("#" + unit_id.replace(/([$%&()*+,./:;<=>?@\[\\\]^\{|}~])/g, "\\$1"))
    .parents("li.accordion")
    .find(".fa-chevron-right ")
    .addClass("fa-rotate-90");
}

// Check if current unit is completed, thus if next unit should be available
function isUnitAvailable(currentUnit) {
  $("ol.outline-item.accordion-panel li a.outline-item.focusable").each(
    function(i, element) {
      // Not for first unit
      if (i !== 0) {
        isUnitSeen =
          $(this)
            .children()
            .children()
            .hasClass("tma_completed") ||
          $(this)
            .children()
            .children()
            .hasClass("tma_started");
        isPreviousSeen =
          $("ol.outline-item.accordion-panel li a.outline-item.focusable")
            .eq(i - 1)
            .children()
            .children()
            .hasClass("tma_completed") ||
          $("ol.outline-item.accordion-panel li a.outline-item.focusable")
            .eq(i - 1)
            .children()
            .children()
            .hasClass("tma_started");

        // If current unit and previous unit have not been started nor completed, link is disabled
        if (!isUnitSeen && !isPreviousSeen) {
          $(this).addClass("disabled-link");
        } else {
          $(this).removeClass("disabled-link");
        }
      }
    }
  );

  // If current unit is not completed yet, disable button next + add tooltip
  let button = $(".sequence-bottom .sequence-nav-button.button-next");
  if (
    !$('a.outline-item.focusable[id="' + currentUnit + '"]')
      .children()
      .children()
      .hasClass("tma_completed")
  ) {
    // HAD TO ATTRIBUTE IT TO PARENT AS IT DOESNT WORK ON DISABLED BUTTON
    button.prop("disabled", true);
    button.parent().qtip({
      content: {
        text:
          "You cannot access the next unit because the current unit is not completed. Please ensure that you viewed all contents and answered all questions."
      },
      position: {
        my: "top right",
        at: "bottom right"
      },
      events: {
        render: function(event, api) {
          var elem = api.elements.tip;
        }
      }
    });
  } else {
    button.prop("disabled", false);
    button.parent().qtip("destroy", true);
  }
}
