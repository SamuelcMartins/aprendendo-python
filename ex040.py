n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
c = {'a' : '\033[34m', 'v' : '\033[31m', 'l' : '\033[m', 'ver' : '\033[32m'}
m = (n1 + n2) / 2
if m >= 7:
    print('Tirando {}{:.1f}{} e {}{:.1f}{}, a média do aluno é {}{:.1f}{}'.format(c['a'], n1, c['l'],c['a'], n2, c['l'], c['a'], m, c['l']))
    print('{}O aluno esta APROVADO{}.'.format(c['a'], c['l']))
elif m < 5:
    print('Tirando {}{:.1f}{} e {}{:.1f}{}, a média do aluno é {}{:.1f}{}'.format(c['v'], n1, c['l'], c['v'], n2, c['l'], c['v'], m, c['l']))
    print('{}O aluno esta de REPROVADO{}.'.format(c['v'], c['l']))
elif m >= 5 and m < 7:
    print('Tirando {}{:.1f}{} e {}{:.1f}{}, a média do aluno é {}{:.1f}{}'.format(c['ver'], n1, c['l'], c['ver'], n2, c['l'], c['ver'], m, c['l']))
    print('{}O aluno esta de RECUPERAÇÃO{}.'.format(c['ver'], c['l']))
