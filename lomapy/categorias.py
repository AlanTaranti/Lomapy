"""
.. module:: Categorias
   :synopsis: Interage com as categorias do Lomadee.
"""
from lomapy.helpers import padronizar_resposta_categoria
from lomapy.recursos import manipulador_requisicoes
from lomapy.recursos.rotas import rotas_categoria


def buscar(palavra_chave: str, loja_id: int = None, possui_oferta: bool = None, quantidade: int = None) -> dict:
    """Realiza a busca de categorias através de palavras

    Parameters
    ----------
    palavra_chave : str
        Palavra-chave a ser buscada.

    loja_id : int, optional
        ID de loja. Utilize esse parâmetro para filtrar categorias que possuem ofertas de uma determinada loja

    possui_oferta : bool, optional
        Quando "true" retorna apenas categorias que possuem ofertas.

    quantidade : int, optional (padrão=12)
        Quantidade de categorias. Com este parâmetro você poderá definir o número de categorias que deseja receber.

    Returns
    -------
    dict
        Retorna as Categorias encontradas

    Examples
    --------
    >>> import lomapy
    >>> from pprint import pprint
    >>> app_token = "MEU_APP_TOKEN"
    >>> source_id = "MEU_SOURCE_ID"
    >>> lomapy.autenticar(app_token, source_id)
    >>> resposta = lomapy.categorias.buscar("info", quantidade=2)
    >>> pprint(resposta)  # doctest: +NORMALIZE_WHITESPACE
    {'categories': [{'hasOffer': 493,
                     'id': 2,
                     'link': 'http://api.lomadee.com/v3/MEU_APP_TOKEN/category/_id/2?sourceId=MEU_SOURCE_ID',
                     'name': 'Informática'},
                    {'hasOffer': 325,
                     'id': 7074,
                     'link': 'http://api.lomadee.com/v3/MEU_APP_TOKEN/category/_id/7074?sourceId=MEU_SOURCE_ID',
                     'name': 'Acessórios para Informática'}],
     'pagination': {'page': 1, 'size': 2, 'totalPage': 1, 'totalSize': 2},
     'requestInfo': {'generatedDate': None, 'message': 'SUCCESS', 'status': 'OK'}}
    """
    parametros = {
        "keyword": palavra_chave,
    }

    if loja_id is not None:
        parametros["storeId"] = loja_id

    if possui_oferta is not None:
        parametros["hasOffer"] = possui_oferta

    if quantidade is not None:
        parametros["size"] = quantidade

    endpoint = rotas_categoria.BUSCAR

    resposta = manipulador_requisicoes.get(endpoint, parametros)
    return padronizar_resposta_categoria(resposta)


def obter_todas(loja_id: int = None, possui_oferta: bool = None) -> dict:
    """Consulta a lista de todas as categorias que possuem ofertas dos lojistas parceiros da Lomadee.

    Parameters
    ----------
    loja_id: int, optional
        ID de loja. Utilize esse parâmetro para filtrar categorias que possuem ofertas de uma determinada loja

    possui_oferta: bool, optional
        Quando "true" retorna apenas categorias que possuem ofertas.

    Returns
    -------
    dict
        Retorna as Categorias encontradas

    Examples
    --------
    >>> import lomapy
    >>> from pprint import pprint
    >>> app_token = "MEU_APP_TOKEN"
    >>> source_id = "MEU_SOURCE_ID"
    >>> lomapy.autenticar(app_token, source_id)
    >>> resposta = lomapy.categorias.obter_todas()
    >>> # Atenção: Mostrado apenas duas categorias, por questão de espaço
    >>> pprint(resposta)  # doctest: +NORMALIZE_WHITESPACE
    {'categories': [{'hasOffer': 522904,
                     'id': 0,
                     'link': 'http://api.lomadee.com/v3/MEU_APP_TOKEN/category/_id/0?sourceId=MEU_SOURCE_ID',
                     'name': 'Geral'},
                    {'hasOffer': 18634,
                     'id': 10897,
                     'link': 'http://api.lomadee.com/v3/MEU_APP_TOKEN/category/_id/10897?sourceId=MEU_SOURCE_ID',
                     'name': 'Vestido Feminino Plus Size'}],
     'pagination': {'page': 1, 'size': 5957, 'totalPage': 1, 'totalSize': 5957},
     'requestInfo': {'generatedDate': None, 'message': 'SUCCESS', 'status': 'OK'}}
    """
    parametros = {}

    if loja_id is not None:
        parametros["storeId"] = loja_id

    if possui_oferta is not None:
        parametros["hasOffer"] = possui_oferta

    endpoint = rotas_categoria.OBTER_TODAS

    resposta = manipulador_requisicoes.get(endpoint, parametros)
    return padronizar_resposta_categoria(resposta)


def obter_por_id(categoria_id: int, loja_id: int = None) -> dict:
    """Obtem uma categoria específica de acordo com o ID

    Parameters
    ----------
    categoria_id : int
        ID da categoria desejada

    loja_id: int, optional
        ID de loja. Utilize esse parâmetro para filtrar categorias que possuem ofertas de uma determinada loja

    Returns
    -------
    dict
        Retorna as Categorias encontradas

    Examples
    --------
    >>> import lomapy
    >>> from pprint import pprint
    >>> app_token = "MEU_APP_TOKEN"
    >>> source_id = "MEU_SOURCE_ID"
    >>> lomapy.autenticar(app_token, source_id)
    >>> categoria = lomapy.categorias.obter_todas()["categories"][0]
    >>> resposta = lomapy.categorias.obter_por_id(categoria["id"])
    >>> pprint(resposta)  # doctest: +NORMALIZE_WHITESPACE
    {'categories': [{'hasOffer': 522904,
                     'id': 0,
                     'link': 'http://api.lomadee.com/v3/MEU_APP_TOKEN/category/_id/0?sourceId=MEU_SOURCE_ID',
                     'name': 'Geral'}],
     'pagination': {'page': 1, 'size': 1, 'totalPage': 1, 'totalSize': 1},
     'requestInfo': {'generatedDate': None, 'message': 'SUCCESS', 'status': 'OK'}}
    """
    parametros = {}

    if loja_id is not None:
        parametros["storeId"] = loja_id

    endpoint = rotas_categoria.OBTER_POR_ID.format(categoria_id)

    resposta = manipulador_requisicoes.get(endpoint, parametros)
    return padronizar_resposta_categoria(resposta)
