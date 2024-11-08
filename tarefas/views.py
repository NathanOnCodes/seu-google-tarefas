from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.utils.text import slugify
from .models import ListaTarefa, Tarefa
from .forms import ListaTarefaForm

# Create your views here.


def home(request):
    tarefas = ListaTarefa.objects.all().order_by('-id')
    pagination = Paginator(tarefas, 5)
    
    context = {
        'posts': pagination.page(1)
    }
    return render(request, 'home.html', context)


def criar_lista_tarefa(request):
    if request.method == 'POST':
        form = ListaTarefaForm(request.POST)
        if form.is_valid():
            lista = ListaTarefa(
                nome=form.cleaned_data['nome_lista'],
                slug=slugify(form.cleaned_data['nome_lista'])
            )
            lista.save()
            tarefas_texto = form.cleaned_data['tarefas'].split('\n')
            for texto in tarefas_texto:
                nova_tarefa = Tarefa.objects.create(nome=texto.strip())
                lista.tarefas.add(nova_tarefa)
            return redirect('todo:listar_tarefas')
    else:
        form = ListaTarefaForm()
    return render(request, 'form.html', {'form': form})
            

def lista_tarefas(request):
    listas = ListaTarefa.objects.all()
    return render(request, 'lista_tarefas.html', {'listas': listas})