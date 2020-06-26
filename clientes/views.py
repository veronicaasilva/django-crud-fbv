from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Cliente
from .forms import ClienteForm

def listar_clientes(request):
    '''
    busca = request.GET.get('busca')
    if busca:
        clientes_list = Cliente.objects.filter(nomecompleto__icontains=busca)
    else:
        clientes_list = Cliente.objects.all()   
'''
    clientes = Cliente.objects.all()  
    context = {
        'clientes' : clientes
	}
    return render(request, 'listar_clientes.html', context)


def clonar_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    cliente.pk = None
    cliente.save()
    messages.success(request,  'Cliente clonado com sucesso!') 
    return redirect('listar_clientes')


def cadastrar_cliente(request): 
    form =  ClienteForm(request.POST or None, request.FILES or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,  'Cliente cadastrado com sucesso!')
            return redirect('listar_clientes')
        else:
            messages.error(request,  'Erro ao cadastrar o cliente. Contate o administrador')
    context = {
        'form': form
    }
    return render(request,'cadastrar_cliente.html',context)

def atualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(request.POST or None, request.FILES or None, instance=cliente)
    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,  'Cliente atualizado com sucesso!')
            #return render(request, 'visualizarcadastro.html', {'cliente': cliente})
            return redirect('listar_clientes')
        else:
            messages.error(request,  'Erro ao alterar o contato')
    context = {
        'form': form,
        'cliente' : cliente
    }
    return render(request,'atualizar_cliente.html',context)
