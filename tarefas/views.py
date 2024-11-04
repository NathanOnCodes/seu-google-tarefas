from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import Http404
from .models import ListaTarefa
from .forms import ListaTarefaForm

# Create your views here.


def home(request):
    tarefas = ListaTarefa.objects.all().order_by('-id')
    pagination = Paginator(tarefas, 5)
    
    context = {
        'posts': pagination.page(1)
    }
    return render(request, 'home.html', context)



def criar_tarefa(request):
    form = ListaTarefaForm()    
    return render(request, 'criar_tarefa.html', {'form': form})


def tarefas(request):
    if not request.POST:
        raise Http404()
    form = ListaTarefaForm(request.POST)
    return render(request, 'tarefa_criada.html', {'form': form})