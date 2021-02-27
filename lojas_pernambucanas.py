print('=========>LOJAS PERNAMBUCANAS<=========\n')
valor = float(input('Digite o valor da compra: R$'))
pagamento = [1, 2, 3]
forma = 0
while forma not in pagamento:
    print('Formas de pagamento:')
    print('[ 1 ] à vista no DINHEIRO')
    print('[ 2 ] à vista no CARTÃO')
    print('[ 3 ] parcelado no CARTÃO')
    forma = int(input(''))
    if forma not in pagamento:
        print('Este numero é invalido!')
if forma == 1:
    print('Você deve pagar R${}' .format(valor))
elif forma == 2:
    print('Você deve pagar R${} na compra com o cartão' .format(valor + (valor*0.10)))
else:
    parcelas = int(input('Digite a quantidade de parcelas: '))
    valor_final = (((valor / parcelas) + (valor / parcelas) * 0.2) * parcelas)
    print('Você deve pagar R${} na compra no cartão parcelada em {} veses devido aos juros de 2 por cento ao mes' .format(
        valor_final, parcelas))
