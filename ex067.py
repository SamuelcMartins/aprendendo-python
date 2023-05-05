c = 1
while True:
    v = int(input('Quer ver a tabuda de qual valor? '))
    print('-' * 30)
    if v < 0:
        break
    while c < 11:
        print(f'{v:2} X {c:2} = {v * c}')
        c += 1
    c = 1
print('PROGRAMA TABUADA ENCERRADO. volte sempre!')
