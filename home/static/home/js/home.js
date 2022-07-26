const projectsPanel = document.getElementById('projectsPanel');
const itmsArray = [
  [
    document.getElementById("accountspy"),
    document.getElementById("accountspyPanel"),
  ],
  [
    document.getElementById("snake"), 
    document.getElementById("snakePanel"),
  ],
  [
    document.getElementById("business"),
    document.getElementById("portfolioPanel"),
  ],
];
$(itmsArray).each(function() {
    const carousel = this[0];
    const panel = this[1];
    $(carousel).on("click", () => {
      $([panel, projectsPanel]).each(function () {
        if (!$(this).hasClass("show")) $(this).addClass("show");
      });
      $("html, body").animate(
        { scrollTop: $(panel).offset().top },
        100,
        "swing"
      );
    });
})

