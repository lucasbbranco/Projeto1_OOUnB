from Livraria.biblioteca import Biblioteca
from Livraria.livro import Livro
from Livraria.usuario import Usuario

#menu
def menu():
    biblioteca = Biblioteca()
    biblioteca.carregar_dados("bancoLivros.json")

    while True:
        print("\n\nSistema de Gerenciamento de Biblioteca")
        print("1. Adicionar Livro")
        print("2. Adicionar Usuário")
        print("3. Listar Livros")
        print("4. Listar Usuários")
        print("5. Emprestar Livro")
        print("6. Devolver Livro")
        print("7. Salvar e Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n" * 20)
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = input("Ano: ")
            livro_id = input("ID do Livro: ")
            biblioteca.adicionar_livro(Livro(titulo, autor, ano, livro_id))
            print("Livro adicionado com sucesso!")

        elif opcao == "2":
            print("\n" * 20)
            nome = input("Nome do Usuário: ")
            usuario_id = input("ID do Usuário: ")
            novo_usuario = Usuario(nome, usuario_id)
            if biblioteca.adicionar_usuario(novo_usuario):  # Verifica se o ID é único antes de adicionar
                print(f"Usuário {nome} adicionado com sucesso!")
            else:
                print("Falha ao adicionar usuário. ID já existe.")


        elif opcao == "3":
            print("\n" * 20)
            print("\nLista de Livros:")
            print(biblioteca.listar_livros())

        elif opcao == "4":
            print("\n" * 20)
            print("\nLista de Usuários:")
            print(biblioteca.listar_usuarios())

        elif opcao == "5":
            print("\n" * 20)
            usuario_id = input("ID do Usuário: ")
            livro_id = input("ID do Livro: ")
            biblioteca.emprestar_livro(usuario_id, livro_id)

        elif opcao == "6":
            print("\n" * 20)
            usuario_id = input("ID do Usuário: ")
            livro_id = input("ID do Livro: ")
            biblioteca.devolver_livro(usuario_id, livro_id)

        elif opcao == "7":
            print("\n" * 20)
            biblioteca.salvar_dados("bancoLivros.json")
            print("Dados salvos! Saindo do sistema...")
            break

        else:
            print("Opção inválida, tente novamente.")


#executar
if __name__ == "__main__":
    menu()
