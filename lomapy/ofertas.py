from lomapy.recursos import manipulador_requisicoes
from lomapy.recursos.rotas import rotas_oferta


def obter_por_categoria(categoria_id: int, dados=None) -> dict:
    if dados is None:
        dados = {}

    endpoint = rotas_oferta.OBTER_POR_CATEGORIA.format(categoria_id)

    return manipulador_requisicoes.get(endpoint, dados)


def obter_por_id(oferta_id: int, dados=None) -> dict:
    if dados is None:
        dados = {}

    endpoint = rotas_oferta.OBTER_POR_ID.format(oferta_id)

    return manipulador_requisicoes.get(endpoint, dados)


def buscar(dados=None) -> dict:
    if dados is None:
        dados = {}

    endpoint = rotas_oferta.BUSCAR

    return manipulador_requisicoes.get(endpoint, dados)


def obter_por_loja(loja_id: int, dados=None) -> dict:
    if dados is None:
        dados = {}

    endpoint = rotas_oferta.OBTER_POR_LOJA.format(loja_id)

    return manipulador_requisicoes.get(endpoint, dados)
