from django.shortcuts import render
from nuevaappdjango.models import Familia #importo la clase para usarla

# Create your views here.

#mi primer vista de familia

def mostrar_famlia(request):
    context = {}
    context ["familiar"] = familia.objects.all()
    return render (request, "nuevaappdjango/Familia.html", context)

