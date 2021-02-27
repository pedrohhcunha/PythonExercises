nome = str(input('Digite seu nome completo: ')).strip()

nome_upper = nome.upper()
nome_lower = nome.lower()
nome_letras = len(nome) - nome.count(' ')
dividido = nome.split()
nome1_letras = len(dividido[0])


print('O seu nome com todas as letras maiuscula é:')
print(nome_upper)
print('O seu nome com todas as letras minusculas é:')
print(nome_lower)
print('A quantidade de letras no seu nome é:')
print(nome_letras)
print('A quantidade de letras no seu primeiro nome é:')
print(nome1_letras)
