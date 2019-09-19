"""
.. module:: Categorias
   :synopsis: Interage com as categorias do Lomadee.
"""

from lomapy.recursos import manipulador_requisicoes
from lomapy.recursos.rotas import rotas_categoria


def buscar(palavra_chave: str, loja_id: int = None, possui_oferta: bool = None, quantidade: int = None) -> dict:
    """
    Realiza a busca de categorias através de palavras

    :param palavra_chave: Palavra-chave a ser buscada
    :type palavra_chave: str

    :param loja_id: ID de loja. Utilize esse parâmetro para filtrar categorias que possuem ofertas de uma determinada loja
    :type loja_id: int, optional

    :param possui_oferta: Quando "true" retorna apenas categorias que possuem ofertas.
    :type possui_oferta: bool, optional

    :param quantidade: Quantidade de categorias. Com este parâmetro você poderá definir o número de categorias que deseja receber. Padrão: 12
    :type quantidade: int, optional

    :return: Categorias
    :rtype: dict
    """
    parametros = {
        "keyword": palavra_chave,
    }

    if loja_id is not None:
        parametros["storeId"] = loja_id

    if possui_oferta:
        parametros["hasOffer"] = possui_oferta

    if quantidade:
        parametros["size"] = quantidade

    endpoint = rotas_categoria.BUSCAR

    return manipulador_requisicoes.get(endpoint, parametros)


def obter_todas(loja_id: int = None, possui_oferta: bool = None) -> dict:
    """
    Consulta a lista de todas as categorias que possuem ofertas dos lojistas parceiros da Lomadee.

    :param loja_id: ID de loja. Utilize esse parâmetro para filtrar categorias que possuem ofertas de uma determinada loja
    :type loja_id: int, optional

    :param possui_oferta: Quando "true" retorna apenas categorias que possuem ofertas.
    :type possui_oferta: bool, optional

    :return: Categorias
    :rtype: dict
    """
    parametros = {}

    if loja_id is not None:
        parametros["storeId"] = loja_id

    if possui_oferta:
        parametros["hasOffer"] = possui_oferta

    endpoint = rotas_categoria.OBTER_TODAS

    return manipulador_requisicoes.get(endpoint, parametros)


def obter_por_id(categoria_id: int, loja_id: int = None) -> dict:
    """
    Obtem uma categoria específica de acordo com o ID

    :param categoria_id: ID da categoria desejada
    :type categoria_id: int

    :param loja_id: ID de loja. Utilize esse parâmetro para filtrar categorias que possuem ofertas de uma determinada loja
    :type loja_id: int, optional

    :return: Categorias
    :rtype: dict
    """
    parametros = {}

    if loja_id is not None:
        parametros["storeId"] = loja_id

    endpoint = rotas_categoria.OBTER_POR_ID.format(categoria_id)

    return manipulador_requisicoes.get(endpoint, parametros)
