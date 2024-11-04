from .views import home, criar_tarefa, tarefas
from django.urls import path, include

urlpatterns = [
    path('', home, name='home'),
    path('contas/', include('allauth.urls'), name='contas'),
    path('tarefas/', tarefas, name='tarefas'),
    path('tarefas/criar', criar_tarefa, name='criar-tarefa'),
]
