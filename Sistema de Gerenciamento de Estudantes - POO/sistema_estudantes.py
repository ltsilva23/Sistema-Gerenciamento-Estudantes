# Definindo a classe Estudante
class Estudante:
    def __init__(self, nome, idade, nota):
        self.nome = nome  
        self.idade = idade  
        self.nota = nota  
    
    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome
    
    def get_idade(self):
        return self.idade
    
    def set_idade(self, idade):
        self.idade = idade
    
    def get_nota(self):
        return self.nota
    
    def set_nota(self, nota):
        self.nota = nota

def menu():
    estudantes = []  # Lista para armazenar os objetos Estudante
    
    while True:
        print("\n====== Sistema de Gerenciamento de Estudantes ======\n" +
              "1 - Adicionar um novo estudante\n" +
              "2 - Atualizar a nota de um estudante existente\n" +
              "3 - Visualizar informações de um estudante\n" +
              "4 - Listar todos os estudantes\n" +
              "5 - Sair\n")
        
        escolha = input("Escolha uma opção: ").strip()  # Recebe a opção do usuário
        
        if escolha == '1':
            # Adicionar um novo estudante
            nome = input("Digite o nome do estudante: ").strip()
            if not nome:
                print("Nome inválido. Tente novamente.")
                continue
            
            nome = nome[0].upper() + nome[1:].lower()  # Formata o nome
            
            try:
                idade = int(input("Digite a idade do estudante: ").strip())
            except ValueError:
                print("Idade inválida. Tente novamente.")
                continue
            
            while True:
                try:
                    nota = float(input("Digite a nota do estudante (0 a 10): ").strip())
                    if 0 <= nota <= 10:
                        break
                    else:
                        print("Nota inválida. A nota deve estar entre 0 e 10.")
                except ValueError:
                    print("Nota inválida. Tente novamente.")

            if nome in [estudante.get_nome() for estudante in estudantes]:
                print(f"\nEstudante {nome} já existe na lista. Tente novamente.")
                continue
            
            novo_estudante = Estudante(nome, idade, nota)
            estudantes.append(novo_estudante)
            print(f"\nEstudante {nome} adicionado com sucesso.")
        
        elif escolha == "2":
            # Atualizar a nota de um estudante existente
            nome = input("Digite o nome do estudante para atualizar a nota: ").strip()
            encontrados = [estudante for estudante in estudantes if nome.lower() in estudante.get_nome().lower()]
            
            if encontrados:
                print("\nEstudantes encontrados:")
                for i, estudante in enumerate(encontrados, 1):
                    print(f"{i}. Nome: {estudante.get_nome()}, Idade: {estudante.get_idade()}, Nota: {estudante.get_nota()}")
                
                try:
                    escolha_estudante = int(input("Digite o número do estudante cuja nota deseja atualizar: ").strip())
                    if 1 <= escolha_estudante <= len(encontrados):
                        estudante_selecionado = encontrados[escolha_estudante - 1]
                        while True:
                            try:
                                nova_nota = float(input("Digite a nova nota (0 a 10): ").strip())
                                if 0 <= nova_nota <= 10:
                                    break
                                else:
                                    print("Nota inválida. A nota deve estar entre 0 e 10.")
                            except ValueError:
                                print("Nota inválida. Tente novamente.")
                        estudante_selecionado.set_nota(nova_nota)
                        print("Nota atualizada com sucesso.")
                    else:
                        print("Número inválido. Tente novamente.")
                except ValueError:
                    print("Entrada inválida. Digite um número.")
            else:
                print("Nenhum estudante encontrado com esse nome.")
        
        elif escolha == "3":
            # Visualizar informações de um estudante
            nome = input("Digite o nome do estudante para visualizar as informações: ").strip()
            encontrados = [estudante for estudante in estudantes if nome.lower() in estudante.get_nome().lower()]
            
            if encontrados:
                print("\nEstudantes encontrados:")
                for i, estudante in enumerate(encontrados, 1):
                    print(f"{i}. Nome: {estudante.get_nome()}")
                
                try:
                    escolha_estudante = int(input("Digite o número do estudante cujas informações deseja visualizar: ").strip())
                    if 1 <= escolha_estudante <= len(encontrados):
                        estudante_selecionado = encontrados[escolha_estudante - 1]
                        print(f"\nNome: {estudante_selecionado.get_nome()}\nIdade: {estudante_selecionado.get_idade()}\nNota: {estudante_selecionado.get_nota()}")
                    else:
                        print("Número inválido. Tente novamente.")
                except ValueError:
                    print("Entrada inválida. Digite um número.")
            else:
                print("Nenhum estudante encontrado com esse nome.")
        
        elif escolha == "4":
            # Listar todos os estudantes
            if estudantes:
                print("\nTodos os estudantes cadastrados:")
                for estudante in estudantes:
                    print(f"\nNome: {estudante.get_nome()}\nIdade: {estudante.get_idade()}\nNota: {estudante.get_nota()}")
            else:
                print("Nenhum estudante cadastrado.")
        
        elif escolha == "5":
            # Sair do programa
            print("Saindo...")
            break
        
        else:
            # Se a opção escolhida não for válida
            print("Opção inválida. Tente novamente.")

# Chama a função menu para iniciar o programa
menu()
