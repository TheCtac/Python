$(document).ready(function(){

      $(".open-menu").click(function(){
          menuDiv = this.parentElement
          lis = menuDiv.querySelectorAll('.child-menu')
          $(lis).slideToggle();
          fas_ = menuDiv.querySelectorAll('fas')
          $(fas_).toggleClass('flip');
      });
});
