class Categoria:
    """
    Representa uma Categoria
    """

    def __init__(self):
        self.id = None
        self.nome = None
        self.quantidade_ofertas = None
        self.link = None

    def construir(self, categoria: dict):
        """ Popula a categoria de acordo com os dados da Lomadee

        Parameters
        ----------
        categoria: dict
            Dados da Lomadee

        Returns
        -------
        None
        """
        self.id = categoria["id"]
        self.nome = categoria.get("name", None)
        self.quantidade_ofertas = categoria.get("hasOffer", None)
        self.link = categoria["link"]

    def para_dict(self) -> dict:
        """ Retorna os dados da Categoria no formato de dicionário

        Returns
        -------
        dict
            Dados no formato de dicionário
        """
        return {
            "id": self.id,
            "nome": self.nome,
            "quantidade_ofertas": self.quantidade_ofertas,
            "link": self.link
        }
