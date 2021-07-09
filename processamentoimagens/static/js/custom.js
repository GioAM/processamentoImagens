var path = "/static/img/resultado/"
var toastElList = [].slice.call(document.querySelectorAll('#information'));
var toastList = toastElList.map(function(toastEl) {
	return new bootstrap.Toast(toastEl, {delay: 25000});
});
var functionInformation = new Map();

$(document).ready(function() {
    functionInformation.set('rgbtogray',['RGB to Gray','<p>Transforma uma imagem da escala de RGB para a escala de cinza</p><p><strong>Dados: </strong>Imagem 1</p>']);
    functionInformation.set('rgbtobit',['RGB to Bit','<p>Transforma uma imagem da escala de RGB para a escala de bit a partir de um valor limiar estipulado</p><p><strong>Dados: </strong>Imagem 1, valor</p><p><strong>Valor Default: </strong> 127</p>']);
    functionInformation.set('negativo',['Negativo','<p>Os valores da imagem são invertidos para gerar uma imagem negativa</p><p><strong>Dados: </strong>Imagem 1</p>']);
    functionInformation.set('histograma',['Equalização de Histograma','<p>Visa o aumento da uniformidade da distribuição de níveis de cinza de uma imagem</p><p><strong>Dados: </strong>Imagem 1</p>']);
    functionInformation.set('adicao',['Adição','<p>Realiza a adição de duas imagens</p><p><strong>Dados: </strong>Imagem 1, Imagem 2</p>']);
    functionInformation.set('subtracao',['Subtração','<p>Realiza a subtração de duas imagens</p><p><strong>Dados: </strong>Imagem 1, Imagem 2</p>']);
    functionInformation.set('multiplicacao',['Multiplicacão','<p>Pode ser usada como meio simples de ajuste de contraste e como extensão à adição/subtração. </br> Aumento de contraste em 50% = multiplicação por 1.5</p><p><strong>Dados: </strong>Imagem 1, Valor</p><p><strong>Valor Default: </strong>1.5</p>']);
    functionInformation.set('divisao',['Divisão','<p>Pode ser usada como meio simples de ajuste de contraste e como extensão à adição/subtração. </br> Redução de contraste em 25% = divisão por 4</p><p><strong>Dados: </strong>Imagem 1, Valor</p><p><strong>Valor Default: </strong>4</p>']);
    functionInformation.set('blending',['Blending','<p>Produz a mistura de duas imagens do mesmo tamanho, pela combinação da multiplicação de um escalar e adição de imagens. Valor escalar da imagem 1, vai ser o valor digitado e o valor 2 vai ser 1 - valor 1</p><p><strong>Dados: </strong>Imagem 1, Imagem 2, valor</p><p><strong>Valor Default: </strong>0.8</p>']);
    functionInformation.set('and',['AND','<p>Realiza a operação lógica AND entre duas imagens de escala binária</p><p><strong>Dados: </strong>Imagem 1, Imagem 2</p>']);
    functionInformation.set('or',['OR','<p>Realiza a operação lógica OR entre duas imagens de escala binária</p><p><strong>Dados: </strong>Imagem 1, Imagem 2</p>']);
    functionInformation.set('xor',['XOR','<p>Realiza a operação lógica XOR entre duas imagens de escala binária</p><p><strong>Dados: </strong>Imagem 1, Imagem 2</p>']);
    functionInformation.set('not',['NOT','<p>Realiza a operação lógica NOT em uma imagem de escala binária</p><p><strong>Dados: </strong>Imagem 1</p>']);
    functionInformation.set('media',['Média','<p>É um filtro linear para suavização de imagens. Ele substitui cada pixel da imagem pelo valor média de sua vizinhança. O valor digitado será usado como a matriz quadrada (valor X valor) para o filtro.</p><p><strong>Dados: </strong>Imagem 1, valor</p><p><strong>Valor default: </strong>5</p>']);
    functionInformation.set('mediana',['Mediana','<p> É um filtro não linear e apresenta bons resultados em ruídos sal e pimenta. É mais eficaz na preservação de detalhes de alta frequência. O valor digitado indica a intensidade.</p><p><strong>Dados: </strong>Imagem 1, valor</p><p><strong>Valor default: </strong>5</p>']);
    functionInformation.set('gaussiana',['Gaussiana','<p>É um filtro linear, passa-baixas. Apresenta bons resultados no tratamento de imagens com ruído gaussiano. O valor digitado será usado como a matriz quadrada (valor X valor) para o filtro.</p><p><strong>Dados: </strong>Imagem 1, valor</p><p><strong>Valor default: </strong>5</p>']);
    functionInformation.set('dilatacao',['Dilatação','<p>É caracterizada pela dilatação da área do objeto de interesse. O valor digitado será usado como a matriz quadrada (valor X valor) para o processo.</p><p><strong>Dados: </strong>Imagem 1, valor</p><p><strong>Valor default: </strong>5</p>']);
    functionInformation.set('erosao',['Erosão','<p>É caracterizada pela corrosão das arestas, resultando em um objeto menor. O valor digitado será usado como a matriz quadrada (valor X valor) para o processo.</p><p><strong>Dados: </strong>Imagem 1, valor</p><p><strong>Valor default: </strong>5</p>']);
    functionInformation.set('abertura',['Abertura','<p>É caracterizada pela operação de erosão seguida da operação de dilatação. O valor digitado será usado como a matriz quadrada (valor X valor) para o processo.</p><p><strong>Dados: </strong>Imagem 1, valor</p><p><strong>Valor default: </strong>3</p>']);
    functionInformation.set('fechamento',['Fechamento','<p>Usado para preencher os pontos nos objetos de interesse. É caracterizada pela operação de dilatação seguida da operação de erosão. O valor digitado será usado como a matriz quadrada (valor X valor) para o processo.</p><p><strong>Dados: </strong>Imagem 1, valor</p><p><strong>Valor default: </strong>5</p>']);
    functionInformation.set('contorno',['Contorno','<p>Representa a borda do objeto de interesse. O valor digitado será usado como a matriz quadrada (valor X valor) para o processo.</p><p><strong>Dados: </strong>Imagem 1, valor</p><p><strong>Valor default: </strong>3</p>']);
});

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
    var value = parseFloat($("#value").val());
    if(isNaN(value)){
        value = 0
    }
    sendImageValue("multiplicacao", image1, value);
});

