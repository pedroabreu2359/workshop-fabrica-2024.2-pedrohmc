'''
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao(str(input("Informe seu nome: ")))

def soma(a, b):
    return a + b

resultado = soma(int(input("Informe um número: ")), int(input("Informe outro número: ")))
print(f"O resultado é {resultado}")
'''
def fatorial(x):
    if x == 1:
        return 1
    else:
        return x * fatorial(x - 1)

num = int(input("Informe um número: "))
print(f"{num}! = {fatorial(num)}")
