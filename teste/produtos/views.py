from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

def ver_produto(request): 
    return render(request, 'ver_produto.html')

def colocar_produto(request): 
    return HttpResponse('Estou bem e você?')
