from django.urls import path
from .views import (converter_comissoes,
    VendedorListView, VendedorCreateView, VendedorUpdateView, VendedorDeleteView,
    ComissaoListView, ComissaoCreateView, ComissaoUpdateView, ComissaoDeleteView
)

urlpatterns = [
    path('converter-comissoes/', converter_comissoes, name='converter-comissoes'),

    # URLs para Vendedor
    path('vendedores/', VendedorListView.as_view(), name='vendedor-list'),
    path('vendedores/novo/', VendedorCreateView.as_view(), name='vendedor-create'),
    path('vendedores/<int:pk>/editar/', VendedorUpdateView.as_view(), name='vendedor-update'),
    path('vendedores/<int:pk>/deletar/', VendedorDeleteView.as_view(), name='vendedor-delete'),

    # URLs para Comissão
    path('comissoes/', ComissaoListView.as_view(), name='comissao-list'),
    path('comissoes/nova/', ComissaoCreateView.as_view(), name='comissao-create'),
    path('comissoes/<int:pk>/editar/', ComissaoUpdateView.as_view(), name='comissao-update'),
    path('comissoes/<int:pk>/deletar/', ComissaoDeleteView.as_view(), name='comissao-delete'),
]