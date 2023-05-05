print('Gerador de PA\n', '-=' * 10)
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = 10
pa = p
while c > 0:
    print('{} → '.format(pa), end='')
    pa += r
    c -= 1
print('fim')
