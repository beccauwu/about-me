class Gallery {
  /**
   * @param {thingsList} list [button, content, class, imgClass, container, overlay]
   */
  constructor(thingsList) {
    this.button = thingsList[0];
    this.content = thingsList[1];
    this.className = thingsList[2];

    $(this.content).hide();
    $(this.button).on("click", this._toggle.bind(this));
    $('.img').on("click", this._imgPreview.bind(this));
  }
  _toggle() {
    const $this = this;
    $($this.className).each(function () {
      $(this).toggle();
      $($this.content).is(":visible")
        ? $($this.button).text("Hide photos")
        : $($this.button).text("Show more");
    });
  }

  _imgPreview() {
    $('.img').on("click", function () {
      if ($('#overlayContainer').is(":hidden")){
        $("#overlayContainer").show();
      }
      $('#overlay')
        .attr("src", $(this).attr("src"))
        .show()
        .one("click", function () {
          $(this).hide();
          $("#overlayContainer").hide();
        });
    });
  }

  /**
   * @param {thingsList} list [button, content, class, imgClass, container, overlay]
   */
  static apply(thingsList) {
    new Gallery(thingsList);
  }
}

// apply to different panels
Gallery.apply([
  "#kebBtn",
  "#kebContent",
  ".keb",
]);
Gallery.apply([
  "#rgBtn",
  "#rgContent",
  ".rg",
]);
Gallery.apply([
  "#otherBtn",
  "#otherContent",
  ".oth",
]);
