c = {'a': '\033[34m', 'l': '\033[m'}
maior = 0
menor = 0
for b in range(1,8):
    ano = int(input('Em que ano a {}° pessoa nasceu?'.format(b)))
    idade = 2022 - ano
    if idade < 18:
        menor += 1
    else:
        maior += 1
print('Ao todo tivemos {}{}{} pessoas maiores de idade'.format(c['a'], maior, c['l']))
print('E também tivemos {}{}{} pessoas menores de idade'.format(c['a'], menor, c['l']))
