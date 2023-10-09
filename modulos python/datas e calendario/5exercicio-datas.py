# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcelas

from datetime import datetime
from dateutil.relativedelta import relativedelta


valor_emprestimo = 1_000_000
data_emprestimo = datetime.strptime('20/12/2020', '%d/%m/%Y')
parcelas_ano = relativedelta(years=5)
data_final = data_emprestimo + parcelas_ano

parcelas = []
data_parcela = data_emprestimo

while data_parcela < data_final:
    parcelas.append(data_parcela)
    data_parcela += relativedelta(months=1)

nmr_parcelas = len(parcelas)
valor_parcelas = valor_emprestimo / nmr_parcelas

for data in parcelas:
    print(data.strftime('%d/%m/%Y'), f'R$= {valor_parcelas:,.2f}')
