from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import ListaTarefa

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('home/')
    return redirect('login/')

def home(request):
    tarefas = ListaTarefa.objects.all().order_by('-id')
    pagination = Paginator(tarefas, 5)
    
    context = {
        'posts': pagination.page(1)
    }
    return render(request, 'index.html', context)


def get_login(request):
    return render(request, 'login.html')