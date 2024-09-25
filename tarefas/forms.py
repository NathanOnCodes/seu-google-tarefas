from django import forms
from django.utils.text import slugify
from .models import ListaTarefa, Tarefa

class TarefaCriandoForm(forms.ModelForm):
    slug = forms.CharField(required=False, widget=forms.widgets.HiddenInput())
    class meta:
        model = ListaTarefa
        fields = ("nome", "slug")

    def limpar_nome(self) -> str:
        nome: str = self.cleaned_data.get("nome")
        slug = slugify(nome)
        if ListaTarefa.objects.filter(slug=slug).exists():
            raise forms.ValidationError(f"A Lista de tarefas {nome} ja existe")
        return nome
    
    def salvar(self, commit: bool = True) -> ListaTarefa: 
        lista_tarefa: ListaTarefa = super().save(commit)
        lista_tarefa.slug = slugify(lista_tarefa.nome)
        lista_tarefa.save()
        return lista_tarefa
    

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ("nome", "concluida")

    def limpar_nome(self) -> str:
        nome: str = self.cleaned_data["nome"]
        if Tarefa.objects.filter(nome=nome).exclude(concluida=True).exists():
            raise forms.ValidationError(f"A tarefa {nome} ja existe")
        return nome
    
    
    def salvar(self, commit: bool = True) -> Tarefa:
        tarefa: Tarefa = super().save(commit)
        tarefa.save()
        return tarefa