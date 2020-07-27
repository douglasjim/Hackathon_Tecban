from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('<int:servico_id>',views.receita, name='receita'),
    path('<int:servico_id>',views.Empresas, name='empresas')
]