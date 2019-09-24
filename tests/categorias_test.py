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


def validar_resposta(resposta):
    assert type(resposta) is dict
    assert type(resposta["categorias"]) is list
    assert len(resposta["categorias"]) == resposta["paginacao"]["quantidade"]


def test_buscar():
    resposta = lomapy.categorias.buscar("info")

    validar_resposta(resposta)


def test_obter_todas():
    resposta = lomapy.categorias.obter_todas()

    validar_resposta(resposta)


def test_obter_por_id():
    categoria = lomapy.categorias.obter_todas()["categorias"][0]
    resposta = lomapy.categorias.obter_por_id(categoria["id"])

    validar_resposta(resposta)
