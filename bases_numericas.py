num = int(input('Digite um numero: '))

print('Escolha a base numerica em que você deseja transformar o numero informado!')
print('Para BINARIO  digite 1')
print('Para HEXADECIMAL  digite 2')
print('Para OCTAL  digite 3')
print('Para BINARIO, HEXADECIMAL e OCTAL digite 4')
bs = int(input(''))
op = [1, 2, 3, 4]
if bs not in op:
    print('Este numero é invalido!')
elif bs == 1:
    print('O numero escolhido em binario é: {}' .format(bin(num)))
elif bs == 2:
    print('O numero escolhido em hexadecimal é: {}' .format(hex(num)))
elif bs == 3:
    print('O numero escolhido em octadecimal é: {}' .format(oct(num)))
else:
    print('O numero escolhido em binario é: {}' .format(bin(num)))
    print('O numero escolhido em hexadecimal é: {}' .format(hex(num)))
    print('O numero escolhido em octadecimal é: {}' .format(oct(num)))

