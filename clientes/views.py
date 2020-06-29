from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm

@login_required
def listar_clientes(request):
    busca = request.GET.get('busca')
    if busca:
        clientes_list = Cliente.objects.filter(nomecompleto__icontains=busca).order_by('nomecompleto')
    else:
        clientes_list = Cliente.objects.all().order_by('nomecompleto')   
    paginator = Paginator(clientes_list, 10)
    page = request.GET.get('page')
    clientes = paginator.get_page(page)
    context = {
        'clientes' : clientes
	}
    return render(request, 'listar_clientes.html', context)


@login_required
def cadastrar_cliente(request): 
    form =  ClienteForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            cliente = form.save()
            messages.success(request,  'Cliente cadastrado com sucesso!')
            return redirect('visualizar_cliente', cliente.id)
            #return render(request,'visualizar_cliente.html',{'cliente' : form.cleaned_data})
        else:
            messages.error(request,  'Erro ao cadastrar o cliente. Contate o administrador')
    return render(request,'cadastrar_cliente.html',{'form': form})


@login_required
def atualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(request.POST or None, instance=cliente)
    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,  'Cliente atualizado com sucesso!')
            return render(request, 'visualizar_cliente.html', {'cliente': cliente})
        else:
            messages.error(request,  'Erro ao alterar o contato')
    context = {
        'form': form,
        'cliente' : cliente
    }
    return render(request,'atualizar_cliente.html',context)


@login_required
def visualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    context = {
        'cliente' : cliente
    }
    return render(request,'visualizar_cliente.html',context)


@login_required
def excluir_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    cliente.delete()
    messages.success(request, 'Cliente excluído com sucesso')

    return redirect('listar_clientes')


@login_required
def clonar_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    cliente.pk = None
    cliente.save()
    messages.success(request,  'Cliente clonado com sucesso!') 
    return redirect('listar_clientes')