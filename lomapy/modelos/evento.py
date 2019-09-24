class Evento:
    """
    Representa um Evento
    """

    def __init__(self):
        self.comissao = None
        self.nome = None
        self.tipo = None
        self.ehComissaoFixa = None

    def construir(self, evento: dict):
        """ Popula o evento de acordo com os dados da Lomadee

        Parameters
        ----------
        evento: dict
            Dados da Lomadee

        Returns
        -------
        None
        """
        self.comissao = evento["commission"]
        self.nome = evento["event"]
        self.tipo = evento["eventType"]
        self.ehComissaoFixa = evento["fixedCommission"]

    def para_dict(self) -> dict:
        """ Retorna os dados do Evento no formato de dicionário

        Returns
        -------
        dict
            Dados no formato de dicionário
        """
        return {
            "comissao": self.comissao,
            "nome": self.nome,
            "tipo": self.tipo,
            "ehComissaoFixa": self.ehComissaoFixa
        }
