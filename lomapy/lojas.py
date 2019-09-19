from lomapy.recursos import manipulador_requisicoes
from lomapy.recursos.rotas import rotas_loja


def obter_todas(dados=None) -> dict:
    if dados is None:
        dados = {}

    endpoint = rotas_loja.OBTER_TODAS

    return manipulador_requisicoes.get(endpoint, dados)
