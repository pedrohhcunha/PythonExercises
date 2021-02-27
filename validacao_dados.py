sexo = str(input('Sexo [M/F]: ')).lower().strip()[0]
while sexo not in 'mf':
    sexo = str(input('Dados invalidos!Sexo [M/F]: ')).lower().strip()[0]
print('Dados registrados com sucesso!')
