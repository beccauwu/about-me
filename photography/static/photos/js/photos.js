class Gallery {
  /**
   * @param {thingsList} list [button, content, class]
   */
  constructor([buttonID, contentID, previewID]) {
    this.button = buttonID;
    this.content = contentID;
    this.preview = previewID;
    this.overlay = '#overlay';
    this.overlayContainer = '#overlayContainer';
    this.contentdown = false;
    $(this.overlayContainer).hide()
    $(this.overlay).hide();
    $(this.button).on("click", this._toggle.bind(this));
    $(".img").on("click", this._imgPreview.bind(this));
  }
  _toggle() {
    $(this.preview).toggle("fast");
    $(this.content).slideToggle("fast");
    if (!this.contentdown) {
      $(this.button).text("Hide photos");
      this.contentdown = true;
    } else {
      $(this.overlay).trigger("click");
      $(this.button).text("Show more");
      this.contentdown = false;
    }
  }
  _imgPreview() {
    const $this = this;
    $(".img").on("click", function () {
      if ($($this.overlayContainer).is(":hidden")) {
        $($this.overlayContainer).show();
      }
      $($this.overlay)
        .attr("src", $(this).attr("src"))
        .show()
        .one("click", function () {
          $(this).hide();
          $($this.overlayContainer).hide();
        });
    });
  }
  /**
   * @param {thingsList} list [buttonID, contentID, previewID]
   */
  static apply([buttonID, contentID, previewID]) {
    new Gallery([buttonID, contentID, previewID]);
  }
}

// apply to different panels
Gallery.apply([
  "#kebBtn",
  "#kebContent",
  "#kebPreview",
]);
Gallery.apply([
  "#rgBtn",
  "#rgContent",
  "#rgPreview",
]);
Gallery.apply([
  "#otherBtn",
  "#otherContent",
  "#otherPreview",
]);
