$('.nav-link').each.on('click', function(){
  localStorage.setItem('currentPage', $(this).html())
})

$('#resumeBackLink').on('click', function(){
  localStorage.getItem('currentPage')
})
