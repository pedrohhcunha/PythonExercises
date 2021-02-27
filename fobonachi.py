print('-'*22)
print('SEQUENCIA DE FIBONACCI')
print('-'*22)
n = int(input('Quantos valores deseja calcular? '))
cont = 2
t1 = 0
t2 = 1
print('{}-> {}-> ' .format(t1, t2), end='')
while cont != n:
    t3 = t1+t2
    print(t3, end='-> ')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
