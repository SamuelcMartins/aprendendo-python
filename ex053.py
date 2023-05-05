f = input('Digite uma frase: ').strip().upper()
ff = f.split()
fr =''.join(ff)
inv = fr[len(fr)::-1]
print('O inverso de {} é {}{}{}'.format(f, '\033[31m', inv, '\033[m'))
if inv == fr:
    print('Temos um PALINDROMO')
else:
    print('A frase digitada NÃO É UM PALINDROMO')
