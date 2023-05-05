n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
c = {'a' : '\033[34m', 'v' : '\033[31m', 'l' : '\033[m'}
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    if n1 == n2 and n2 == n3:
        print('{}Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO{}'.format(c['a'], c['l']))
    elif n1 != n2 != n3 != n1:
        print('{}Os segmentos acima PODEM FORMAR um triângulo ESCALENO{}'.format(c['a'], c['l']))
    else:
        print('{}Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES{}'.format(c['a'], c['l']))
else:
    print('{}Os segmentos acima NÃO PODEM FORMAR triângulo{}'.format(c['v'], c['l']))
