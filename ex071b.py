print(f'''{'=' * 30}
{"BANCO CEV" :^30}
{'=' * 30}''')
while True:
    try:
        saque = int(input('Que valor você quer sacar? R$ '))
        break
    except ValueError:
        print('Valor inválido, por favor digite um valor inteiro.')
tot = saque
ced = 50
totced = 0
while True:
    if tot >= ced:
        tot -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if tot ==0:
            break


