n = int(input('Digite um número: '))
c = {'a' : '\033[34m', 'v' : '\033[31m', 'l' : '\033[m'}
d = 0
for b in range(1, n+1):
    if n % b == 0:
        print(c['a'], b, c['l'], end=' ')
        d += 1
    else:
        print(c['v'], b, c['l'], end=' ')
print('\nO número {} foi divisivel {} vezes'.format(n, d))
if d == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
