from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.http import HttpResponse
from .models import Grafica,Empresas
from urllib import request


def index(request):

    servicos = Grafica.objects.all()


    dados = {
        'servicos': servicos
    }

    return render(request,'index.html',dados)

def receita(request, servico_id):
    servico = get_object_or_404(Grafica, pk=servico_id)
    servico_a_exibit = {
        'servico': servico
    }
    return render(request,'receita.html',servico_a_exibit)

def Empresas(request, servico_id):
    servico = get_object_or_404(Empresas, pk=servico_id)
    servico_a_exibit = {
        'servico': servico
    }
    return render(request,'empresa.html',servico_a_exibit)