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
        print('Nome:', self.medico.nome)
        print('CRM:', self.medico.crm)
        print('Especialização:', self.medico.especializcao)
        print('====DADOS DO PACIENTE===')
        print('Nome:', self.paciente.nome)
        print('CPF:', self.paciente.cpf)
        print('Idade:', self.paciente.idade)
        print('====DADOS DO EXAME===')
        print('Médico solicitante:', self.medico.nome)
        print('Nome do paciente:', self.paciente.nome)
        print('Tipo de teste realiazo:', self.descricao)
        print('Resultado:', self.resultado)


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


paciente01 = Paciente('Marcelo Silva', '033444555-22', 26)
paciente02 = Paciente('Carlos Durante', '426972888-48', 26)
medico01 = Medico('Ana Beatriz', 333431, 'Clínico Geral')
medico02 = Medico('João Silva', 367439, 'Clínico Geral')
exame01 = Exame(medico01, paciente01, 'COVID-19', 'Negativo')
exame01.imprimir_exame()
exame02 = Exame(medico02, paciente02, 'COVID-19', 'Negativo')
exame02.imprimir_exame()
# Deve exibir relatório com todos os dados do exame
# (inclusive os dados do médico e paciente)
