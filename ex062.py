print('Gerador de PA\n', '-=' * 10)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro_termo
count = 0
termos_adicionais = 10
while count < termos_adicionais:
    print('{} → '.format(termo), end= '')
    termo += razao
    count += 1
    if count == termos_adicionais:
        qta = int(input('Pausa\nQuantos termos você quer mostrar a mais? '))
        termos_adicionais += qta
print('Progressão finalizada com {} termos mostrados.'.format(count))
