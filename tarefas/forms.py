from django import forms
from .models import ListaTarefa


class ListaTarefaForm(forms.ModelForm):
    class meta:
        model = ListaTarefa
        fields = ["nome", "slug", "tarefas"]