$('#divisao').click(function(){
    var image1 = $('#inputImage1')[0].files[0].name;
    var value = parseFloat($("#value").val());
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
    var value = parseFloat($("#value").val());
    console.log(value);
    if(isNaN(value)){
        value = 0
    }
    sendTwoImagesValue("blending", image1, image2, value);
});

$('#media').click(function(){
    var image1 = $('#inputImage1')[0].files[0].name;
    var value = parseInt($("#value").val());
    if(isNaN(value)){
        value = 0
    }
    sendImageValue("media", image1, value);
});

$('#mediana').click(function(){
    var image1 = $('#inputImage1')[0].files[0].name;
    var value = parseInt($("#value").val());
    if(isNaN(value)){
        value = 0
    }
    sendImageValue("mediana", image1, value);
});

$('#gaussiana').click(function(){
    var image1 = $('#inputImage1')[0].files[0].name;
    var value = parseInt($("#value").val());
    if(isNaN(value)){
        value = 0
    }
    sendImageValue("gaussiana", image1, value);
});

$('#dilatacao').click(function(){
    var image1 = $('#inputImage1')[0].files[0].name;
    var value = parseInt($("#value").val());
    if(isNaN(value)){
        value = 0
    }
    sendImageValue("dilatacao", image1, value);
});

$('#abertura').click(function(){
    var image1 = $('#inputImage1')[0].files[0].name;
    var value = parseInt($("#value").val());
    if(isNaN(value)){
        value = 0
    }
    sendImageValue("abertura", image1, value);
});

$('#fechamento').click(function(){
    var image1 = $('#inputImage1')[0].files[0].name;
    var value = parseInt($("#value").val());
    if(isNaN(value)){
        value = 0
    }
    sendImageValue("fechamento", image1, value);
});

$('#erosao').click(function(){
    var image1 = $('#inputImage1')[0].files[0].name;
    var value = parseInt($("#value").val());
    if(isNaN(value)){
        value = 0
    }
    sendImageValue("erosao", image1, value);
});

$('#contorno').click(function(){
    var image1 = $('#inputImage1')[0].files[0].name;
    var value = parseInt($("#value").val());
    if(isNaN(value)){
        value = 0
    }
    sendImageValue("contorno", image1, value);
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

function sendTwoImagesValue(url, image1, image2, value){
    var data = {
        image1 : image1,
        image2 : image2,
        value: value
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
 $('.btn').mouseover(function(e) {
    reset();
    var infotoast = functionInformation.get(e.target.id);
    $('#title-toast').text(infotoast[0])
    $('#message-toast').html(infotoast[1])
    toastList.forEach(toast => toast.show());
 });
 $('.btn').click(function() {
	toastList.forEach(toast => toast.hide());
 });
 $('.btn').mouseout(function() {
	toastList.forEach(toast => toast.hide());
 });
 function reset(){
    $('#title-toast').html('');
    $('#message-toast').html('');
 }