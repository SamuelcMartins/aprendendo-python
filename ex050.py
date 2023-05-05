s = 0
c = 0
for b in range(1,7):
    n = int(input('\033[31mDigite o {}° valor: '.format(b)))
    if n % 2 == 0:
        s += n
        c += 1
print('\033[34mVocê informou {} números PARES e a soma foi {}\033[m'.format(c,s))
