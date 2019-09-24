from lomapy.modelos import Evento


def obter_evento_original() -> dict:
    return {
        'commission': 0.064,
        'event': 'Vendas - Hang Loose',
        'eventType': 'Sale',
        'fixedCommission': False
    }


def test_construcao():
    evento_original = obter_evento_original()

    evento = Evento()
    evento.construir(evento_original)

    assert evento.comissao == evento_original["commission"]
    assert evento.nome == evento_original["event"]
    assert evento.tipo == evento_original["eventType"]
    assert evento.ehComissaoFixa == evento_original["fixedCommission"]


def test_para_dicionario():
    evento_original = obter_evento_original()

    evento = Evento()
    evento.construir(evento_original)
    evento_dicionario = evento.para_dict()

    assert evento_dicionario["comissao"] == evento_original["commission"]
    assert evento_dicionario["nome"] == evento_original["event"]
    assert evento_dicionario["tipo"] == evento_original["eventType"]
    assert evento_dicionario["ehComissaoFixa"] == evento_original["fixedCommission"]
