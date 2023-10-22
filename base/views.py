from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Tarefa
from .forms import TarefaForm

def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('/')  

    context = {'page': page}
    return render(request, 'base/login_registro.html', context)


def registro(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Dados inválidos')

    context = {'form':form}        
    return render(request, 'base/login_registro.html', context)        

def logoutPage(request):
    logout(request)

    return redirect('login')

@login_required(login_url='login')
def listaTarefa(request):
    tarefas = Tarefa.objects.filter(user=request.user)

    cont = Tarefa.objects.filter(completo=False, user=request.user).count()

    search_area = request.GET.get('search-area') or ''

    if search_area:
        tarefas = Tarefa.objects.filter(titulo__startswith=search_area)


    context = {'tarefas': tarefas, 'cont':cont}

    return render(request, 'base/lista_tarefa.html', context)
    
@login_required(login_url='login')    
def detalhesTarefa(request, pk):
    tarefa = Tarefa.objects.get(id=pk)


    context = {'tarefa':tarefa}
    return render(request, 'base/detalhes_tarefa.html', context) 

@login_required(login_url='login')
def adicionarTarefa(request):
    form = TarefaForm

    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            user.save() 
            return redirect('/')

    context = {'form':form}
    return render(request, 'base/adicionar_tarefa.html', context)

@login_required(login_url='login')
def atualizarTarefa(request, pk):
    tarefa = Tarefa.objects.get(id=pk)
    form = TarefaForm(instance=tarefa)

    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'base/atualizar_tarefa.html', context)

@login_required(login_url='login')
def apagarTarefa(request, pk):
    tarefa = Tarefa.objects.get(id=pk)

    if request.method == 'POST':
        tarefa.delete()
        return redirect('/')

    context = {'tarefa': tarefa}
    return render(request, 'base/apagar_tarefa.html', context)

