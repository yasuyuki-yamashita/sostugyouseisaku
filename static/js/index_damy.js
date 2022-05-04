$(document).ready(function () {
    $(".accordion__btn").on("click", function(){
        $(this).toggleClass("accordion__btn--active");
        $(this).parent("dt").next().toggleClass("accordion__body--active");
    });
});
$(function(){
    $(document).on('change keyup keydown paste cut', 
      'textarea.auto-resize', function()
    {
      if ($(this).outerHeight() > this.scrollHeight){
        $(this).height(1)
      }
      while ($(this).outerHeight() < this.scrollHeight){
        $(this).height($(this).height() + 1)
      }
    });
  });