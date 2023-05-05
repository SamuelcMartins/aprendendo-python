print('=' * 30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('=' * 30)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for b in range(p, (p+10)*r, r):
    print('\033,b, end='→')
print('Acabou')