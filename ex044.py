p = float(input('Preço das compras: R$ '))
c = {'a' : '\033[34m', 'l' : '\033[m', 'ver' : '\033[32m'}
print('{}FORMAS DE PAGAMENTO'.format(c['a']))
print('''[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2X no cartão
[ 4 ] 3X ou mais no cartão{}'''.format(c['l']))
o = int(input('\033[34mQual é a sua opção? \033[m'))
if o == 1:
    t = p - (p * 10 / 100)
elif o == 2:
    t = p - (p * 5 / 100)
elif o == 3:
    t = p
    print('{}Sua compra será pacelada em 2X de R${:.2f}{}'.format(c['ver'], t / 2, c['l']))
elif o == 4:
    t = p + (p * 20 / 100)
    q = int(input('\033[34mQuantas parcelas? \033[m'))
    print('{}Sua compra será parcelada em {}X de R${:.2f} com juros{}'.format(c['ver'], q, t / q, c['l']))
else:
    t = p
    print('\033[31mOpção de pagamento invalida. Tente novamente{}'.format(c['l']))
print('{}Sua compra de R${:.2f} vai custar R${:.2f} no final.{}'.format(c['ver'], p, t, c['l']))
