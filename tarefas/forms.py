from django import forms
from .models import ListaTarefa

class ListaTarefaForm(forms.ModelForm):
    nome_lista = forms.CharField(
        label="Nome da lista:",
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    nome_tarefa = forms.CharField(
        label='Nome da tarefa:',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Digite uma tarefa por linha'
        }),
        help_text='Digite uma tarefa por linha'
    )

    class Meta:
        model = ListaTarefa
        fields = ['nome_lista']