from datetime import datetime

ano_atual = datetime.today().year
ano_nasceu = int(input('Digite o ano do seu nascimento: '))
idade = ano_atual - ano_nasceu
print('O integrante tem {} anos' .format(idade))
if idade < 14:
    print('Tem de idade de MIRIM')
elif idade < 18:
    print('Tem idade de JUVENIL')
elif idade <= 35:
    print('Tem idade de ADULTA')
else:
    print('Tem idade de VETERANO')
