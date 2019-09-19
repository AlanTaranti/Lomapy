"""
.. module:: Lojas
   :synopsis: Interage com as lojas do Lomadee.
"""

from lomapy.recursos import manipulador_requisicoes
from lomapy.recursos.rotas import rotas_loja


def obter_todas(categoria_id: int = None, possui_oferta: bool = None) -> dict:
    """
    Lista os parceiros e lojistas da Lomadee

    :param categoria_id: ID de categoria. Utilize esse parâmetro para filtrar lojas que possuem ofertas de uma determinada categoria
    :type categoria_id: int, optional

    :param possui_oferta: Quando "true" retorna apenas lojas que possuem ofertas.
    :type possui_oferta: bool, optional

    :return: Lojas
    :rtype: dict
    """
    parametros = {}

    if categoria_id is not None:
        parametros["categoryId"] = categoria_id

    if possui_oferta:
        parametros["hasOffer"] = possui_oferta

    endpoint = rotas_loja.OBTER_TODAS

    return manipulador_requisicoes.get(endpoint, parametros)
