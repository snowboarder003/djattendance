$(document).ready(function() {
  $('[data-toggle=offcanvas]').click(function() {
    $('.row-offcanvas').toggleClass('active');
    $('.sidebar-toggle').toggleClass('active');
  });
  $('.content').click(function() {
	  if ($('.sidebar-toggle.active').length > 0){
	  	$('.row-offcanvas').toggleClass('active');
	  	$('.sidebar-toggle').toggleClass('active');
	  }
  });
});