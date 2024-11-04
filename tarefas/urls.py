from .views import home, criar_tarefa, tarefas
from django.urls import path, include


app_name = 'tarefas'
urlpatterns = [
    path('', home, name='home'),
    path('contas/', include('allauth.urls'), name='contas'),
    path('cadastrar/', tarefas, name='tarefas'),
    path('cadastrar/criar/', criar_tarefa, name='criar-tarefa'),
]
