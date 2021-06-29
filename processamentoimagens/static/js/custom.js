var path = "/static/img/resultado/"

$('#rgbtobit').click(function(){
    var image1 = $('#inputImage1')[0].files[0].name;
    var value = parseInt($("#value").val());
    if(isNaN(value)){
        value = 0
    }
    sendImageValue("rgbtobit", image1, value);
});

$('#rgbtogray').click(function(){
    var image1 = $('#inputImage1')[0].files[0].name
    sendOneImage("rgbtogray", image1);
});

$('#negativo').click(function(){
    var image1 = $('#inputImage1')[0].files[0].name
    sendOneImage("negativo", image1);
});

$('#histograma').click(function(){
    var image1 = $('#inputImage1')[0].files[0].name
    sendOneImage("histograma", image1);
});

$('#adicao').click(function(){
    var image1 = $('#inputImage1')[0].files[0].name
    var image2 = $('#inputImage2')[0].files[0].name
    sendTwoImages("adicao", image1, image2);
});

$('#subtracao').click(function(){
    var image1 = $('#inputImage1')[0].files[0].name
    var image2 = $('#inputImage2')[0].files[0].name
    sendTwoImages("subtracao", image1, image2);
});

$('#multiplicacao').click(function(){
    var image1 = $('#inputImage1')[0].files[0].name;
    var value = parseInt($("#value").val());
    if(isNaN(value)){
        value = 0
    }
    sendImageValue("multiplicacao", image1, value);
});

$('#divisao').click(function(){
    var image1 = $('#inputImage1')[0].files[0].name;
    var value = parseInt($("#value").val());
    if(isNaN(value)){
        value = 0
    }
    sendImageValue("divisao", image1, value);
});

$('#and').click(function(){
    var image1 = $('#inputImage1')[0].files[0].name
    var image2 = $('#inputImage2')[0].files[0].name
    sendTwoImages("fand", image1, image2);
});

$('#or').click(function(){
    var image1 = $('#inputImage1')[0].files[0].name
    var image2 = $('#inputImage2')[0].files[0].name
    sendTwoImages("for", image1, image2);
});

$('#xor').click(function(){
    var image1 = $('#inputImage1')[0].files[0].name
    var image2 = $('#inputImage2')[0].files[0].name
    sendTwoImages("fxor", image1, image2);
});

$('#not').click(function(){
    var image1 = $('#inputImage1')[0].files[0].name
    sendOneImage("fnot", image1);
});

$('#blending').click(function(){
    var image1 = $('#inputImage1')[0].files[0].name
    var image2 = $('#inputImage2')[0].files[0].name
    sendTwoImages("blending", image1, image2);
});

function sendOneImage(url, image1){
    var data = {
        image1 : image1
    };
    $.ajax({
        url: 'http://localhost:8000/' + url,
        method: "GET",
        data: data
    }).then(function(data){
        document.getElementById('imageResult').src = path + data['resultado'];
    });
}

function sendTwoImages(url, image1, image2){
    var data = {
        image1 : image1,
        image2 : image2
    };
    $.ajax({
        url: 'http://localhost:8000/' + url,
        method: "GET",
        data: data
    }).then(function(data){
        document.getElementById('imageResult').src = path + data['resultado'];
    });
}

function sendImageValue(url, image1, value){
    var data = {
        image1 : image1,
        value : value
    };
    $.ajax({
        url: 'http://localhost:8000/' + url,
        method: "GET",
        data: data
    }).then(function(data){
        document.getElementById('imageResult').src = path + data['resultado'];
    });
}