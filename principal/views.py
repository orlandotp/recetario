# Create your views here.
# Importaciones
from principal.models import Bebida
from django.shortcuts import render_to_response
# Funcion
def lista_bebidas(request):
	bebidas = Bebidas.objects.all()
	return render_to_response('lista_bebidas.html',{'lista':bebidas})
