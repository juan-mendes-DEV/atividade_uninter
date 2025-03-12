
# lista dos livros que serão cadastrados pelo cliente
lista_livro = []
id_global = 0

# funcao de cadastrar livros
def cadastrar_livro(id):

    nome = input("qual o nome do livro? ")
    autor = input("qual o autor do livro? ")
    editora = input("qual a editora do livro? ")
    # adicionando dados ao dicionario
    dados_livro = {"id": id, "nome":nome, "autor":autor, "editora":editora}    
    # adicionando dicionario a lista
    lista_livro.append(dados_livro)

    print("livro cadastrado com sucesso")

# funcao de consulta de livros por id e por autor e todos duma vez
def consultar_livro():
    while True:
        print("o que deseja consultar? ")
        escolha = input("(1. Consultar Todos \n/ 2. Consultar por Id \n/ 3. Consultar por Autor \n/ 4. Retornar ao menu)\n")

        if escolha == "1":
            print("lista de todos livros cadastrados")
            if not lista_livro:
                print("nenhum livro cadastrado")
            else: 
                # loop para listar todos livros :< usado para colocar espaços muito pratico 
                print(f"{'ID':<5} {'Nome':<20} {'Autor':<15} {'Editora':<15}")
                for livro in lista_livro:
                    print("---------------------------------------------------------")
                    print(f"{livro['id']:<5} {livro['nome']:<20} {livro['autor']:<15} {livro['editora']:<15}")
                    print("----------------------------------------------------------")
        elif escolha == "2":
            while True:
                try:
                    id_de_busca = int(input("Digite o ID para pesquisa: "))
                    break  # Sai do loop se a conversão for bem-sucedida
                except ValueError:
                    print("ID inválido. Por favor, insira um número inteiro válido.")

            encontrado = False
            for livro in lista_livro:
                if livro["id"] == id_de_busca:
                        print("\nLivro encontrado:")
                        print(f"{'ID':<5} {'Nome':<20} {'Autor':<15} {'Editora':<15}")
                        print("---------------------------------------------------------")
                        print(f"{livro['id']:<5} {livro['nome']:<20} {livro['autor']:<15} {livro['editora']:<15}")
                        print("----------------------------------------------------------")
                        encontrado = True
                        break

                else:
                    print("livro nao encontrado")
            if not encontrado:
                print("Livro com ID informado não encontrado.")

        elif escolha == "3":
            buscar_autor = input("digite o nome do autor para buscar: ")
            
            # ! IMPORTANTE esta linha de código abaixo cria uma nova lista, chamada encontrados, 
            # contendo todos os livros da lista_livro onde o autor do livro 
            # é igual ao autor fornecido em buscar_autor, ignorando diferenças de maiúsculas e minúsculas 
            
            encontrados = [livro for livro in lista_livro if livro["autor"].lower() == buscar_autor.lower()]
            if encontrados:
                print("\nLivros encontrados:")
                
                for livro in encontrados:
                    print(f"{'ID':<5} {'Nome':<20} {'Autor':<15} {'Editora':<15}")
                    print("---------------------------------------------------------")
                    print(f"{livro['id']:<5} {livro['nome']:<20} {livro['autor']:<15} {livro['editora']:<15}")
                    print("----------------------------------------------------------")
            else:
                print("Nenhum livro encontrado para esse autor.")

        elif escolha == "4":
            break
        else:
            print("opção invalida")

# funcao de remover livros pelo id
def remover_livro():
    # loop
    while True:
        # confirmação de remoção
        certeza = input("deseja remover livro? [S] para sim , [N] para não?").upper()
        if certeza == "S":
            opcao = int(input("qual livro deseja remover pelo id? "))
            encontrado = False
            # obtendo livro pra remoçaõ
            for livro in lista_livro:
                if livro["id"] == opcao:
                    lista_livro.remove(livro)
                    print(f"Livro com ID {opcao} removido com sucesso.")
                    encontrado = True
                    break
                else:
                    print("livro não encontrado")
        else:
            print("saindo...")
            break
# função principal
def main():
    global id_global
    print("para continuar digite seu nome e sobrenome")
    # obtendo nomes
    nome = input("digite seu nome: ")
    sobrenome = input("digite seu sobrenome: ")

    print(f"ola {nome} {sobrenome} seja bem vindo a meu sistema de cadastro de livros ;D\n\n")
    print("---------------------Menu----------------------------")
    while True:
        print("\nMenu Principal:\n")
        print("1. Cadastrar Livro")
        print("2. Consultar Livro")
        print("3. Remover Livro")
        print("4. Encerrar Programa")
        print("-----------------------------------------------------")

        escolha = input("Escolha uma opção: ")
        # menu de escolha
        if escolha == '1':
            cadastrar_livro(id_global)  # Passa o ID para a função
            id_global += 1  # Incrementa o ID somente após o cadastro do livro
        elif escolha == '2':
            consultar_livro()
        elif escolha == '3':
            remover_livro()
        elif escolha == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# chamada da função principal
main()