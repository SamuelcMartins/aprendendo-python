c = {'a': '\033[34m', 'l': '\033[m'}
maior = 0
menor = 0
for b in range(1, 6):
    peso = float(input('Pesp da {}° pessoa: '.format(b)))
    if b == 1:
        maior = b
        menor = b
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}{:.1f}{}Kg'.format(c['a'], maior, c['l']))
print('O menor peso lido foi de {}{:.1f}{}Kg'.format(c['a'], menor, c['l']))
