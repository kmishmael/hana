$(function(){
    $('#cancel').click(function () { 
        $('.pop-out').toggleClass('pop-n');
        $('#btn').toggleClass('roll');
    });
    $('#btn').click(function(){
        $(this).toggleClass('roll');
        $('.pop-out').toggleClass('pop-n');
       // $(this).toggleClass('roll-r');
    });

});


