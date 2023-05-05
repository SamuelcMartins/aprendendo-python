print('-' * 30, '\nSequência de ibonacci\n'+'-' * 30)
t = int(input('Quantos termos você quer mostrar? '))
print('=' * 30)
t1 = 0
t2 = 0
ta = 0
while t > 0:
    print('{} → '.format(ta), end='')
    t -= 1
    ta = t1 + t2
    if ta == 0:
        ta = 1
    t1 = t2
    t2 = ta
print('FIM')
