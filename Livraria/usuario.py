from .livro import Livro


class Usuario:
    def __init__(self, nome, usuario_id):
        self.__nome = nome
        self.__usuario_id = usuario_id
        self.__livros_emprestados = []

    def emprestar_livro(self, livro):
        self.__livros_emprestados.append(livro)

    def devolver_livro(self, livro):
        for l in self.__livros_emprestados:
            if l.to_dict()["livro_id"] == livro.to_dict()["livro_id"]:
                self.__livros_emprestados.remove(l)
                return True
        return False

    def get_info(self):
        livros = [
            f"{livro.to_dict()['titulo']} de {livro.to_dict()['autor']} ({livro.to_dict()['ano']}) - ID: {livro.to_dict()['livro_id']}"
            for livro in self.__livros_emprestados
    ]
        info = f"\n{self.__nome} (ID: {self.__usuario_id})"
        if livros:
            info += "\n-" + "\n-".join(livros)
        else:
            info += ""
        return info

    def to_dict(self):
        return {
            "nome": self.__nome,
            "usuario_id": self.__usuario_id,
            "livros_emprestados": [livro.to_dict() for livro in self.__livros_emprestados],
        }

    @classmethod
    def from_dict(cls, data):
        usuario = cls(data["nome"], data["usuario_id"])
        usuario.__livros_emprestados = [Livro.from_dict(livro) for livro in data["livros_emprestados"]]
        return usuario