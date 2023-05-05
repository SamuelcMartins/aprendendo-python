c = {'a': '\033[34m', 'l': '\033[m'}
somaidade = 0
maioridadehomem = 0
nomemaisvelho = ''
totmulher = 0
for b in range(1,5):
    print('{} {}°PESSOA {}'.format('-' * 5, b, '-' * 5))
    nome = input('nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()
    somaidade += idade
    if b == 1 and sexo in 'mM':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
print('A média de idade do grupo é de {}{}{} anos'.format(c['a'], somaidade / 4, c['l']))
print('O homem mais velho tem {}{}{} anos e se chama {}{}{}'.format(c['a'], maioridadehomem, c['l'], c['a'], nomemaisvelho, c['l']))
print('Ao todo são {}{}{} mulheres com menos de {}20{} anos'.format(c['a'], totmulher, c['l'], c['a'],c['l']))
