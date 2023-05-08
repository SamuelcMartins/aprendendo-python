from random import randint
print('=-' * 15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*15)
count = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    soma = computador + jogador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Impar [P/I] ')).strip().upper()
    par_impar = 'par' if soma % 2 == 0 else 'impar'
    print('=-' * 15)
    print(f'Você jogou {jogador} e o computador {computador}. total de {soma} Deu {par_impar}')
    print('=-' * 15)
    if (par_impar == 'par' and escolha == 'P') or (par_impar == 'impar' and escolha == 'I'):
        print('Você VENCEU!')
        count += 1
    else:
        print('Você PERDEU!')
        break
    print('vamos jogar novamente...')
print(f'GAME OVER! Você venceu {count}')
