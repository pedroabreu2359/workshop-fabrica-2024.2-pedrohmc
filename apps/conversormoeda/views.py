import requests
from django.shortcuts import render

# Lista de moedas listadas
MOEDAS = [
    ('USD', 'Dólar Americano'),
    ('BRL', 'Real Brasileiro'),
    ('EUR', 'Euro'),
]

def conversao_moedas(request):
    taxa_cambio = None
    moeda_origem = request.GET.get('moeda_origem', 'USD')
    moeda_destino = request.GET.get('moeda_destino', 'BRL')
    valor = request.GET.get('valor', 1)

    if moeda_origem and moeda_destino and valor:
        url = f'https://api.exchangerate-api.com/v4/latest/{moeda_origem}'
        response = requests.get(url)
        dados = response.json()

        if dados.get('rates'):
            taxa_cambio = dados['rates'].get(moeda_destino)
            if taxa_cambio:
                valor_convertido = float(valor) * taxa_cambio
                context = {
                    'moeda_origem': moeda_origem,
                    'moeda_destino': moeda_destino,
                    'valor': valor,
                    'valor_convertido': valor_convertido,
                    'taxa_cambio': taxa_cambio,
                    'moedas': MOEDAS,
                }
                return render(request, 'conversao_moedas.html', context)
            
    context = {
        'moedas': MOEDAS,
        'moeda_origem': moeda_origem,
        'moeda_destino': moeda_destino,
        'valor': valor,
    }

    return render(request, 'conversao_moedas.html', context)
