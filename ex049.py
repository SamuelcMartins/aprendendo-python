n = int(input('Digite um número para ver sua tabuada: '))
c = {'a' : '\033[34m', 'l' : '\033[m'}
for b in range(1, 11):
    print('{}{} X {:2} = {}{}'.format(c['a'], n, b, n * b, c['l']))
