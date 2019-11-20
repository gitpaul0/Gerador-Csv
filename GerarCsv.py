from random import randint
'''
Tabela: VENDA (quantidade de registros: entre 80 e 120 registros)
◦ número da nota fiscal
◦ codigo do brinquedo vendido
◦ data da venda (dentro do intervalo de outubro/2018 a outubro/2019)
◦ quantidade vendida
◦ código da loja onde aconteceu a venda
'''
min = 234567
meses = {
    '1': 'Janeiro',
    '2': 'Fevereiro',
    '3': 'Março',
    '4': 'Abril',
    '5': 'Maio',
    '6': 'Junho',
    '7': 'Julho',
    '8': 'Agosto',
    '9': 'Setembro',
    '10': 'Outubro',
    '11': 'Novembro',
    '12': 'Dezembro'
}
arq = open("Vendas.csv", 'w')
csv = []
cabecalho = 'nota_fiscal, cod_brinquedo, data_venda, qtd_vendida, cod_loja \n'
csv.append(cabecalho)

for i in range(0, 120):
    numero_nota_fiscal = min
    cod_brinquedo = randint(1,20)
    aux = randint(1, 12)
    if aux < 10:
        data_venda = str(randint(1, 30)) + "/" + meses[str(aux)] + "/2019"
    else:
        data_venda = str(randint(1, 30)) + "/" + meses[str(aux)] + "/2018"

    qtdVendida = randint(1, 10)
    cod_loja = randint(1, 6)
    min += 1
    texto = str(numero_nota_fiscal) + ', ' + str(cod_brinquedo) + ', ' + str(data_venda) + ', ' + str(qtdVendida) + ', ' + str(cod_loja) + '\n'
    csv.append(texto)

arq.writelines(csv)
arq.close()