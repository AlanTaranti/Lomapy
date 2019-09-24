.. _topics-index:

=============================
Lomapy |release| Documentação
=============================

Lomapy é uma biblioteca **não oficial** que disponibiliza um interface em python para a API de Afiliados do Lomadee.
O Lomapy é compatível com versão 3 da API da Lomadee.

Instalação
==========

O Lomapy roda em Python 3.4 ou superior.

Para instalar o Lomapy com o pip::

   pip install lomapy

Primeiros Passos
================
Para utilizar o Lomapy, você precisa de uma APP_KEY e um SOURCE_ID da Lomadee.
Caso não os possua, você pode obtê-los em https://developer.lomadee.com/ ::

    # Importar a biblioteca
    import lomapy

    # Definir suas chaves
    app_token = {SEU_APP_TOKEN_AQUI}
    source_id = {SEU_SOURCE_ID_AQUI}

    # Passar as chaves para lomapy
    lomapy.autenticar(app_token, source_id)

    # Listar todas as categorias
    lomapy.categorias.obter_todas()


Módulos
=======

.. toctree::
   :caption: Módulos
   :hidden:

   modulos/categorias
   modulos/lojas
   modulos/ofertas

O Lomapy possui três modulos interagir com a API de Ofertas do Lomadee.

:doc:`modulos/categorias`
    Métodos do módulo Categorias.

:doc:`modulos/lojas`
    Métodos do módulo Lojas.

:doc:`modulos/ofertas`
    Métodos do módulo Ofertas.

Modo Produção
=============
Por padrão, o Lomapy funciona no modo desenvolvimento (caixa de areia).
Para ativar o modo produção, basta passar o valor False para o parâmetro caixa_de_areia no método autenticar ::

    # Importar a biblioteca
    import lomapy

    # Definir suas chaves
    app_token = {SEU_APP_TOKEN_AQUI}
    source_id = {SEU_SOURCE_ID_AQUI}

    # Passar as chaves para lomapy
    lomapy.autenticar(app_token, source_id, caixa_de_areia=False)

    # Listar todas as categorias
    lomapy.categorias.obter_todas()

Contribua
=========

Quera ajudar a melhorar o Lomapy? Contribua com o código e/ou reporte algum problema que encontrar.

- `Rastreador de Problemas`_
- `Código Fonte`_

.. _Rastreador de Problemas: https://github.com/AlanTaranti/Lomapy/issues
.. _Código Fonte: https://github.com/AlanTaranti/Lomapy
