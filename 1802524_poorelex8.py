# Carlos Henrique Durante da Silva
# (11)96340-9937
# carlos.durante@outlook.com
# https://linkedin.com/in/carloshdurante
# Programação Orientada a Objetos


class Exame:
    def __init__(self, medico, paciente, descricao, resultado):
        self.medico = medico
        self.paciente = paciente
        self.descricao = descricao
        self.resultado = resultado

    def imprimir_exame(self):
        print('====DADOS DO MÉDICO===')
        print('Nome:', medico.nome)
        print('CRM:', medico.crm)
        print('Especialização:', medico.especializcao)
        print('====DADOS DO PACIENTE===')
        print('Nome:', paciente.nome)
        print('CPF:', paciente.cpf)
        print('Idade:', paciente.idade)
        print('====DADOS DO EXAME===')
        print('Médico solicitante:', exame01.medico.nome)
        print('Nome do paciente:', exame01.paciente.nome)
        print('Tipo de teste realiazo:', exame01.descricao)
        print('Resultado:', exame01.resultado)


class Paciente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade


class Medico:
    def __init__(self, nome, crm, especializacao):
        self.nome = nome
        self.crm = crm
        self.especializcao = especializacao


paciente = Paciente('Marcelo Silva', '033444555-22', 26)
medico = Medico('Ana Beatriz', 333431, 'Clínico Geral')
exame01 = Exame(medico, paciente, 'COVID-19', 'Negativo')
exame01.imprimir_exame()
# Deve exibir relatório com todos os dados do exame
# (inclusive os dados do médico e paciente)
