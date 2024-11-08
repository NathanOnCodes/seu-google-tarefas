from . import views
from django.urls import path, include

app_name = 'todo'
urlpatterns = [
    path('', views.home, name='home'),
    path('contas/', include('allauth.urls'), name='contas'),
    path('tarefas/criar/', views.criar_lista_tarefa, name='criar-lista'),
    path('tarefas/', views.lista_tarefas, name='lista-tarefas'),
]
