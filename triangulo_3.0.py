a = float(input('Digite o valor do lado A: '))
b = float(input('Digite o valor do lado B: '))
c = float(input('Digite o valor do lado C: '))

if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('Pode formar um triangulo!')
    if a != b != c != a:
        print('Esse triangulo é ESCALENO!')
    elif a == b == c:
        print('Esse triangulo é EQUILATERO!')
    else:
        print('Esse triangulo é ISOCELES!')
else:
    print('Não pode formar um triangulo!')
