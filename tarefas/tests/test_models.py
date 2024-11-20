import pytest
from tarefas.models import ListaTarefa, Tarefa
from django.urls import reverse



@pytest.mark.django_db
class TestTarefaLista:
    def test_criar_lista(self):
        lista = ListaTarefa(
            nome="Minha lista",
            slug="minha-lista"
        )

        assert lista.nome == "Minha lista"
        assert lista.slug == "minha-lista"

    def test_str_representacao(self):
        lista = ListaTarefa.objects.create(
            nome="Minha lista",
            slug="minha-lista"
        )

        assert type(str(lista)) == str


    def test_adicionar_tarefa(self):
        lista = ListaTarefa.objects.create(
            nome="Minha lista",
            slug="minha-lista"
        )      
        tarefa1 = Tarefa.objects.create(nome="Tarefa 1")
        tarefa2 = Tarefa.objects.create(nome="Tarefa 2")

        lista.tarefas.add(tarefa1, tarefa2)
        lista.save()

        assert lista.tarefas.count() == 2
        assert list(lista.tarefas.values_list('nome', flat=True)) == ["Tarefa 1", "Tarefa 2"]
