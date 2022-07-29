$(window).scroll(function() {
    var x = $(this).scrollTop();
    $('#introducao').css('left', parseInt(x) );
    if(x < 1400){
      $('#introducao').css('background', 'transparent' );
    }else if(x>3100){
      $('#introducao').css('background', 'rgba(20, 19, 19, 0.973)' );
      $('#introducao').css('transition', '2s' );
    }else{
      $('#introducao').css('background', 'transparent' );
    }

        var p = document.querySelector('#introducao');
    posicoes = p.getBoundingClientRect();
    console.log(posicoes);
});