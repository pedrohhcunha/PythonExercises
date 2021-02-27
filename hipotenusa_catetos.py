import math

ca = float(input('Informe a medida em cm do cateto adjacente: '))

co = float(input('Informe a medida em cm do cateto oposto: '))

h = math.sqrt(math.exp(ca) + math.exp(co))

print('A hipotenusa de um triangulo retângulo onde o CA vale {} e o CO vale {} é igual a {:.2f}' .format(ca, co, h))
