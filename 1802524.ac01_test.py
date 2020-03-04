# Carlos Henrique Durante da Silva
# (11)96340-9937
# carlos.durante@outlook.com
# https://linkedin.com/in/carloshdurante
# Funções x Dicionários x Módulos

import ac01

alunos = {'pedro': [10, 9.5, 9, 5, 7],
          'ana': [4, 7, 9.5, 10, 8],
          'jose': [10, 4.5, 5, 6, 8]}


print(ac01.adicionar_aluno(alunos, 'ana', [1, 2, 3, 4, 5]))

print(ac01.remover_aluno(alunos, 'carlos'))

print(ac01.pesquisar_aluno(alunos, 'carlos'))

print(ac01.calcular_media(alunos, 'pedro'))

print(ac01.calcular_media_turma(alunos))
