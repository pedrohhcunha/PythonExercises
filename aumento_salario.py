s = float(input('Digite o valor do salario: R$'))
if s >= 1250:
    print('O salario com o aumento derá de: {}' .format(s + (s*0.10)))
else:
    print('O salario com o aumento derá de: {}' .format(s + (s*0.15)))
