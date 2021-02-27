ano = int(input('Digite um ano: '))
if ano % 4 == 0 and ano % 100 != 0:
    print('O ano que você digitou é bissexto!')
else:
    print('O ano que você digitou não é bissexto!')
