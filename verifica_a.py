frase = (str(input('Digite uma frase: '))).lower().strip()

print("a letra A está aparecendo {} veses na frase" .format(frase.count('a')))

print('A primeira letra A aparece na posição {}'.format(1+frase.find('a')))
print('A primeira letra A aparece na posição {}'.format(1+frase.rfind('a')))
