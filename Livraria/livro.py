class Livro:
    def __init__(self, titulo, autor, ano, livro_id):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
        self.__livro_id = livro_id
        self.__disponivel = True

    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            return True
        return False

    def devolver(self):
        self.__disponivel = True

    def get_info(self):
        if self.__disponivel:
            status = "Disponível"

        else:
            status = "Emprestado"

        return f"{self.__titulo} de {self.__autor} ({self.__ano}) - ID: {self.__livro_id} - {status}"

    def to_dict(self):
        return {
            "titulo": self.__titulo,
            "autor": self.__autor,
            "ano": self.__ano,
            "livro_id": self.__livro_id,
            "disponivel": self.__disponivel,
        }

    @classmethod
    def from_dict(cls, data):
        livro = cls(data["titulo"], data["autor"], data["ano"], data["livro_id"])
        livro.__disponivel = data["disponivel"]
        return livro