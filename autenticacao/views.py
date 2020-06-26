from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def logar_usuario(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('listar_clientes')
        else:
            messages.error(request,  "Usuário ou senha incorretos")
            return redirect('login')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render (request, 'login.html', context)


def deslogar_usuario (request):
    logout(request)
    return redirect('login')


def novo_usuario(request):
    if request.method == 'POST':
        form  = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,  'Cadastro realizado com sucesso!')
            return redirect('login')
    else:
        form = UserCreationForm()
    context ={
        'form':form
    }
    return render(request, 'novo_usuario.html', context)
