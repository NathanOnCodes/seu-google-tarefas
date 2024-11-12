from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('contas/', include('allauth.urls'), name='contas'),
    path('tarefas/criar/', views.criar_lista_tarefa, name='criar-lista'),
    path('tarefas/', views.lista_tarefas, name='lista-tarefas'),
    path('tarefas/<slug:slug>/atualizar/', views.atualizar_lista, name='atualizar-lista'),
    path('tarefas/<slug:slug>/deletar/', views.deletar_lista, name='deletar-lista'),
    path('tarefas/<slug:slug>/tarefa/<int:tarefa_id>/deletar/', views.deletar_tarefa, name='deletar-tarefa'),
    path('tarefas/<slug:slug>/tarefa/<int:tarefa_id>/atualizar/', views.atualizar_tarefa, name='atualizar-tarefa'),
]
