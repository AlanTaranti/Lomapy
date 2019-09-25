import os
import lomapy
from dotenv import load_dotenv

#
# Configurar Lomapy
#

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

app_token = os.environ.get("LOMAPY_APP_TOKEN")
source_id = os.environ.get("LOMAPY_SOURCE_ID")
lomapy.autenticar(app_token, source_id)


def validacao_padrao(resposta):
    assert type(resposta) is dict
    assert type(resposta["lojas"]) is list
    assert len(resposta["lojas"]) == resposta["paginacao"]["quantidade"]


def test_obter_todas():
    resposta = lomapy.lojas.obter_todas()

    validacao_padrao(resposta)


def test_obter_todas_por_categoria():
    categoria = lomapy.categorias.obter_todas()["categorias"][0]

    resposta = lomapy.lojas.obter_todas(categoria_id=categoria["id"])

    validacao_padrao(resposta)


def test_obter_todas_por_possuir_oferta():

    resposta = lomapy.lojas.obter_todas(possui_oferta=True)
    validacao_padrao(resposta)
    assert resposta["lojas"][0]["quantidade_ofertas"] > 0

    resposta = lomapy.lojas.obter_todas(possui_oferta=False)
    validacao_padrao(resposta)
    assert resposta["lojas"][0]["quantidade_ofertas"] == 0

