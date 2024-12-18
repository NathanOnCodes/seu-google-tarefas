import pytest
from tarefas.models import ListaTarefa, Tarefa
from django.urls import reverse



@pytest.mark.django_db
class TestTarefaListaModel:
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
    

    def test_verbose_nmar(self):
        lista = ListaTarefa.objects.create(
            nome="lista de tarefas",
            slug="lista-tarefas"
        )
        assert lista._meta.verbose_name == "lista de tarefas"
        assert lista._meta.verbose_name_plural == "listas de tarefas"


@pytest.mark.django_db
class TestTarefaModel:
    def test_criar_tarefa(self):
        tarefa = Tarefa(
            nome="Tarefa 1",
        )
        assert tarefa.nome == "Tarefa 1"
    
    def test_str_repr(self):
        tarefa = Tarefa(
            nome="compras",
        )
        assert str(tarefa) == "compras"

    def concluir_tarefa(self):
        tarefa = Tarefa.objects.create(
            nome="estudar",
            concluida=False
        )

        assert tarefa.concluida == False

        tarefa.concluida = True
        tarefa.save()

        tarefa_atualizada = Tarefa.objects.get(id=tarefa.id)
        assert tarefa_atualizada.concluida
    

    def test_tarefa_verbose_name(self):
        tarefa = Tarefa.objects.create(nome = "mercado")
        assert tarefa._meta.verbose_name == "tarefa"
        assert tarefa._meta.verbose_name_plural == "tarefas"