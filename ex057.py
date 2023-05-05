c = {'a': '\033[34m', 'l': '\033[m'}
sexo = input('Informe seu sexo: [M/F] ').strip().upper()[0]
while not sexo in 'MF':
    sexo = input('Dados inválidos. Por favor, informe o seu sexo: ').strip().upper()[0]
print('Sexo {}{}{} registrado com sucesso'.format(c['a'], sexo, c['l']))
