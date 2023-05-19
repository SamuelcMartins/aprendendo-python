while True:
    try:
        num = int(input('Digite um número entre 0 e 20: '))
        break
    except ValueError:
        print('Valor inválido, por favor digite um número inteiro')
if num > 20:
    num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
if num < 0:
    num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
extenso = ('zero', 'um' , 'dois', 'três', 'quatro',
           'cinco','seis', 'sete', 'oito', 'nove',
           'dez','onze', 'douze', 'treze', 'quatorze',
           'quinze','dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
print(f'Você digitou o número {extenso[num]}')