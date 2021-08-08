def notas(*n, situação=False):
    '''
    -> Mostras a situação das notas
    :param n: as notas respectivas do aluno
    :param situação: opcional -> Bom, razoável, ruim
    :return: dicionário com informações sobre a turma
    '''
    k = dict()
    k['Total'] = len(n)
    k['Maior'] = max(n)
    k['Menor'] = min(n)
    k['Média'] = sum(n) / len(n)
    if situação:
        if k['Média'] >= 7:
            k['Situação'] = 'BOA'
        elif k['Média'] >= 5:
            k['Situação'] = 'RAZOÁVEL'
        else:
            k['Situação'] = 'RUIM'
    return k


# Programa Principal
resp = notas(5, 9.5, 8, 6, situação=True)
print(resp)
#help(notas)