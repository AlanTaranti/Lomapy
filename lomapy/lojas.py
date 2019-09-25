"""
.. module:: Lojas
   :synopsis: Interage com as lojas do Lomadee.
"""
from lomapy.helpers.padronizar_resposta import padronizar_resposta_loja
from lomapy.recursos import manipulador_requisicoes
from lomapy.recursos.rotas import rotas_loja


def obter_todas(categoria_id: int = None, possui_oferta: bool = None) -> dict:
    """Lista os parceiros e lojistas da Lomadee

    Parameters
    ----------
    categoria_id: int, optional
        ID de categoria. Utilize esse parâmetro para filtrar lojas que possuem ofertas de uma determinada categoria

    possui_oferta: bool, optional
        Quando "true" retorna apenas lojas que possuem ofertas.

    Returns
    -------
    dict
        Retorna as Lojas encontradas

    Examples
    --------
    >>> import lomapy
    >>> from pprint import pprint
    >>> app_token = "MEU_APP_TOKEN"
    >>> source_id = "MEU_SOURCE_ID"
    >>> lomapy.autenticar(app_token, source_id)
    >>> resposta = lomapy.lojas.obter_todas()
    >>> # Atenção: Mostrado apenas duas lojas, por questão de espaço
    >>> pprint(resposta)  # doctest: +NORMALIZE_WHITESPACE
    {'pagination': {'page': 1, 'size': 178, 'totalPage': 1, 'totalSize': 178},
     'requestInfo': {'generatedDate': None, 'message': 'SUCCESS', 'status': 'OK'},
     'stores': [{'events': [{'commission': 0.064,
                             'event': 'Vendas - Hang Loose',
                             'eventType': 'Sale',
                             'fixedCommission': False}],
                 'hasOffer': 0,
                 'id': 5695,
                 'link': 'https://developer.lomadee.com/redir/validation/?sourceId=MEU_SOURCE_ID&appToken=MEU_APP_TOKEN',
                 'maxCommission': 6.4,
                 'name': 'Hang Loose',
                 'thumbnail': 'https://www.lomadee.com/programas/BR/5695/logo_115x76.png'},
                {'events': [{'commission': 0.0354,
                             'event': 'Cozinha, Ar condicionado, Ferramentas',
                             'eventType': 'Sale',
                             'fixedCommission': False},
                            {'commission': 0.0354,
                             'event': 'Casa e Móveis',
                             'eventType': 'Sale',
                             'fixedCommission': False}],
                 'hasOffer': 0,
                 'id': 5800,
                 'link': 'https://developer.lomadee.com/redir/validation/?sourceId=MEU_SOURCE_ID&appToken=MEU_APP_TOKEN',
                 'maxCommission': 3.54,
                 'name': 'Mega Mamute',
                 'thumbnail': 'https://www.lomadee.com/vitrine/logo590367.gif'}]}
    """
    parametros = {}

    if categoria_id is not None:
        parametros["categoryId"] = categoria_id

    if possui_oferta:
        parametros["hasOffer"] = possui_oferta

    endpoint = rotas_loja.OBTER_TODAS

    resposta = manipulador_requisicoes.get(endpoint, parametros)
    return padronizar_resposta_loja(resposta)
