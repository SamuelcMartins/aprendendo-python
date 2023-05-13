print(f''''{'=' * 30}
{"BANCO CEV" :^30}
{'=' * 30}''')
saque = int(input('Que valor você quer sacar ? R$'))
if saque // 50:
    cedulas50 = saque // 50
    resto = saque % 50
    print(f'Total de {cedulas50} cédulas de R$50')
if resto // 20:
    cedulas20 = resto // 20
    resto = resto % 20
    print(f'Total de {cedulas20} cédulas de R$20')
if resto // 10:
    cedulas10 = resto// 10
    resto = resto % 10
    print(f'Total de {cedulas10} cédulas de R$10')
if resto // 1:
    cedulas1 = resto // 1
    print(f'Total de {cedulas1} cédulas de R$1')
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')