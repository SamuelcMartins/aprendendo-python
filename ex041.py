a = int(input('Ano de nascimento: '))
i = 2022 - a
c = {'a': '\033[34m', 'l': '\033[m', 'ver': '\033[32m'}
print('{}O atleta tem {} anos.{}'.format(c['a'], i, c['l']))
if i <= 9:
    cl = 'MIRIM'
elif i <= 14:
    cl = 'INFANTIL'
elif i <= 19:
    cl = 'JÚNIOR'
elif i <= 25:
    cl = 'SÊNIOR'
else:
    cl = 'MASTER'
print('{}Classifição: {}{}{}'.format(c['a'], c['ver'], cl, c['l']))
