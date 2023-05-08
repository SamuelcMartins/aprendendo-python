maiores_de18 = homem = mulher_menor20 = 0
while True:
    print(f'''{'=' * 25}
    {"CADASTRE UMA PESSOA" :^25}
    {'=' * 25}''')
    sexo = ' '
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = input('Sexo : [M/F] ').upper().strip()
    print('=' * 25)
    if idade > 18:
        maiores_de18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher_menor20 += 1
    continuar =' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').upper().strip()
    if continuar == 'N':
        break
print(f'''Total de pessoas com mais de 18 anos: {maiores_de18}
Ao todo temos {homem} homens cadastrados
E temos {mulher_menor20} mulheres com menos de 20 anos''')
