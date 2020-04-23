$(document).ready(function(){

    $(".parent-menu").click(function(){
      lis = this.querySelectorAll('.child-menu');  
      $(lis).slideToggle();
    });

});
