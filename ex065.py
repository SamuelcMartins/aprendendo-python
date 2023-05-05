n = s = m = count = maior = menor = 0
c = 'S'
while 'S' in c:
    n = int(input('Digite um número: '))
    c = input('Quer continuar? [S/N]').strip().upper()
    s += n
    count += 1
    if count == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
m = s / count
print('Você digitou {} números e a média foi {}'.format(count, m))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
