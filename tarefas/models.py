from django.db import models
from django.urls import reverse

# Create your models here.
class ListaTarefa(models.Model):
    nome = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)

    class meta:
        verbose_name = "Lista de Tarefas"
        verbose_name_plural = "Listas de Tarefas"

    def __str__(self) -> str:
        return f"sua tarefa: {self.nome} e ({self.slug})"
    
    def get_url_absoluta(self) -> str:
        return reverse("tarefas:tarefas", kwargs={"slug": self.slug})
    
    @property
    def esta_completa(self):
        return not self.slug
    
class Tarefa(models.Model):
    lista_tarefa = models.ForeignKey(
        ListaTarefa,
        related_name="tarefas",
        on_delete=models.CASCADE,
    )
    nome = models.CharField(max_length=255)
    concluida = models.BooleanField(default=False)

    class meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"

