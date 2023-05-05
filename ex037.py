n = int(input('Digite um número: '))
c = {'a' : '\033[34m', 'l' : '\033[m', 'ver' : '\033[32m'}
print('Escolha uma das bases para conversão:')
print('''{}[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL{}'''.format(c['a'], c['l']))
o = int(input('\033[34mSua opção: \033[m'))
if o == 1:
    print('{}{}{} convertido para BINÁRIO é igual a {}{}{}'.format(c['ver'], n, c['l'], c['ver'], bin(n)[2:], c['l']))
elif o == 2:
    print('{}{}{} convertido para OCTAL é igual a {}{}{}'.format(c['ver'], n, c['l'], c['ver'], oct(n)[2:], c['ver'], c['l']))
elif o == 3:
    print('{}{}{} convertido para HEXADECIMAL é igual a {}{}{}'.format(c['ver'], n, c['l'], c['ver'], hex(n)[2:], c['l']))
else:
    print('{}Opçao invalida tente novamente{}'.format(c['a'], c['l']))
