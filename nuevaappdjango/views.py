from django.shortcuts import render
from nuevaappdjango.models import Familia #importo la clase para usarla

# Create your views here.

#mi primer vista de familia

def mostrar_famlia(request):
    context = {}
    context ["familia"] = Familia.objects.all()
    return render (request, "nuevaappdjango/familia.html", context)

