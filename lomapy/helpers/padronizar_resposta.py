from typing import List

from lomapy.modelos import Categoria, Loja, Oferta


def _padronizar_paginacao(paginacao_nao_padronizada):
    return {
        "pagina": paginacao_nao_padronizada["page"],
        "quantidade": paginacao_nao_padronizada["size"],
        "total_paginas": paginacao_nao_padronizada["totalPage"],
        "total_quantidade": paginacao_nao_padronizada["totalSize"]
    }


def _padronizar_categoria(categoria_nao_padronizada) -> dict:
    categoria = Categoria()
    categoria.construir(categoria_nao_padronizada)
    return categoria.para_dict()


def _padronizar_loja(loja_nao_padronizada) -> dict:
    loja = Loja()
    loja.construir(loja_nao_padronizada)
    return loja.para_dict()


def _padronizar_oferta(oferta_nao_padronizada) -> dict:
    oferta = Oferta()
    oferta.construir(oferta_nao_padronizada)
    return oferta.para_dict()


def _padronizar_categorias(lista_categorias_nao_padronizadas) -> List[dict]:
    categorias = []
    for c in lista_categorias_nao_padronizadas:
        categorias.append(_padronizar_categoria(c))
    return categorias


def _padronizar_lojas(lista_lojas_nao_padronizadas) -> List[dict]:
    lojas = []
    for l in lista_lojas_nao_padronizadas:
        lojas.append(_padronizar_loja(l))
    return lojas


def _padronizar_ofertas(lista_ofertas_nao_padronizadas) -> List[dict]:
    ofertas = []
    for o in lista_ofertas_nao_padronizadas:
        ofertas.append(_padronizar_oferta(o))
    return ofertas


def padronizar_resposta_categoria(resposta) -> dict:
    return {
        "categorias": _padronizar_categorias(resposta["categories"]),
        "paginacao": _padronizar_paginacao(resposta["pagination"])
    }


def padronizar_resposta_loja(resposta) -> dict:
    return {
        "lojas": _padronizar_lojas(resposta["stores"]),
        "paginacao": _padronizar_paginacao(resposta["pagination"])
    }


def padronizar_resposta_oferta(resposta) -> dict:
    return {
        "ofertas": _padronizar_ofertas(resposta["offers"]),
        "paginacao": _padronizar_paginacao(resposta["pagination"])
    }
