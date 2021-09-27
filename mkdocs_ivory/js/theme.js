function ready() {
  $('.nav .section').each(function() {
    $(this).click(function(e) {
      $(this).toggleClass("hide");
      $(this).parent().children(".subnav").toggleClass("hide");
    });
  });

  $('.hamburger').click(function(e) {
    $('html').toggleClass("show");
    $('aside').toggleClass("show");
    $('.home-top .site-name').toggleClass("hide");
  });

  $('.arrow').click(function(e) {
    $('aside').toggleClass("hide");
    $(this).toggleClass("hide");
  });
}

$(ready);
