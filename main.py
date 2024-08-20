'''
Jogo de Adivinhação em Python
O programa escolhe um número aleatório de 1 a 10 para o usuário adivinhar
'''
import random
from time import sleep
from os import system

system('cls')
numero = random.randint(1, 10) # Escolhe um número aleatório entre 1 e 10
print("Escolhi um número aleatório de 1 a 10.")
sleep(2)
print("Tente adivinhar qual é!")
sleep(2)
system('cls')
palpite = 0 # Palpite do usuário
tentativas = 0  # Quantidade de tentativas

# Início do Loop de Jogo:
while palpite != numero:
    tentativas += 1

    print(f"{tentativas}ª tentativa") # Mostra a tentativa atual
    palpite = int(input("Seu palpite (1-10): ")) # Pede um palpite pro usuário
    system('cls')

    if palpite == numero: # Verifica se o palpite do usuário está correto
        # Verifica se o usuário acertou de primeira
        if tentativas == 1:
            print("Na mosca! Acertou de primeira!")
        else:
            print(f"Você acertou em {tentativas} tentativas!")
        
        # Pergunta para o usuário se ele quer jogar de novo
        dnv = str(input("Quer jogar de novo? (S/N)\n> ")).upper()
        if dnv == 'S': # Se sim, dá reset em tudo e escolhe outro número de 1-10
            numero = random.randint(1, 10)
            palpite = 0
            tentativas = 0
            system('cls')
        else:
            break
        
    # Dá dicas para o usuário caso o palpite dele esteja errado
    elif palpite < numero:
        print("Um pouco mais...")
    else:
        print("Um pouco menos...")
