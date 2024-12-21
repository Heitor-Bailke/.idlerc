def digite_nota(atividade, notaminima, notamaxima):
    while True:
        try:
            nota = float(input(f'Digite a {atividade} ({notaminima}-{notamaxima}): '))
            if notaminima <= nota <= notamaxima:
                return nota
            else:
                print(f'Valor da nota incorreto. Preencha com uma nota entre {notaminima} e {notamaxima}')
        except ValueError:
            print('Dados incorretos. Coloque um valor numérico válido.')

def classificar_aluno(sm, md):
    if sm < 3:
        return 'Aluno Reprovado sem Direito a Recuperação'
    elif sm >= 7:
        return 'Aluno Aprovado'
    else:
        return 'Aluno de Recuperação'

def main():
    total_al = 3
    aprovados = 0
    reprovados = 0

    for i in range(1, total_al + 1):
        print(f'\nAluno {i}:')

        aop1 = digite_nota('Nota da AOP1', 0, 1)
        aop2 = digite_nota('Nota da AOP2', 0, 2)
        aop3 = digite_nota('Nota da AOP3', 0, 1)
        prova_regular = digite_nota('Nota da Prova Regular', 0, 6)

        sm = aop1 + aop2 + aop3 + prova_regular
        md = sm / 2

        classificacao = classificar_aluno(sm, md)
        print(f'Nota:{sm: .2f}')
        print(f'Status do Aluno: {classificacao}')

        if classificacao == 'Aluno de Recuperação':
            prova_rec = digite_nota('Nota da Prova de Recuperação', 0, 10)

            md = (sm + prova_rec) / 2

            if md >= 7:
                classificacao = 'Aluno Aprovado'
            elif md >= 5:
                classificacao = 'Aluno Aprovado'
            else:
                classificacao = 'Aluno Reprovado'

            if 'Aluno de Recuperação' == 'Aluno Aprovado' or 'Aluno Reprovado':
              print(f'Nota Final: {md}')
              print(f'Status do Aluno: {classificacao}')

        if classificacao == 'Aluno Aprovado':
            aprovados += 1
        elif classificacao == 'Aluno Reprovado sem Direito a Recuperação' or classificacao == 'Aluno Reprovado':
            reprovados += 1

    valor_da_porcentagem_de_aprovados = (aprovados / total_al) * 100
    valor_da_porcentagem_de_reprovados = (reprovados / total_al) * 100

    print(f'\nAlunos Aprovados:{aprovados}')
    print(f'Alunos Reprovados:{reprovados}')
    print(f'\nPorcentagem de Aprovados: {valor_da_porcentagem_de_aprovados:.2f}%')
    print(f'Porcentagem de Reprovados: {valor_da_porcentagem_de_reprovados:.2f}%')

if __name__ == '__main__':
    main()