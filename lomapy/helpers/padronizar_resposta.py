from typing import List

from lomapy.modelos import Categoria


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


def _padronizar_categorias(lista_categorias_nao_padronizadas) -> List[dict]:
    categorias = []
    for c in lista_categorias_nao_padronizadas:
        categorias.append(_padronizar_categoria(c))
    return categorias


def padronizar_resposta_categoria(resposta) -> dict:
    return {
        "categorias": _padronizar_categorias(resposta["categories"]),
        "paginacao": _padronizar_paginacao(resposta["pagination"])
    }
