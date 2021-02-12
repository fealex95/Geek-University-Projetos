from utils.helper import formatar_real_moeda

class Produto:
    contador: int = 1
    def __init__(self: object, nome: str, preco: float) -> None:
        self.__codigo: int = Produto.contador
        self.__nome = nome
        self.__preco = preco
        Produto.contador += 1

    @property
    def codigo(self: object) -> int:
        return self.__codigo
    
    @property
    def nome(self: object) -> str:
        return self.__nome
    
    @property
    def preco(self: object) -> float:
        return self.__preco

    def __str__(self: object) -> str:
        return f'Código: {self.codigo} \nNome: {self.nome} \nPreço: {formatar_real_moeda(self.preco)}'