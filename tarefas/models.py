from django.db import models
from django.urls import reverse

# Create your models here.
class ListaTarefa(models.Model):
    nome = models.CharField(max_length=255, null=False)
    slug = models.CharField(max_length=255)
    tarefas = models.ManyToManyField("Tarefa")

    class Meta:
        verbose_name = "lista de tarefas"
        verbose_name_plural = "listas de tarefas"


    def __str__(self) -> str:
        return f"sua tarefa: {self.nome} e ({self.slug})"
    
    
    
class Tarefa(models.Model):
    nome = models.CharField(max_length=255)
    concluida = models.BooleanField(default=False)

    class Meta:
        verbose_name = "tarefa"
        verbose_name_plural = "tarefas"

    def __str__(self) -> str:
        return self.nome


