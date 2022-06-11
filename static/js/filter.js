jQuery(document).ready(function ($) {

  
    //ISOTOPE
    let btns = $("#map .button-group button");
  
    btns.click(function (e) {
      $("#map .button-group button").removeClass("active");
      e.target.classList.add("active");
  
      let selector = $(e.target).attr("data-filter");
      $("#map .grid").isotope({
        filter: selector,
      });
    });
  
    $(window).on("load", function () {
      $("#map .grid").isotope({
        filter: ".sexual",
      });
    });
  

  

  });

  