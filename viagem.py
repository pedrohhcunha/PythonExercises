distancia = float(input('Digite a distancia em Km da viagem: '))
if distancia < 200:
    print('O valor da sua viagem é de {}' .format(distancia*0.50))
else:
    print('O valor da sua viagem é de {}' .format(distancia*0.45))
