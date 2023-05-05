p = float(input('Qual é o seu peso? (Kg) '))
a = float(input('Qual é a sua altura? (m) '))
imc = p / (a ** 2)
c = {'a' : '\033[34m', 'v' : '\033[31m', 'l' : '\033[m'}
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('{}VOCÊ ESTA ABAIXO DO PESO NORMAL{}'.format(c['v'], c['l']))
elif imc < 25:
    print('{}PARABENS! VOCÊ ESTA NA FAIXA DE PESO NORMAL{}'.format(c['a'], c['l']))
elif imc <= 40:
    print('{}VOCÊ ESTA EM OBESIDADE!{}'.format(c['v'], c['l']))
else:
    print('{}VOCÊ ESTA EM OBESIDADE MÓRBIDA, CUIDADO!{}'.format(c['v'], c['l']))
