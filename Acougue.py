print('Escolha o tipo de carne: ')  # imprime na tela
print('')  # Pula uma linha
print('Digite 1 para Filé Duplo')  # imprime na tela
print('Digite 2 para Alcatra')  # imprime na tela
print('Digite 3 para Picanha')  # imprime na tela
carne = int(input())  # atribui a variavel carne o valor do input
tiposcarne = [1, 2, 3]  # cria e atribui valor a uma variavel do tipo list
# verifica se na lista contem o int da variavel
if carne in tiposcarne:
    # pede ao usuario e armazena a quantidade de carne
    quantidade = int(input('Digite a quantidade em Kg de carne: '))
    if quantidade < 5:  # testa se a quantidade é menos que 5
        if carne == 1:
            NomeCarne = 'Filé Duplo'
            valor = 4.90
        if carne == 2:
            NomeCarne = 'Alcatra'
            valor = 5.90
        if carne == 3:
            NomeCarne = 'Picanha'
            valor = 6.90
    else:  # executa caso a quantidade seja maior de 5
        if carne == 1:
            NomeCarne = 'Filé Duplo'
            valor = 5.80
        if carne == 2:
            NomeCarne = 'Alcatra'
            valor = 6.80
        if carne == 3:
            NomeCarne = 'Picanha'
            valor = 7.80

    ValorTotal = valor * quantidade

    print('Escolha o metodo de pagamento: ')
    print('Digite 1 para dinheiro')
    print('Digite 2 para cartao fidelidade')
    pagamento = int(input())
    tipospagamento = [1, 2]
    if pagamento in tipospagamento:
        if pagamento == 2:
            desconto = 0.5
            ValorTotal = (quantidade*valor)
            ValorFinal = ValorTotal - (ValorTotal*0.05)
            print('Voce comprou ', quantidade, 'kg de ', NomeCarne)
            print('O valor total é: ', ValorTotal, 'R$')
            print('O desconto é de 5%')
            print('O Valor com desconto é: ', ValorFinal)
            print('Você pagou com o nosso cartão fidelidade')
        else:
            ValorTotal = (quantidade*valor)
            print('Voce comprou ', quantidade, 'kg de ', NomeCarne)
            print('O valor total é: ', ValorTotal, 'Kg')
            print('Você pagou com dinheiro')
    else:
        print('Este Valor é invalido!')

else:
    print('Este Valor é invalido!')
