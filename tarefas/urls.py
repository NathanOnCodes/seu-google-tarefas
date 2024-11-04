from .views import home, criar_tarefa
from django.urls import path, include

urlpatterns = [
    path('', home, name='home'),
    path('contas/', include('allauth.urls'), name='contas'),
    path('tarefa/criar', criar_tarefa, name='criar-tarefa'),
]
