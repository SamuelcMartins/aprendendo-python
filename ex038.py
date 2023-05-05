n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
c = {'a' : '\033[34m', 'l' : '\033[m'}
if n1 > n2:
    print('{}O PRIMEIRO valor é maior{}'.format(c['a'], c['l']))
elif n2 > n1:
    print('{}O SEGUNDO valor é maior{}'.format(c['a'], c['l']))
elif n1 == n2:
    print('{}Os dois valores são IGUAIS{}'.format(c['a'], c['l']))
