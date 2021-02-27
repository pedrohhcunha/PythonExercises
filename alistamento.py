from datetime import datetime
ano = datetime.now.year()
nascimento = int(input('Digite o ano do seu nascimento: '))
if (ano - nascimento) < 18:
    print('Você deve se alistar em {} anos!' .format(18-(ano - nascimento)))
elif(ano - nascimento) > 18:
    print('O tempo de se alistar ja passou!')
else:
    print('Você deve se alistar esse ano!')
