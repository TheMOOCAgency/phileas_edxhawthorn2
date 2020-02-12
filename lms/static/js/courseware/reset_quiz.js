const get_all_questions = () => {
  let xBlocks = document.getElementsByClassName("vert");
  let problem_xblock_list = [];

  xBlocks.forEach(xBlock => {
    problem_xblock_list.push(xBlock.dataset.id);
  });
  return problem_xblock_list;
};

const reset_all_problems = () => {
  let count = 0;
  problem_xblock_list = get_all_questions();
  // course_id is passed through courseware.html script
  problem_xblock_list.forEach(xblock_id => {
    $.ajax({
      url:
        "/courses/" +
        course_id +
        "/xblock/" +
        xblock_id +
        "/handler/xmodule_handler/problem_reset",
      type: "POST",
      dataType: "json",
      data: {
        id: xblock_id,
        isResettable: true
      },
      success: () => {
        count += 1;
        if (count >= problem_xblock_list.length) {
          window.location.reload(true);
        }
      }
    });
  });
};
