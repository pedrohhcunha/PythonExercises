salario = float(input('Digite o seu salario: R$'))
valor_casa = float(input('Digite o valor da casa: R$'))
tempo = int(input('Digite o tempo em meses que você deseja pagar: '))

if (valor_casa/tempo) > (salario*0.3):
    print('Infelizmente o(a) senhor(a) não pode efetuar o emprestimo!')
elif (valor_casa/tempo) < (salario*0.3):
    print('O senhor(a) pode realizar o emprestimo!')
