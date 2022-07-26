$("#toTop").on("click", () => {
  $("html, body").animate({ scrollTop: $("#top").offset().top }), 50, "swing";
});
