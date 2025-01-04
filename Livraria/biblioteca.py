import json
from .livro import Livro
from .usuario import Usuario

class Biblioteca:
    def __init__(self):
        self.__livros = []
        self.__usuarios = []

    def adicionar_livro(self, livro):
        self.__livros.append(livro)

    def adicionar_usuario(self, usuario): #verificaçao de id, false = ja registrado, true = sera registrado
        for u in self.__usuarios:
            if u.to_dict()["usuario_id"].lower() == usuario.to_dict()["usuario_id"].lower():
                return False  
        
        self.__usuarios.append(usuario)
        print(f"Usuário '{usuario.to_dict()['nome']}' (ID: {usuario.to_dict()['usuario_id']}) adicionado com sucesso!")
        return True

    def listar_livros(self):
        return "\n".join([livro.get_info() for livro in self.__livros])

    def listar_usuarios(self):
        return "\n".join([usuario.get_info() for usuario in self.__usuarios])

    def salvar_dados(self, arquivo): #trabalha junto com o adicionar_usuario
        dados = {
            "livros": [livro.to_dict() for livro in self.__livros],
            "usuarios": [usuario.to_dict() for usuario in self.__usuarios],
        }
        with open(arquivo, "w") as f:
            json.dump(dados, f, indent=4)
        print("Dados salvos com sucesso!")

    def carregar_dados(self, arquivo):
        try:
            with open(arquivo, "r") as f:
                dados = json.load(f)
                self.__livros = [Livro.from_dict(livro) for livro in dados["livros"]]
                self.__usuarios = [Usuario.from_dict(usuario) for usuario in dados["usuarios"]]
        except FileNotFoundError:
            print("Arquivo não encontrado, iniciando com dados vazios.")

    def emprestar_livro(self, usuario_id, livro_id):
        usuario_id = usuario_id.lower()
        livro_id = livro_id.lower()
    
        usuario = next((u for u in self.__usuarios if u.to_dict()["usuario_id"].lower() == usuario_id), None)
        livro = next((l for l in self.__livros if l.to_dict()["livro_id"].lower() == livro_id), None)
        if usuario and livro and livro.emprestar():
            usuario.emprestar_livro(livro)
            print("\n" * 20)
            print(f"Livro '{livro.to_dict()['titulo']}' emprestado para {usuario.to_dict()['nome']}.")
        else:
            print("\n" * 20)
            print("Empréstimo não realizado. Verifique os dados.")

    def devolver_livro(self, usuario_id, livro_id):
        usuario_id = usuario_id.lower()
        livro_id = livro_id.lower()

        usuario = next((u for u in self.__usuarios if u.to_dict()["usuario_id"].lower() == usuario_id), None)
        livro = next((l for l in self.__livros if l.to_dict()["livro_id"].lower() == livro_id), None)

        if usuario and livro:
            if usuario.devolver_livro(livro):
                livro.devolver()  #atualiza o status do livro pra disponivel
                print("\n" * 20)
                print(f"Livro '{livro.to_dict()['titulo']}' devolvido com sucesso.")
                return
        print("\n" * 20)
        print("Devolução não realizada. Verifique os dados.")

    def verificar_disponibilidade(self, livro_id): #verificador de disponibilidade
        livro_id = livro_id.lower()

        livro_na_biblioteca = next((l for l in self.__livros if l.to_dict()["livro_id"].lower() == livro_id), None)

        livro_com_usuario = any(
            livro_id in [livro["livro_id"].lower() for usuario in self.__usuarios for livro in usuario.to_dict()["livros_emprestados"]]
        )

        if livro_com_usuario and livro_na_biblioteca:
            return False  #false = emprestado
        elif livro_na_biblioteca:
            return True  #true = disponivel
        return None  #se bugar bugou