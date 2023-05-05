from random import randint
computador = randint(1, 10)
print('''Sou seu computador...
Acabei de pensar em um número de 0 e 10.
Será que você consegue adivinhar qual foi?''')
tentativas = 1
jogador = int(input('Qual é o seu palpite? '))
while jogador != computador:
    tentativas += 1
    if jogador < computador:
        print('Mais... tente mais uma vez.')
        jogador = int(input('Qual é o seu palpite? '))
    elif jogador > computador:
        print('Menos... Tente mais uma vez.')
        jogador = int(input('Qual é o seu palpite? '))
print('Acertou com {} tentativas'.format(tentativas))