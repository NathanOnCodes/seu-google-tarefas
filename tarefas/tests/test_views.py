import pytest
from tarefas.models import ListaTarefa
from django.urls import reverse
from django.test import Client

@pytest.mark.django_db
def test_criar_lista_tarefa_view():
    client = Client()

    form_data = {
        'nome_lista': 'Nova Lista de Tarefas',
        'nome_tarefa': 'Tarefa 1\nTarefa 2\nTarefa 3'
    }


    response = client.post(reverse('criar-lista'), form_data)
    assert response.status_code == 302

    lista = ListaTarefa.objects.get(nome='Nova Lista de Tarefas')
    assert lista.slug == 'nova-lista-de-tarefas'
    assert lista.tarefas.count() == 3