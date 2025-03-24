import re

class Funcionario:
    def __init__(self, id_funcionario, nome, cargo, salario, email, idade, cidade, estado, escolaridade):
        # Construtor que inicializa os atributos de um funcionário
        self.id_funcionario = id_funcionario
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.email = email
        self.idade = idade
        self.cidade = cidade
        self.estado = estado
        self.escolaridade = escolaridade

    def __str__(self):
        # Representação em formato de string do funcionário
        return f"ID: {self.id_funcionario}, Nome: {self.nome}, Cargo: {self.cargo}, Salário: R${self.salario:.2f}, Email: {self.email}, Idade: {self.idade}, Cidade: {self.cidade}/{self.estado}, Escolaridade: {self.escolaridade}"

# Função para validar e-mail
def validar_email(email):
    # Expressão regular para validar um e-mail simples
    padrao_email = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    
    # Checando se o e-mail segue o padrão
    if re.match(padrao_email, email):
        # Lista de domínios aceitos
        dominios_aceitos = ["gmail.com", "hotmail.com", "outlook.com", "yahoo.com", "example.com"]
        dominio = email.split('@')[1]

        if dominio in dominios_aceitos:
            return True
        else:
            print("Domínio de e-mail não aceito. Apenas e-mails de domínios aceitos são permitidos.")
            return False
    else:
        print("E-mail inválido. Por favor, insira um e-mail válido.")
        return False

class SistemaGerenciamento:
    def __init__(self):
        self.funcionarios = {}  # Dicionário para armazenar funcionários com ID como chave

    def adicionar_funcionario(self):
        # Função para adicionar um novo funcionário

        # Verifica o maior ID existente e adiciona 1
        if len(self.funcionarios) > 0:
            id_funcionario = max(self.funcionarios.keys()) + 1
        else:
            # Se não houver nenhum funcionário, o ID começa em 1
            id_funcionario = 1

        print(f"O ID do novo funcionário será: {id_funcionario}")

        nome = input("Digite o nome do funcionário: ")
        cargo = input("Digite o cargo do funcionário: ")
        salario = float(input("Digite o salário do funcionário: "))
        
        while True:
            email = input("Digite o e-mail do funcionário: ")
            if validar_email(email):
                break

        idade = int(input("Digite a idade do funcionário: "))
        cidade = input("Digite a cidade onde o funcionário reside: ")
        estado = input("Digite o estado onde o funcionário reside: ")
        escolaridade = input("Digite o nível de escolaridade do funcionário: ")

        # Criando o objeto Funcionário e armazenando no dicionário
        funcionario = Funcionario(id_funcionario, nome, cargo, salario, email, idade, cidade, estado, escolaridade)
        self.funcionarios[id_funcionario] = funcionario
        print(f"Funcionário {nome} adicionado com sucesso!")

    def atualizar_funcionario(self):
        # Função para atualizar os dados de um funcionário
        id_funcionario = input("Digite o ID do funcionário para atualizar: ")

        if id_funcionario not in self.funcionarios:
            print("Funcionário não encontrado.")
            return

        funcionario = self.funcionarios[id_funcionario]

        # Atualizando as informações do funcionário
        funcionario.nome = input(f"Digite o novo nome ({funcionario.nome}): ") or funcionario.nome
        funcionario.cargo = input(f"Digite o novo cargo ({funcionario.cargo}): ") or funcionario.cargo
        funcionario.salario = float(input(f"Digite o novo salário ({funcionario.salario}): ") or funcionario.salario)

        while True:
            email = input(f"Digite o novo e-mail ({funcionario.email}): ") or funcionario.email
            if validar_email(email):
                funcionario.email = email
                break

        funcionario.idade = int(input(f"Digite a nova idade ({funcionario.idade}): ") or funcionario.idade)
        funcionario.cidade = input(f"Digite a nova cidade ({funcionario.cidade}): ") or funcionario.cidade
        funcionario.estado = input(f"Digite o novo estado ({funcionario.estado}): ") or funcionario.estado
        funcionario.escolaridade = input(f"Digite a nova escolaridade ({funcionario.escolaridade}): ") or funcionario.escolaridade

        print(f"Funcionário {funcionario.nome} atualizado com sucesso!")

    def listar_funcionarios(self):
        # Função para listar todos os funcionários cadastrados
        if not self.funcionarios:
            print("Nenhum funcionário cadastrado.")
            return

        print("Lista de funcionários:")
        for funcionario in self.funcionarios.values():
            print(funcionario)

    def remover_funcionario(self):
        # Função para remover um funcionário
        id_funcionario = input("Digite o ID do funcionário a ser removido: ")

        if id_funcionario not in self.funcionarios:
            print("Funcionário não encontrado.")
            return

        del self.funcionarios[id_funcionario]
        print(f"Funcionário com ID {id_funcionario} removido com sucesso!")

def menu():
    sistema = SistemaGerenciamento()

    while True:
        # Exibe o menu de opções para o usuário
        print("\n===== Menu do Sistema de Gerenciamento de Funcionários =====")
        print("1. Adicionar Funcionário")
        print("2. Atualizar Funcionário")
        print("3. Listar Funcionários")
        print("4. Remover Funcionário")
        print("5. Sair")
        opcao = input("Escolha uma opção (1-5): ")

        if opcao == '1':
            sistema.adicionar_funcionario()
        elif opcao == '2':
            sistema.atualizar_funcionario()
        elif opcao == '3':
            sistema.listar_funcionarios()
        elif opcao == '4':
            sistema.remover_funcionario()
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()