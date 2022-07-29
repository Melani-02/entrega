from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):
	return HttpResponse("Hola Django - Coder")

def hermana(request):
	return HttpResponse("Hermana mayor: Rocio")

def hermano(request):
	return HttpResponse("Hermano menor: Juan")

def mama(request):
	return HttpResponse("Mama: Paola")

def bienvenida(request):
	return render(request, "template1.html", context={})