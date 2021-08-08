from datetime import date
ano = (int(input('Insira seu ano de Nascimento: ')))
data = date.today().year
idade = data - ano
alistamento = 18 - idade
ano_alistamento =alistamento + data
alist2 = idade - 18
print('Quem nasceu em {} tem {} anos em {}.'.format(ano,idade,data))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!!!')
elif idade < 18:
    print('Ainda faltam {} anos para o alistamento\nSeu alistamento será em {}.'.format(alistamento,ano_alistamento))
elif idade > 18:
    print('Você ja deveria ter se alistado há {} anos.\nSeu alistamento foi em {}'.format(alist2,ano_alistamento))