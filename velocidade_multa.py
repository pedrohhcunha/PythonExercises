velocidade = float(input('Digite a velocidade atual do seu veiculo: '))

if velocidade > 80:
    print('Você está acima da velocidade maxima permitida!')
    print('Devido a velocidade de {}Km/h você deve pagar uma multa de R${}!' .format(velocidade, (velocidade-80)*7))
else:
    print('Tudo certo!')
