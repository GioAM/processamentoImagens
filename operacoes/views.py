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
    resultado_image = "resultado" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'])
    resultado = functions.rgbtogray(image1)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)


def rgbtobit(request):
    limiar = 127
    resultado_image = "resultado" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'], 2)
    value = int(request.GET['value'])
    if value > 0:
        limiar = value
    resultado = functions.rgbtobit(image1, limiar)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)


def negativo(request):
    resultado_image = "resultado" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'])
    resultado = functions.negative(image1)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)


def histograma(request):
    resultado_image = "resultado" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'], 2)
    resultado = functions.equalizacao(image1)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)


def adicao(request):
    resultado_image = "resultado" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'])
    image2 = cv2.imread(path + request.GET['image2'])
    resultado = functions.adicao(image1, image2)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)


def subtracao(request):
    resultado_image = "resultado" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'])
    image2 = cv2.imread(path + request.GET['image2'])
    resultado = functions.subtracao(image1, image2)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)


def multiplicacao(request):
    limiar = 0.5
    resultado_image = "resultado" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'])
    value = int(request.GET['value'])
    if value > 0:
        limiar = value
    resultado = cv2.multiply(image1, limiar)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)


def divisao(request):
    limiar = 0.5
    resultado_image = "resultado" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'])
    value = int(request.GET['value'])
    if value > 0:
        limiar = value
    resultado = cv2.divide(image1, limiar)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)


def blending(request):
    resultado_image = "resultado" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'])
    image2 = cv2.imread(path + request.GET['image2'])
    resultado = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)


def f_and(request):
    resultado_image = "resultado" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'])
    image2 = cv2.imread(path + request.GET['image2'])
    resultado = functions.f_and(image1, image2)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)


def f_or(request):
    resultado_image = "resultado" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'])
    image2 = cv2.imread(path + request.GET['image2'])
    resultado = functions.f_or(image1, image2)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)


def f_xor(request):
    resultado_image = "resultado" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'])
    image2 = cv2.imread(path + request.GET['image2'])
    resultado = functions.f_xor(image1, image2)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)


def f_not(request):
    resultado_image = "resultado" + strftime("%Y%m%d%H%M%S", gmtime()) + ".png"
    image1 = cv2.imread(path + request.GET['image1'])
    resultado = functions.f_not(image1)
    cv2.imwrite(path_result + resultado_image, resultado)
    data = {'resultado': resultado_image}
    return JsonResponse(data)
