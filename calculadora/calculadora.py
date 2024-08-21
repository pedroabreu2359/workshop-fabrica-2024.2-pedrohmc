from operacoes import somar, subtrair, multiplicar, dividir, raiz_quadrada, fatorial

def calcular():
    opcao = int(input(
    """Escolha sua opção:
[1] Soma
[2] Subtração
[3] Multiplicação
[4] Divisão
[5] Raiz Quadrada
[6] Fatorial
> """))
    match opcao:
        case 1:
            num1 = float(input("Informe o 1º número: "))
            num2 = float(input("Informe o 2º número: "))
            print(f"{num1} + {num2} = {somar(num1, num2)}")
        case 2:
            num1 = float(input("Informe o 1º número: "))
            num2 = float(input("Informe o 2º número: "))
            print(f"{num1} - {num2} = {subtrair(num1, num2)}")
        case 3:
            num1 = float(input("Informe o 1º número: "))
            num2 = float(input("Informe o 2º número: "))
            print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
        case 4:
            num1 = float(input("Informe o 1º número: "))
            num2 = float(input("Informe o 2º número: "))
            print(f"{num1} / {num2} = {dividir(num1, num2)}")
        case 5:
            num = float(input("Informe o número: "))
            print(f"√{num} = {raiz_quadrada(num)}")
        case 6:
            num = int(input("Informe o número: "))
            print(f"{num}! = {fatorial(num)}")
        case _:
            print("Opção inválida, tente novamente.")
