from lomapy.modelos import Categoria


def obter_categoria_original() -> dict:
    return {
        'hasOffer': 493,
        'id': 2,
        'link': 'http://api.lomadee.com/v3/MEU_APP_TOKEN/category/_id/2?sourceId=MEU_SOURCE_ID',
        'name': 'Informática'
    }


def test_construcao():
    categoria_original = obter_categoria_original()

    categoria = Categoria()
    categoria.construir(categoria_original)

    assert categoria.nome == categoria_original["name"]
    assert categoria.id == categoria_original["id"]
    assert categoria.quantidade_ofertas == categoria_original["hasOffer"]
    assert categoria.link == categoria_original["link"]


def test_para_dicionario():
    categoria_original = obter_categoria_original()

    categoria = Categoria()
    categoria.construir(categoria_original)
    categoria_dicionario = categoria.para_dict()

    assert categoria_dicionario["nome"] == categoria_original["name"]
    assert categoria_dicionario["id"] == categoria_original["id"]
    assert categoria_dicionario["quantidade_ofertas"] == categoria_original["hasOffer"]
    assert categoria_dicionario["link"] == categoria_original["link"]
