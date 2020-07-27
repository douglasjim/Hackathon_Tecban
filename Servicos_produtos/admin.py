from django.contrib import admin
from .models import Grafica,Empresas

# a parte la do django onde adicionamos os servicos etcc. fica nesta linha se a gente a apagar essa opcao vai sumir
admin.site.register(Grafica)
admin.site.register(Empresas)

