from typing import List, Optional

from .evento import Evento


class Loja:
    """
    Representa uma Loja
    """

    def __init__(self):
        self.id = None
        self.nome = None
        self.quantidade_ofertas = None
        self.link = None
        self.eventos = None  # type: Optional[List[Evento]]
        self.comissao_maxima = None
        self.thumbnail = None

    def construir(self, loja: dict):
        """ Popula a loja de acordo com os dados da Lomadee

        Parameters
        ----------
        loja: dict
            Dados da Lomadee

        Returns
        -------
        None
        """
        self.id = loja["id"]
        self.nome = loja["name"]
        self.quantidade_ofertas = loja.get("hasOffer", None)
        self.link = loja["link"]
        self.comissao_maxima = loja.get("maxCommission", None)
        self.thumbnail = loja["thumbnail"]
        self.eventos = []

        if "events" in loja:
            for e in loja["events"]:
                evento = Evento()
                evento.construir(e)
                self.eventos.append(evento)

    def para_dict(self) -> dict:
        """ Retorna os dados da Loja no formato de dicionário

        Returns
        -------
        dict
            Dados no formato de dicionário
        """
        dados = {
            "id": self.id,
            "nome": self.nome,
            "quantidade_ofertas": self.quantidade_ofertas,
            "link": self.link,
            "comissao_maxima": self.comissao_maxima,
            "thumbnail": self.thumbnail,
            "eventos": []
        }

        for e in self.eventos:
            dados["eventos"].append(e.para_dict())

        return dados
