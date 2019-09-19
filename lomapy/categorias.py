from lomapy.recursos import manipulador_requisicoes
from lomapy.recursos.rotas import rotas_categoria


def buscar(dados=None) -> dict:
    if dados is None:
        dados = {}

    endpoint = rotas_categoria.BUSCAR

    return manipulador_requisicoes.get(endpoint, dados)


def obter_todas(dados=None) -> dict:
    if dados is None:
        dados = {}

    endpoint = rotas_categoria.OBTER_TODAS

    return manipulador_requisicoes.get(endpoint, dados)


def obter_por_id(categoria_id: int, dados=None) -> dict:
    if dados is None:
        dados = {}

    endpoint = rotas_categoria.OBTER_POR_ID.format(categoria_id)

    return manipulador_requisicoes.get(endpoint, dados)
