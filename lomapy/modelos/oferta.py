from .categoria import Categoria
from .loja import Loja


class Oferta:
    """
    Representa uma Oferta
    """

    def __init__(self):
        self.id = None
        self.nome = None
        self.parcelas = None  # type: dict
        self.link = None
        self.categoria = None  # type: Categoria
        self.loja = None  # type: Loja
        self.preco_atual = None
        self.preco_original = None
        self.thumbnail = None

    def construir(self, oferta: dict):
        """ Popula a oferta de acordo com os dados da Lomadee

        Parameters
        ----------
        oferta: dict
            Dados da Lomadee

        Returns
        -------
        None
        """
        self.id = oferta["id"]
        self.nome = oferta["name"]
        self.parcelas = dict()
        self.parcelas["quantidade"] = oferta["installment"].get("quantity", 1)
        self.parcelas["valor"] = oferta["installment"].get("value", oferta["price"])
        self.link = oferta["link"]
        self.preco_atual = oferta["price"]
        self.preco_original = oferta["priceFrom"]
        self.thumbnail = oferta["thumbnail"]

        categoria = Categoria()
        categoria.construir(oferta["category"])
        self.categoria = categoria

        loja = Loja()
        loja.construir(oferta["store"])
        self.loja = loja

    def para_dict(self) -> dict:
        """ Retorna os dados da Oferta no formato de dicionário

        Returns
        -------
        dict
            Dados no formato de dicionário
        """
        dados = {
            "id": self.id,
            "nome": self.nome,
            "parcelas": self.parcelas,
            "link": self.link,
            "preco_atual": self.preco_atual,
            "preco_original": self.preco_original,
            "thumbnail": self.thumbnail,
            "loja": self.loja.para_dict(),
            "categoria": self.categoria.para_dict(),
        }
        return dados
