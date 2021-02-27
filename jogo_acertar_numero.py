from random import randint

numero = int(randint(1, 100))
tentativa = 0
chute = 0

print('----------INICIO DO JOGO----------\n')

while chute != numero:
    chute = int(input('Digite um número entre 1 e 100: '))
    tentativa += 1
    if chute == numero:
        print('\nParabéns VOCÊ ACERTOU!')
        print('Você realizou {} tentativas' .format(tentativa))
        print('O número é {}!' .format(chute))
    elif chute > 100 or chute < 1:
        print('Este valor é invalido!\n')
    elif chute > numero:
        print('Tente um valor menor!\n')
    else:
        print('Tente um valor maior!\n')

print('----------INICIO DO JOGO----------')

# Fazer com que o jogador determine o numero maximo de números (10, 100, 500, 1000, 10000, 1000000)

# Fazer com que o jogador não consiga tentar o mesmo número duas veses
