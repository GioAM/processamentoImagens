from django.http import JsonResponse
from django.shortcuts import render
from time import gmtime, strftime
from django.conf import settings
from . import functions
import cv2
path = "C:/ProjetosGit/processamentoimagens/imagens/"
path_result = "C:/ProjetosGit/processamentoimagens/processamentoimagens/static/img/resultado/"


def index(request):
    return render(request, 'index.html')


def rgbtogray(request):
    print(settings.MEDIA_URL)
    resultado_image = "rgbtogray" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'])
    resultado = functions.rgbtogray(image1)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)


def rgbtobit(request):
    limiar = 127
    resultado_image = "rgbtobit" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'], 2)
    value = int(request.GET['value'])
    if value > 0:
        limiar = value
    resultado = functions.rgbtobit(image1, limiar)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)


def negativo(request):
    resultado_image = "negativo" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'])
    resultado = functions.negative(image1)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)


def histograma(request):
    resultado_image = "histograma" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'], 2)
    resultado = functions.equalizacao(image1)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)


def adicao(request):
    resultado_image = "adicao" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'])
    image2 = cv2.imread(path + request.GET['image2'])
    resultado = functions.adicao(image1, image2)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)


def subtracao(request):
    resultado_image = "subtracao" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'])
    image2 = cv2.imread(path + request.GET['image2'])
    resultado = functions.subtracao(image1, image2)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)


def multiplicacao(request):
    limiar = 1.5
    resultado_image = "multiplicacao" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'])
    value = float(request.GET['value'])
    if value > 0:
        limiar = value
    resultado = functions.multiplicacao(image1, limiar)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)


def divisao(request):
    limiar = 4
    resultado_image = "divisao" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'])
    value = float(request.GET['value'])
    if value > 0:
        limiar = value
    resultado = functions.divisao(image1, limiar)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)


def blending(request):
    limiar = 0.8
    resultado_image = "blending" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'])
    image2 = cv2.imread(path + request.GET['image2'])
    value = float(request.GET['value'])
    if value > 0:
        limiar = value
    limiar2 = 1 - limiar
    resultado = cv2.addWeighted(image1, limiar, image2, limiar2, 0)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)


def f_and(request):
    resultado_image = "and" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'])
    image2 = cv2.imread(path + request.GET['image2'])
    resultado = functions.f_and(image1, image2)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)


def f_or(request):
    resultado_image = "or" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'])
    image2 = cv2.imread(path + request.GET['image2'])
    resultado = functions.f_or(image1, image2)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)


def f_xor(request):
    resultado_image = "xor" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'])
    image2 = cv2.imread(path + request.GET['image2'])
    resultado = functions.f_xor(image1, image2)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)


def f_not(request):
    resultado_image = "not" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'])
    resultado = functions.f_not(image1)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)


def media(request):
    limiar = 5
    resultado_image = "media" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'])
    value = int(request.GET['value'])
    if value > 0:
        limiar = value
    resultado = cv2.blur(image1, (limiar, limiar))
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)


def mediana(request):
    limiar = 5
    resultado_image = "mediana" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'])
    value = int(request.GET['value'])
    if value > 0:
        limiar = value
    resultado = cv2.medianBlur(image1, limiar)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)


def gaussiana(request):
    limiar = 5
    resultado_image = "gaussiana" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'])
    value = int(request.GET['value'])
    if value > 0:
        limiar = value
    resultado = cv2.GaussianBlur(image1, (limiar, limiar), 5)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)


def dilatacao(request):
    limiar = 5
    resultado_image = "dilatacao" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'])
    value = int(request.GET['value'])
    if value > 0:
        limiar = value
    elemento = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (limiar, limiar))
    resultado = cv2.dilate(image1, elemento, iterations=3)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)


def erosao(request):
    limiar = 5
    resultado_image = "erosao" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'])
    value = int(request.GET['value'])
    if value > 0:
        limiar = value
    elemento = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (limiar, limiar))
    resultado = cv2.erode(image1, elemento, iterations=3)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)


def abertura(request):
    limiar = 3
    resultado_image = "abertura" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'])
    value = int(request.GET['value'])
    if value > 0:
        limiar = value
    elemento = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (limiar, limiar))
    resultado = cv2.morphologyEx(image1, cv2.MORPH_OPEN, elemento)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)


def fechamento(request):
    limiar = 5
    resultado_image = "fechamento" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'])
    value = int(request.GET['value'])
    if value > 0:
        limiar = value
    elemento = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (limiar, limiar))
    resultado = cv2.morphologyEx(image1, cv2.MORPH_CLOSE, elemento)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)


def contorno(request):
    limiar = 3
    resultado_image = "contorno" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'])
    value = int(request.GET['value'])
    if value > 0:
        limiar = value
    elemento = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (limiar, limiar))
    resultado = cv2.morphologyEx(image1, cv2.MORPH_GRADIENT, elemento)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)

