nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
media= (nota1 + nota2) / 2
if media >= 7.0:
    print('Tirando {} e {}, a média do aluno é {}.\nO aluno está APROVADO'.format(nota1,nota2,media))
elif media >= 5 or m < 7:
    print('Tirando {} e {}, a média do aluno é {}.\nO aluno está de RECUPERAÇÃO'.format(nota1,nota2,media))
elif media < 5:
    print('Tirando {} e {}, a média do aluno é {}.\O aluno está REPROVADO!!!')