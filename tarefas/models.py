from django.db import models
from django.urls import reverse

# Create your models here.
class ListaTarefa(models.Model):
    nome = models.CharField(max_length=255, null=False)
    slug = models.CharField(max_length=255)
    tarefas = models.ManyToManyField("Tarefa")

    class meta:
        verbose_name = "lista de tarefas"
        verbose_name_plural = "listas de tarefas"


    def __str__(self) -> str:
        return f"sua tarefa: {self.nome} e ({self.slug})"
    
    def get_url_absoluta(self) -> str:
        return reverse("tarefas:tarefas", kwargs={"slug": self.slug})
    
    
class Tarefa(models.Model):
    nome = models.CharField(max_length=255)
    concluida = models.BooleanField(default=False)

    class meta:
        verbose_name = "tarefa"
        verbose_name_plural = "tarefas"

    def __str__(self) -> str:
        return self.nome


