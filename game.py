import random

print('----- JOGO DA ADVINHAÇÃO -----')
secret = random.randint(1,10)
tentativas = 0

while True:
    number = int(input('Digite um número de 1 a 10: '))
    tentativas += 1

    if number < secret:
        print('O número secreto é maior')
    elif number > secret:
        print('O número secreto é menor')
    else:
        print(f'Você acertou em {tentativas} tentativas. O número correto é {number}')
        break