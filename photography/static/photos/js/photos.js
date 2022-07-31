class Gallery {
  /**
   * @param {thingsList} list [button, content, class, imgClass, container, overlay]
   */
  constructor(thingsList) {
    this.button = thingsList[0];
    this.content = thingsList[1];
    this.className = thingsList[2];
    this.imgClass = thingsList[3];
    this.container = thingsList[4];
    this.overlay = thingsList[5];

    $(this.content).hide();
    $(this.button).on("click", this._toggle.bind(this));
    $(this.imgClass).on("click", this._imgPreview.bind(this));
  }
  _toggle() {
    let $this = this;
    $($this.className).each(function () {
      $(this).toggle();
      $($this.content).is(":visible")
        ? $($this.button).text("Hide photos")
        : $($this.button).text("Show more");
    });
  }

  _imgPreview() {
    let $this = this;
    $($this.imgClass).on("click", function () {
      $($this.container).is(":hidden")
        ? $($this.container).show()
        : $($this.container).hide();

      $($this.overlay)
        .attr("src", $(this).attr("src"))
        .show()
        .one("click", function () {
          $(this).hide();
          $($this.container).hide();
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

Gallery.apply(['#kebBtn', '#kebContent', '.keb', '.kebImg', '#overlayContainer', '#overlay'])


// $("#kebContent").hide();
// $("#otherContent").hide();

// $("#kebBtn").on("click", function () {
//   $(".keb").each(function () {
//     $(this).toggle();
//     if ($("#kebContent").is(":visible")) {
//       $("#kebBtn").text("Hide photos");
//     } else {
//       $("#kebBtn").text("Show more");
//     }
//   });
// });

// $(".kebImg").on("click", function () {
//   if ($("#overlayContainer").is(":hidden")) {
//     $("#overlayContainer").show();
//   }
//   $("#overlay")
//     .attr("src", $(this).attr("src"))
//     .show()
//     .one("click", function () {
//       $(this).hide();
//       $("#overlayContainer").hide();
//     });
// });
