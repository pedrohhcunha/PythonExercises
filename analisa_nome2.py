frase = (str(input('Digite uma frase: '))).lower().strip()

frase = frase.split()
primeiro_nome = frase[0]
ultimo_nome = frase[-1]

print('Seu primeiro nome é: {}'.format(primeiro_nome))
print('Seu ultimo nome é: {}' .format(ultimo_nome))
