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


def test_buscar():
    dados = {
        "keyword": "info"
    }

    resposta = lomapy.categorias.buscar(dados)

    assert type(resposta) is dict
    assert resposta["requestInfo"]["status"] == "OK"
    assert type(resposta["categories"]) is list


def test_obter_todas():
    resposta = lomapy.categorias.obter_todas()

    assert type(resposta) is dict
    assert resposta["requestInfo"]["status"] == "OK"
    assert type(resposta["categories"]) is list


def test_obter_por_id():
    categoria = lomapy.categorias.obter_todas()["categories"][0]
    resposta = lomapy.categorias.obter_por_id(categoria["id"])

    assert type(resposta) is dict
    assert resposta["requestInfo"]["status"] == "OK"
    assert type(resposta["categories"]) is list
