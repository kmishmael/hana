$(function(){
    $('#cancel').click(function () { 
        $('.pop-out').css("display", "none");
        $('#btn').toggleClass('roll');
    });
    $('#btn').click(function(){
        $(this).toggleClass('roll');
        $('.pop-out').toggleClass('pop-n');
       // $(this).toggleClass('roll-r');
    })
});


