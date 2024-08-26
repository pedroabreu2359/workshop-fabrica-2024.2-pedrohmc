import requests
from decimal import Decimal
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Vendedor, Comissao
from django.shortcuts import render

# Lista de moedas listadas
MOEDAS = [
    ('USD', 'Dólar Americano'),
    ('BRL', 'Real Brasileiro'),
    ('EUR', 'Euro'),
]

# Vendedor Views
class VendedorListView(ListView):
    model = Vendedor
    template_name = 'vendedores/vendedor_list.html'
    context_object_name = 'vendedores'

class VendedorCreateView(CreateView):
    model = Vendedor
    template_name = 'vendedores/vendedor_form.html'
    fields = ['nome', 'cpf']
    success_url = reverse_lazy('vendedor-list')

class VendedorUpdateView(UpdateView):
    model = Vendedor
    template_name = 'vendedores/vendedor_form.html'
    fields = ['nome', 'cpf']
    success_url = reverse_lazy('vendedor-list')

class VendedorDeleteView(DeleteView):
    model = Vendedor
    template_name = 'vendedores/vendedor_confirm_delete.html'
    success_url = reverse_lazy('vendedor-list')

# Comissao Views
class ComissaoListView(ListView):
    model = Comissao
    template_name = 'comissoes/comissao_list.html'
    context_object_name = 'comissoes'

class ComissaoCreateView(CreateView):
    model = Comissao
    template_name = 'comissoes/comissao_form.html'
    fields = ['vendedor', 'valor', 'data_comissao', 'descricao']
    success_url = reverse_lazy('comissao-list')

class ComissaoUpdateView(UpdateView):
    model = Comissao
    template_name = 'comissoes/comissao_form.html'
    fields = ['vendedor', 'valor', 'data_comissao', 'descricao']
    success_url = reverse_lazy('comissao-list')

class ComissaoDeleteView(DeleteView):
    model = Comissao
    template_name = 'comissoes/comissao_confirm_delete.html'
    success_url = reverse_lazy('comissao-list')

import requests
from django.shortcuts import render
from .models import Comissao

# Lista de moedas listadas
MOEDAS = [
    ('USD', 'Dólar Americano'),
    ('EUR', 'Euro'),
    ('BRL', 'Real Brasileiro'),
]

def converter_comissoes(request):
    taxa_cambio = None
    moeda_origem = request.GET.get('moeda_origem', 'USD')
    moeda_destino = 'BRL'  # Converter sempre para Real
    comissoes_convertidas = []

    if moeda_origem:
        url = f'https://api.exchangerate-api.com/v4/latest/{moeda_origem}'
        response = requests.get(url)
        dados = response.json()

        if dados.get('rates'):
            taxa_cambio = dados['rates'].get(moeda_destino)
            if taxa_cambio:
                # Obter todas as comissões na moeda de origem
                comissoes = Comissao.objects.filter(vendedor__cpf__isnull=False)

                for comissao in comissoes:
                    valor_convertido = comissao.valor * Decimal(taxa_cambio)
                    comissoes_convertidas.append({
                        'vendedor': comissao.vendedor.nome,
                        'valor_original': comissao.valor,
                        'valor_convertido': valor_convertido,
                        'taxa_cambio': taxa_cambio,
                        'moeda_origem': moeda_origem,
                    })

    context = {
        'moedas': MOEDAS,
        'moeda_origem': moeda_origem,
        'comissoes_convertidas': comissoes_convertidas,
    }

    return render(request, 'converter_comissoes.html', context)
