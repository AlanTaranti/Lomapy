"""
.. module:: Manipulador de Requisições
   :synopsis: Gerencia as requisições para a API da Lomadee
"""

import requests
from lomapy.recursos.sdk import sdk

# URLs de Produção e Caixa de Areia
CAIXA_DE_AREIA = 'http://sandbox-api.lomadee.com/v3/'
PRODUCAO = "https://api.lomadee.com/v3/"

PARAMETROS_GLOBAIS = {}


def validar_reposta(resposta: requests.Response) -> dict:
    """
    Valida a resposta da API do Lomadee e retorna os dados

    :param resposta: Reposta a ser validada
    :type resposta: requests.Response

    :raises Exception: Falha na requisição

    :return: Dados da Resposta
    :rtype: dict
    """
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return erro(resposta)


def obter_url(endpoint: str) -> str:
    """
    Obtem a url de acordo com o endpoint

    :param endpoint: Endpoint
    :type endpoint: str

    :return: URL
    :rtype: str
    """
    url_base = CAIXA_DE_AREIA if PARAMETROS_GLOBAIS["caixa_de_areia"] else PRODUCAO
    return "{}{}{}".format(url_base, PARAMETROS_GLOBAIS["app_token"], endpoint)


def autenticar(app_token: str, source_id: str, caixa_de_areia: bool = True):
    """
    Define os parametros de autenticação da Lomadee

    :param app_token: APP_TOKEN da Lomadee
    :type app_token: str

    :param source_id: SOURCE_ID da Lomadee
    :type source_id: str

    :param caixa_de_areia: Define se o ambiente é o caixa de areia. Padrão: True
    :type caixa_de_areia: bool
    """
    global PARAMETROS_GLOBAIS
    PARAMETROS_GLOBAIS['app_token'] = app_token
    PARAMETROS_GLOBAIS['source_id'] = source_id
    PARAMETROS_GLOBAIS['caixa_de_areia'] = caixa_de_areia


def get(endpoint: str, parametros: dict = None) -> dict:
    """
    Realiza um requisição HTTP do tipo GET para a API da Lomadee

    :param endpoint: Endpoint da requisição
    :type endpoint: str

    :param parametros: Parâmetros da requisição
    :type parametros: dict

    :return: Dados da Resposta
    :rtype: dict
    """
    if parametros is None:
        parametros = {}

    parametros['sourceId'] = PARAMETROS_GLOBAIS['source_id']
    url = obter_url(endpoint)
    resposta = requests.get(url, params=parametros, headers=cabecalhos())

    return validar_reposta(resposta)


def erro(resposta: requests.Response):
    """
    Gera uma exceção padronizada

    :param resposta: Resposta
    :type resposta: requests.Response

    :raises Exception: Falha na requisição
    """
    raise Exception({
        "codigo": resposta.status_code,
        "motivo": resposta.reason,
        "resposta": resposta.json()
    })


def cabecalhos() -> dict:
    """
    Gera o cabeçalho da requisição

    :return: Cabecalhos
    :rtype: dict
    """
    _headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'User-Agent': 'lomapy/v{}'.format(sdk.VERSAO)
    }
    return _headers
