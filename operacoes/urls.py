from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rgbtobit', views.rgbtobit, name='rgbtobit'),
    path('rgbtogray', views.rgbtogray, name='rgbtogray'),
    path('negativo', views.negativo, name='negativo'),
    path('histograma', views.histograma, name='histograma'),
    path('adicao', views.adicao, name='adicao'),
    path('subtracao', views.subtracao, name='subtracao'),
    path('divisao', views.divisao, name='divisao'),
    path('multiplicacao', views.multiplicacao, name='multiplicacao'),
    path('blending', views.blending, name='blending'),
    path('fand', views.f_and, name='fand'),
    path('for', views.f_or, name='for'),
    path('fxor', views.f_xor, name='fxor'),
    path('fnot', views.f_not, name='fnot'),
    path('media', views.media, name='media'),
    path('mediana', views.mediana, name='mediana'),
    path('gaussiana', views.gaussiana, name='gaussiana'),
    path('dilatacao', views.dilatacao, name='dilatacao'),
    path('erosao', views.erosao, name='erosao'),
    path('abertura', views.abertura, name='abertura'),
    path('fechamento', views.fechamento, name='fechamento'),
    path('contorno', views.contorno, name='contorno'),
]
