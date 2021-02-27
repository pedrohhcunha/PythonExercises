num = int(input('Digite um numero para o calculo fatorial: '))
cont = num
f = 1
while cont > 0:
    print('{}'.format(cont), end=' ')
    if cont >= 2:
        print('x ', end='')
    else:
        print('= ', end='')
    f *= cont
    cont -= 1
print(f)
