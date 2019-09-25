from lomapy.modelos import Loja


def obter_loja_original() -> dict:
    return {
        'events': [{'commission': 0.0354,
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
        'thumbnail': 'https://www.lomadee.com/vitrine/logo590367.gif'
    }


def test_construcao():
    loja_original = obter_loja_original()

    loja = Loja()
    loja.construir(loja_original)

    assert loja.id == loja_original["id"]
    assert loja.nome == loja_original["name"]
    assert loja.quantidade_ofertas == loja_original["hasOffer"]
    assert loja.link == loja_original["link"]
    assert loja.comissao_maxima == loja_original["maxCommission"]
    assert loja.thumbnail == loja_original["thumbnail"]
    assert len(loja.eventos) == len(loja_original["events"])


def test_para_dicionario():
    loja_original = obter_loja_original()

    loja = Loja()
    loja.construir(loja_original)
    loja_dicionario = loja.para_dict()

    assert loja_dicionario["id"] == loja_original["id"]
    assert loja_dicionario["nome"] == loja_original["name"]
    assert loja_dicionario["quantidade_ofertas"] == loja_original["hasOffer"]
    assert loja_dicionario["link"] == loja_original["link"]
    assert loja_dicionario["comissao_maxima"] == loja_original["maxCommission"]
    assert loja_dicionario["thumbnail"] == loja_original["thumbnail"]
    assert len(loja_dicionario["eventos"]) == len(loja_original["events"])
