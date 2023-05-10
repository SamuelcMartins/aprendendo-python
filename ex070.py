print(f'''{'-' * 35}
{ "LOJA SUPER BARATÃO" :^35}
{'-' * 35}''')
tot = mais1000 =0
mais_barato = {"nome": "", "preço": float('inf')}
while True:
    produto = input('Nome do produto: ')
    preço = float(input('Preço: R$ '))
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').upper().strip()
    tot += preço
    if preço > 1000:
        mais1000 += 1
    if mais_barato["preço"] > preço:
        mais_barato["nome"] = produto
        mais_barato["preço"] = preço
    if continuar == 'N':
        break
print(f'''O total da compra foi R${tot:.2f}
Temos {mais1000} produtos custando mais de R$1000.00
O produto mais barato foi {mais_barato['nome']} que custa R${mais_barato['preço']:.2f}''')
