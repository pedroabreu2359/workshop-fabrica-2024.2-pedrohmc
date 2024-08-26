from django.db import models

class Vendedor(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.nome

class Comissao(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, related_name='comissoes')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_comissao = models.DateField()
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.vendedor.nome} - {self.valor} - {self.data_comissao}"
