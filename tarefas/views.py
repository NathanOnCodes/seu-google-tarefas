from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import include
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
    context = {
        "form": form
    }
    return render(request, 'criar_tarefa.html', context)

