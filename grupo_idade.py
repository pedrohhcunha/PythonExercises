from datetime import datetime
ano = datetime.today().year
cont_menor = 0
cont_maior = 0
ano_nasc = 0
for c in range(0, 7):
    ano_nasc = int(
        input('Digite o ano de nasimneto da {} pessoa: ' .format(c+1)))
    if (ano - ano_nasc) < 18:
        cont_menor += 1
    else:
        cont_maior += 1
print('Dentre as datas de nascimento informadas,\n {}pessoas são adultas\n e a(s) {} restante(s) não são!' .format(
    cont_maior, cont_menor))
