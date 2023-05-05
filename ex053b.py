f = input('Digite uma frase: ').upper().strip()
ff = f.split()
j = ''.join(ff)
inv = ''
for l in range(len(f)-1,-1,-1):
    inv += j[l]
print('O inverso de {} é {}{}{}'.format(f, '\033[31m', inv, '\033[m'))
if inv == j:
    print('Temos um PALINDROMO')
else:
    print('A frase digitada NÃO É UM PALINDROMO')
