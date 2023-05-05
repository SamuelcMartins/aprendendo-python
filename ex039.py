n = int(input('Ano de nascimento: '))
c = {'a' : '\033[34m', 'l' : '\033[m'}
a = 2022
i = 2022 - n
print('Quem nasveu em {}{}{} tem {}{}{} anos em {}{}{}'.format(c['a'], n, c['l'], c['a'], i, c['l'], c['a'], a, c['l']))
if i < 18:
    f = 18 - i
    print('Ainda faltam {}{}{} anos para o alistamento'.format(c['a'], f, c['l']))
    print('seu alistamento será em {}{}{}'.format(c['a'], a + f, c['l']))
elif i > 18:
    f = i - 18
    print('Você ja deveria ter se alistado ha {}{}{} anos.'.format(c['a'], f, c['l']))
    print('Seu alistamento foi em {}{}{}.'.format(c['a'], a - f, c['l']))
else:
    print('Você deve se alistar IMEDIATAMENTE!')
