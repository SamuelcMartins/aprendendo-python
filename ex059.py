from time import sleep
c = {'a': '\033[34m', 'l': '\033[m', 'v': '\033[31m'}
valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
opção = 0
maior = 0
while opção != 5:
    print('=-=' * 10)
    print('''{}[ 1 ]somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa{}'''.format(c['a'], c['l']))
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        print('A soma entre {}{}{} e {}{}{} é {}{}{}'.format(c['a'], valor1, c['l'], c['a'], valor2, c['l'], c['v'],valor1 + valor2, c['l']))
    if opção == 2:
      print('O resultado de {}{}{} X {}{}{} é {}{}{}'.format(c['a'], valor1, c['l'], c['a'], valor2, c['l'], c['v'],valor1 * valor2, c['l']))
    if opção == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print('Entre {}{}{} e {}{}{} o maior valor é {}{}{}'.format(c['a'], valor1, c['l'], c['a'], valor2, c['l'],c['v'], maior, c['l']))
    if opção == 4:
        print('Informe os números novamente: ')
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
    if opção == 5:
        print('finalizando...')
    else:
        print('Opcão inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')