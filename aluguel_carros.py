dias = int(input('Digite a quantidades de dias que você alugou o carro: '))

km = float(input('Digite a quantidade km rodados com o veiculo: '))

p = (dias * 60) + (km*0.15)

print('Rodando {}Km em {} dias com o veiculo alugado você deve pagar R${:.2f}' .format(dias, km, p))
