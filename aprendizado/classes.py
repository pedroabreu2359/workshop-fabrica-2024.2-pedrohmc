from time import sleep

class Veiculo:
    def __init__(self, marca, modelo, ano, cor, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.preco = preco
    
    def consultar(self):
        print("\nVeículos disponíveis:")
        print(f"{self.marca} {self.modelo} {self.ano} {self.cor}\nPreço: R${self.preco}\n")
    
    def test_drive(self):
        print(f"\nTest-Drive para o {self.marca} {self.modelo} {self.cor} marcado com sucesso!\n")
    
    def comprar(self):
        print(f"\nErro: você está liso\n")

carro = Veiculo(marca="Honda", modelo="Civic SI", ano="2008", cor="Prata", preco=88900)

opcao = 0
print("Lojão dos Automóveis")
while True:
    print("""[1] Consultar veículos
[2] Marcar um test-drive
[3] Comprar
[4] Sair""")
    opcao = int(input("Escolha uma opção: "))
    match opcao:
        case 1:
            carro.consultar()
        case 2:
            carro.test_drive()
        case 3:
            carro.comprar()
        case 4:
            break
        case _:
            print("\nOpção inválida, tente novamente\n")
