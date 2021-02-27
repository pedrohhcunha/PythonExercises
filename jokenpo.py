from random import randint
import time

escolha = 0
opcoes = [1, 2, 3]
escolha_pc = int(randint(1, 3))

while escolha not in opcoes:
    print('Suas opções: ')
    print('[ 1 ] para PEDRA')
    print('[ 2 ] PARA PAPEL')
    print('[ 3 ] para TESOURA')
    escolha = int(input(''))
    if escolha not in opcoes:
        print('Este numero é invalido!')
print('\n\n\n\n\n\n\n\n\n\n')
time.sleep(1)
print('JO!\n\n')
time.sleep(1)
print('KEN!\n\n')
time.sleep(1)
print('PO!\n\n')
time.sleep(1)
print('\n\n\n\n')

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
if escolha == 1 and escolha_pc == 1:
    print('Você escolheu PEDRA')
    print('O computador escolheu PEDRA')
    print('O JOGO EMPATOU!')
elif escolha == 1 and escolha_pc == 2:
    print('Você escolheu PEDRA')
    print('O computador escolheu PAPEL')
    print('O COMPUTA DOR VENCEU!')
elif escolha == 1 and escolha_pc == 3:
    print('Você escolheu PEDRA')
    print('O computador escolheu TESOURA')
    print('PARABENS, VOCÊ VENCEU!')
elif escolha == 2 and escolha_pc == 1:
    print('Você escolheu PAPEL')
    print('O computador escolheu PEDRA')
    print('PARABENS, VOCÊ VENCEU!')
elif escolha == 2 and escolha_pc == 2:
    print('Você escolheu PAPEL')
    print('O computador escolheu PAPEL')
    print('O JOGO EMPATOU!')
elif escolha == 2 and escolha_pc == 3:
    print('Você escolheu PAPEL')
    print('O computador escolheu TESOURA')
    print('O COMPUTADOR VENCEU!')
elif escolha == 3 and escolha_pc == 1:
    print('Você escolheu TESOURA')
    print('O computador escolheu PEDRA')
    print('O COMPUTADOR VENCEU!')
elif escolha == 3 and escolha_pc == 2:
    print('Você escolheu TESOURA')
    print('O computador escolheu PAPEL')
    print('PARABENS, VOCÊ VENCEU!')
elif escolha == 3 and escolha_pc == 3:
    print('Você escolheu TESOURA')
    print('O computador escolheu TESOURA')
    print('O JOGO EMPATOU')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('\n\n')
