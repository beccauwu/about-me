$('#kebContent').hide();
$('#kebBtn').on('click', function(){
    $('.keb').each(function(){
        $(this).toggle()
        if ($("#kebContent").is(":visible")) {
          $("#kebBtn").text("Hide photos");
        } else {
          $("#kebBtn").text("Show more");
        }
    })
})

$('.kebImg').on('click', function(){
    if ($("#overlayContainer").is(":hidden")){
        $("#overlayContainer").show();
    }
    $("#overlay")
    .attr('src', $(this).attr('src'))
    .show()
    .one("click", function () {
        $(this).hide();
        $("#overlayContainer").hide();
    });
})
