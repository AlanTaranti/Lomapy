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
    assert type(resposta["ofertas"]) is list
    assert len(resposta["ofertas"]) == resposta["paginacao"]["quantidade"]


def test_buscar():
    categoria = lomapy.categorias.obter_todas()["categorias"][0]

    resposta = lomapy.ofertas.buscar(palavra_chave="info", categoria_id=categoria["id"])

    validar_resposta(resposta)


def test_obter_por_categoria():
    categoria = lomapy.categorias.obter_todas()["categorias"][0]
    resposta = lomapy.ofertas.obter_por_categoria(categoria["id"])

    validar_resposta(resposta)


def test_obter_por_id():
    resposta = lomapy.ofertas.obter_por_id(100003411, 5632)

    validar_resposta(resposta)


def test_obter_por_loja():
    resposta = lomapy.ofertas.obter_por_loja(5632)

    validar_resposta(resposta)
