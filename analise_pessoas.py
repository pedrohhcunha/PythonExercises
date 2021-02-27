from collections import Counter
lista_nomes = []
lista_idade = []
lista_sexo = []
idade_cont_menores = 0
idade_cont_maiores = 0
sexo_op = ['m', 'f']
sexo_cont_masculino = 0
sexo_cont_feminino = 0
cont_maiores_masculino = 0
cont_maiores_femininos = 0
cont_menores_masculinos = 0
cont_menores_femininos = 0
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
          'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cont_letras = Counter()
a = 0
adicionar = 's'
qtn = 0
print('-'*15, 'CADASTRAR PESSOAS', '-'*15)
while adicionar == 's':
    print('-'*15)

    nome = ((str(input('Nome: '))).strip().lower())
    cont_letras.update([nome[0]])
    lista_nomes.append(nome)
    lista_idade.append(int(input('Idade: ')))
    if lista_idade[-1] < 18:
        idade_cont_menores += 1
    else:
        idade_cont_maiores += 1
    sexo = ((str(input('Sexo[M/F}: '))).strip().lower())
    while sexo not in 'mf':
        sexo = str(input('Dados invalidos!Sexo [M/F]: ')).lower().strip()[0]
    lista_sexo.append(sexo)
    if lista_sexo[-1] == sexo_op[0]:
        sexo_cont_masculino += 1
        if lista_idade[-1] >= 18:
            cont_maiores_masculino += 1
        else:
            cont_menores_masculinos += 1
    else:
        sexo_cont_feminino += 1
        if lista_idade[-1] >= 18:
            cont_maiores_femininos += 1
        else:
            cont_menores_femininos += 1
    qtn += 1
    print('-'*15)
    adicionar = (
        (str(input('Cadastrar mais uma pesssoa? [S/N}: '))).strip().lower())
    while adicionar not in 'sn':
        adicionar = str(
            input('\033[31mDados invalidos!Sexo [M/F]: \033[m')).lower().strip()[0]

print('-'*15, 'DADOS INSIRIDOS', '-'*15)

print('Nomes: {}'.format(lista_nomes))
print('Idades: {}'.format(lista_idade))
print('Sexo: {}'.format(lista_sexo))

print('-'*15, 'ANALISE DE DADOS', '-'*15)

idade_mais_velho = max(lista_idade)
id_idade_mais_velho = lista_idade.index(idade_mais_velho)
nome_idade_mais_velho = lista_nomes[id_idade_mais_velho]
idade_mais_novo = min(lista_idade)
id_idade_mais_novo = lista_idade.index(idade_mais_novo)
nome_idade_mais_novo = lista_nomes[id_idade_mais_novo]
idade_media = (sum(lista_idade) / (len(lista_idade)))


print('A pessoa mais nova é {} e ele(a) possui {} anos'.format(
    nome_idade_mais_novo, idade_mais_novo))
print('A pessoa mais velha é {} e ele(a) possui {} anos' .format(
    nome_idade_mais_velho, idade_mais_velho))
print('A media entre as idades das {} pessoas é {:.0} anos'.format(qtn, idade_media))

print('\nO numero de maiores de idade é: {}' .format(idade_cont_maiores))
print('Sendo {} mulheres e {} homens' .format(
    cont_maiores_femininos, cont_maiores_masculino))
print('O numero de pessoa menores de idade é: {}' .format(idade_cont_menores))
print('Sendo {} mulheres e {} homens' .format(
    cont_menores_femininos, cont_menores_masculinos))

print('\nO numero de mulheres é: {}' .format(sexo_cont_feminino))
print('O numero de homens é: {}' .format(sexo_cont_masculino))

letra_mais_frequente = cont_letras.most_common(1)[0]
print('A letra {} é a que mais aparece como inicial! \nAparecendo como inicial {} veses'
      .format(letra_mais_frequente[0], letra_mais_frequente[1]))


print('-'*15, 'FIM DA ANALISE', '-'*15)
