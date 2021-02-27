peso = float(input('Digite o seu peso: '))
altura = int(input('Digite sua altura em cm: '))

imc = peso/((altura/100)**2)
if imc < 16:
    print('O seu IMC é {:.2F} e você tem SUBPESO SEVERO' .format(imc))
elif imc < 20:
    print('O seu IMC é {:.2F} e você tem SUBPESO' .format(imc))
elif imc < 25:
    print('O seu IMC é {:.2F} e você tem um IMC NORMAL' .format(imc))
elif imc < 30:
    print('O seu IMC é {:.2F} e você tem SOBREPESO' .format(imc))
elif imc < 40:
    print('O seu IMC é {:.2F} e você tem OBESIDADE' .format(imc))
else:
    print('O seu IMC é {:.2F} e você tem OBESIDADE MORBIDA' .format(imc))
