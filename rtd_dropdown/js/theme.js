$( document ).ready(function() {
    // Shift nav in mobile when clicking the menu.
    $(document).on('click', "[data-toggle='wy-nav-top']", function() {
      $("[data-toggle='wy-nav-shift']").toggleClass("shift");
      $("[data-toggle='rst-versions']").toggleClass("shift");
    });

    // Close menu when you click a link.
    $(document).on('click', ".wy-menu-vertical .current ul li a", function() {
      $("[data-toggle='wy-nav-shift']").removeClass("shift");
      $("[data-toggle='rst-versions']").toggleClass("shift");
    });

    // Keyboard navigation
    document.addEventListener("keydown", function(e) {
      var key = e.which || e.keyCode || window.event && window.event.keyCode;
      var page;
      switch (key) {
          case 78:  // n
              page = $('[role="navigation"] a:contains(Next):first').prop('href');
              break;
          case 80:  // p
              page = $('[role="navigation"] a:contains(Previous):first').prop('href');
              break;
          case 13:  // enter
              if (e.target === document.getElementById('mkdocs-search-query')) {
                e.preventDefault();
              }
              break;
          default: break;
      }
      if ($(e.target).is(':input')) {
        return true;
      } else if (page) {
        window.location.href = page;
      }
    });

    $(document).on('click', "[data-toggle='rst-current-version']", function() {
      $("[data-toggle='rst-versions']").toggleClass("shift-up");
    });

    // Make tables responsive
    $("table.docutils:not(.field-list)").wrap("<div class='wy-table-responsive'></div>");

    $('table').addClass('docutils');

    /*
     * Custom rtd-dropdown
     */
    toggleCurrent = function (elem) {
        var parent_li = elem.closest('li');
        var menu_li = parent_li.next();
        var menu_ul = menu_li.children('ul');
        parent_li.siblings('li').not(menu_li).removeClass('current').removeClass('with-children');
        parent_li.siblings().find('> ul').not(menu_ul).removeClass('current').addClass('toc-hidden');
        parent_li.toggleClass('current').toggleClass('with-children');
        menu_li.toggleClass('current');
        menu_ul.toggleClass('current').toggleClass('toc-hidden');
    }

    // https://github.com/rtfd/sphinx_rtd_theme/blob/master/js/theme.js
    $('.tocbase').find('.toctree-expand').each(function () {
        var link = $(this).parent();
        $(this).on('click', function (ev) {
            console.log('click expand');
            toggleCurrent(link);
            ev.stopPropagation();
            return false;
        });
        link.on('click', function (ev) {
            console.log('click link');
            toggleCurrent(link);
        });
    });
});

window.SphinxRtdTheme = (function (jquery) {
    var stickyNav = (function () {
        var navBar,
            win,
            stickyNavCssClass = 'stickynav',
            applyStickNav = function () {
                if (navBar.height() <= win.height()) {
                    navBar.addClass(stickyNavCssClass);
                } else {
                    navBar.removeClass(stickyNavCssClass);
                }
            },
            enable = function () {
                applyStickNav();
                win.on('resize', applyStickNav);
            },
            init = function () {
                navBar = jquery('nav.wy-nav-side:first');
                win    = jquery(window);
            };
        jquery(init);
        return {
            enable : enable
        };
    }());
    return {
        StickyNav : stickyNav
    };
}($));

// The code below is a copy of @seanmadsen code posted Jan 10, 2017 on issue 803.
// https://github.com/mkdocs/mkdocs/issues/803
// This just incorporates the auto scroll into the theme itself without
// the need for additional custom.js file.
//
$(function() {
  $.fn.isFullyWithinViewport = function(){
      var viewport = {};
      viewport.top = $(window).scrollTop();
      viewport.bottom = viewport.top + $(window).height();
      var bounds = {};
      bounds.top = this.offset().top;
      bounds.bottom = bounds.top + this.outerHeight();
      return ( ! (
        (bounds.top <= viewport.top) ||
        (bounds.bottom >= viewport.bottom)
      ) );
  };
  if( $('li.toctree-l1.current').length && !$('li.toctree-l1.current').isFullyWithinViewport() ) {
    $('.wy-nav-side')
      .scrollTop(
        $('li.toctree-l1.current').offset().top -
        $('.wy-nav-side').offset().top -
        60
      );
  }
});