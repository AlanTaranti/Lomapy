"""
.. module:: Ofertas
   :synopsis: Interage com as ofertas do Lomadee.
"""

from lomapy.recursos import manipulador_requisicoes
from lomapy.recursos.rotas import rotas_oferta


def obter_por_categoria(categoria_id: int, loja_id: int = None, quantidade: int = None, pagina: int = None,
                        ordenacao: str = None) -> dict:
    """
    Consulta as ofertas de uma determinada categoria

    :param categoria_id: ID de categoria. Utilize esse parâmetro para filtrar ofertas de uma determinada categoria
    :type categoria_id: int

    :param loja_id: ID de loja. Utilize esse parâmetro para filtrar ofertas de uma determinada loja
    :type loja_id: int, optional

    :param quantidade: Quantidade de ofertas. Com este parâmetro você poderá definir o número de ofertas que deseja receber. Padrão: 12
    :type quantidade: int, optional

    :param pagina: Página desejada. Padrão: 1
    :type pagina: int, optional

    :param ordenacao: Ordenação dos resultados. Opções: rating (Ordena por melhor avaliação) e price (Ordena por menor preço). Padrão: rating
    :type pagina: str, optional

    :return: Ofertas
    :rtype: dict
    """
    parametros = {}

    if loja_id is not None:
        parametros["storeId"] = loja_id

    if quantidade:
        parametros["size"] = quantidade

    if pagina:
        parametros["page"] = pagina

    if ordenacao:
        parametros["sort"] = ordenacao

    endpoint = rotas_oferta.OBTER_POR_CATEGORIA.format(categoria_id)

    return manipulador_requisicoes.get(endpoint, parametros)


def obter_por_id(oferta_id: int, loja_id: int) -> dict:
    """
    Consulta uma oferta específica

    :param oferta_id: ID da oferta desejada
    :type oferta_id: int

    :param loja_id: ID de loja. Utilize esse parâmetro para filtrar ofertas de uma determinada loja
    :type loja_id: int

    :return: Ofertas
    :rtype: dict
    """
    parametros = {}

    if loja_id is not None:
        parametros["storeId"] = loja_id

    endpoint = rotas_oferta.OBTER_POR_ID.format(oferta_id)

    return manipulador_requisicoes.get(endpoint, parametros)


def buscar(palavra_chave: str, categoria_id: int = None, loja_id: int = None, quantidade: int = None,
           pagina: int = None, ordenacao: str = None) -> dict:
    """
    Consulta as ofertas de uma determinada palavra-chave

    :param palavra_chave: Palavra-chave a ser buscada
    :type palavra_chave: str

    :param categoria_id: ID de categoria. Utilize esse parâmetro para filtrar ofertas de uma determinada categoria
    :type categoria_id: int, optional

    :param loja_id: ID de loja. Utilize esse parâmetro para filtrar ofertas de uma determinada loja
    :type loja_id: int, optional

    :param quantidade: Quantidade de ofertas. Com este parâmetro você poderá definir o número de ofertas que deseja receber. Padrão: 12
    :type quantidade: int, optional

    :param pagina: Página desejada. Padrão: 1
    :type pagina: int, optional

    :param ordenacao: Ordenação dos resultados. Opções: rating (Ordena por melhor avaliação) e price (Ordena por menor preço). Padrão: rating
    :type pagina: str, optional

    :return: Ofertas
    :rtype: dict
    """
    parametros = {
        "keyword": palavra_chave,
    }

    if categoria_id is not None:
        parametros["categoryId"] = categoria_id

    if loja_id is not None:
        parametros["storeId"] = loja_id

    if quantidade:
        parametros["size"] = quantidade

    if pagina:
        parametros["page"] = pagina

    if ordenacao:
        parametros["sort"] = ordenacao

    if loja_id is None and categoria_id is None:
        raise ValueError("loja_id ou categoria_id precisam ser definidos")

    endpoint = rotas_oferta.BUSCAR

    return manipulador_requisicoes.get(endpoint, parametros)


def obter_por_loja(loja_id: int, categoria_id: int = None, quantidade: int = None, pagina: int = None,
                   ordenacao: str = None) -> dict:
    """
    Consulta as ofertas de uma determinada loja

    :param loja_id: ID de loja. Utilize esse parâmetro para filtrar ofertas de uma determinada loja
    :type loja_id: int

    :param categoria_id: ID de categoria. Utilize esse parâmetro para filtrar ofertas de uma determinada categoria
    :type categoria_id: int, optional

    :param quantidade: Quantidade de ofertas. Com este parâmetro você poderá definir o número de ofertas que deseja receber. Padrão: 12
    :type quantidade: int, optional

    :param pagina: Página desejada. Padrão: 1
    :type pagina: int, optional

    :param ordenacao: Ordenação dos resultados. Opções: rating (Ordena por melhor avaliação) e price (Ordena por menor preço). Padrão: rating
    :type pagina: str, optional

    :return: Ofertas
    :rtype: dict
    """
    parametros = {}

    if categoria_id is not None:
        parametros["categoryId"] = categoria_id

    if quantidade:
        parametros["size"] = quantidade

    if pagina:
        parametros["page"] = pagina

    if ordenacao:
        parametros["sort"] = ordenacao

    endpoint = rotas_oferta.OBTER_POR_LOJA.format(loja_id)

    return manipulador_requisicoes.get(endpoint, parametros)
