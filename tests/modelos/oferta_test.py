from lomapy.modelos import Oferta


def obter_oferta_original() -> dict:
    return {
        'category': {
            'id': 0,
            'link': 'http://api.lomadee.com/v3/MEU_APP_TOKEN/category/_id/0?sourceId=MEU_SOURCE_ID'
        },
        'id': '00053604',
        'installment': {'quantity': 1, 'value': 36.9},
        'link': 'https://developer.lomadee.com/redir/validation/?sourceId=MEU_SOURCE_ID&appToken=MEU_APP_TOKEN',
        'name': 'Mouse Gamer Fortrek Black Hawk OM-703 7 Botões + Scroll '
                '– Preto/Azul',
        'price': 33.94,
        'priceFrom': 36.9,
        'store': {
            'id': 6064,
            'link': 'https://developer.lomadee.com/redir/validation/?sourceId=MEU_SOURCE_ID&appToken=MEU_APP_TOKEN',
            'name': 'Rede Schumann',
            'thumbnail': 'https://www.lomadee.com/programas/BR/6064/imagemBox_80x60.png'
        },
        'thumbnail': 'http://d3alv7ekdacjys.cloudfront.net/Custom/Content/Products/10/69/1069594_mouse-gamer-fortrek-black-hawk-om-703-7-botoes-scroll-preto-azul_z1_637030130715854141'
    }


def test_construcao():
    oferta_original = obter_oferta_original()

    oferta = Oferta()
    oferta.construir(oferta_original)

    print(oferta.para_dict())

    assert oferta.id == oferta_original["id"]
    assert oferta.nome == oferta_original["name"]
    assert oferta.parcelas["quantidade"] == oferta_original["installment"]["quantity"]
    assert oferta.parcelas["valor"] == oferta_original["installment"]["value"]
    assert oferta.link == oferta_original["link"]
    assert oferta.preco_atual == oferta_original["price"]
    assert oferta.preco_original == oferta_original["priceFrom"]
    assert oferta.thumbnail == oferta_original["thumbnail"]
    assert oferta.categoria.id == oferta_original["category"]["id"]
    assert oferta.loja.id == oferta_original["store"]["id"]


def test_para_dicionario():
    oferta_original = obter_oferta_original()

    oferta = Oferta()
    oferta.construir(oferta_original)
    oferta_dicionario = oferta.para_dict()

    assert oferta_dicionario["id"] == oferta_original["id"]
    assert oferta_dicionario["parcelas"]["quantidade"] == oferta_original["installment"]["quantity"]
    assert oferta_dicionario["parcelas"]["valor"] == oferta_original["installment"]["value"]
    assert oferta_dicionario["link"] == oferta_original["link"]
    assert oferta_dicionario["preco_atual"] == oferta_original["price"]
    assert oferta_dicionario["preco_original"] == oferta_original["priceFrom"]
    assert oferta_dicionario["thumbnail"] == oferta_original["thumbnail"]
    assert oferta_dicionario["categoria"]["id"] == oferta_original["category"]["id"]
    assert oferta_dicionario["loja"]["id"] == oferta_original["store"]["id"]
