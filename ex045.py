from random import randint
from time import sleep
i = ['pedra', 'papel', 'tesoura']
print('''Suas opções:
[ 0 ] pedra
[ 1 ] papel
[ 2 ] tesoura''')
j = int(input('Qual é a sua jogada? '))
c = randint(0, 2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('''{}
Computador jogou {}
jogador jogou {}
{}'''.format('-=' * 11, i[c], i[j], '-=' * 11))
if c == 0 and j == 1:
    print('JOGADOR VENCE')
elif c == 1 and j == 2:
    print('JOGADOR VENCE')
elif c == 2 and j == 0:
    print('JOGADOR VENCE')
elif j == 0 and c == 1:
    print('COMPUTADOR VENCE')
elif j == 1 and c == 2:
    print('computador vence')
elif j == 2 and c == 0:
    print('COMPUTADOR VENCE')
elif j == 0 and c == 0:
    print('EMPATE')
elif j == 1 and c == 1:
    print('EMPATE')
elif j == 2 and c == 2:
    print('empate')
else:
    print('JOGADA INVALIDA')
