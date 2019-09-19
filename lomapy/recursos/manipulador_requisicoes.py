import requests
from lomapy.recursos.sdk import sdk

CAIXA_DE_AREIA = 'http://sandbox-api.lomadee.com/v3/'
PRODUCAO = "https://api.lomadee.com/v3/"

PARAMETROS = {}


def validar_reposta(resposta: requests.Response) -> dict:
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return erro(resposta)


def obter_url(endpoint: str) -> str:
    url_base = CAIXA_DE_AREIA if PARAMETROS["caixa_de_areia"] else PRODUCAO
    return "{}{}{}".format(url_base, PARAMETROS["app_token"], endpoint)


def autenticar(app_token: str, source_id: str, caixa_de_areia=True):
    global PARAMETROS
    PARAMETROS['app_token'] = app_token
    PARAMETROS['source_id'] = source_id
    PARAMETROS['caixa_de_areia'] = caixa_de_areia


def get(endpoint: str, dados=None) -> dict:
    if dados is None:
        dados = {}

    dados['sourceId'] = PARAMETROS['source_id']
    url = obter_url(endpoint)
    resposta = requests.get(url, params=dados, headers=cabecalhos())

    return validar_reposta(resposta)


def erro(resposta: requests.Response):
    raise Exception({
        "codigo": resposta.status_code,
        "motivo": resposta.reason,
        "resposta": resposta.json()
    })


def cabecalhos() -> dict:
    _headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'User-Agent': 'lomapy/v{}'.format(sdk.VERSAO)
    }
    return _headers
