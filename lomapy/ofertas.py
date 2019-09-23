"""
.. module:: Ofertas
   :synopsis: Interage com as ofertas do Lomadee.
"""

from lomapy.recursos import manipulador_requisicoes
from lomapy.recursos.rotas import rotas_oferta


def obter_por_categoria(categoria_id: int, loja_id: int = None, quantidade: int = None, pagina: int = None,
                        ordenacao: str = None) -> dict:
    """Consulta as ofertas de uma determinada categoria

    Parameters
    ----------
    categoria_id: int
        ID de categoria. Utilize esse parâmetro para filtrar ofertas de uma determinada categoria

    loja_id: int, optional
        ID de loja. Utilize esse parâmetro para filtrar ofertas de uma determinada loja

    quantidade: int, optional (padrão=12)
        Quantidade de ofertas. Com este parâmetro você poderá definir o número de ofertas que deseja receber

    pagina: int, optional (padrão=1)
        Página desejada

    ordenacao: str, optional (padrão="rating")
        Ordenação dos resultados. Opções: rating (Ordena por melhor avaliação) e price (Ordena por menor preço).

    Returns
    -------
    dict
        Retorna as Ofertas encontradas

    Examples
    --------
    >>> import lomapy
    >>> from pprint import pprint
    >>> app_token = "MEU_APP_TOKEN"
    >>> source_id = "MEU_SOURCE_ID"
    >>> lomapy.autenticar(app_token, source_id)
    >>> categoria = lomapy.categorias.obter_todas()["categories"][0]
    >>> resposta = lomapy.ofertas.obter_por_categoria(categoria["id"])
    >>> # Atenção: Mostrado apenas duas ofertas, por questão de espaço
    >>> pprint(resposta)  # doctest: +NORMALIZE_WHITESPACE
    {'offers': [{'category': {'id': 0,
                              'link': 'http://api.lomadee.com/v3/MEU_APP_TOKEN/category/_id/0?sourceId=MEU_SOURCE_ID'},
                 'id': '000000000001000969',
                 'installment': {'quantity': 12, 'value': 124.91},
                 'link': 'https://developer.lomadee.com/redir/validation/?sourceId=MEU_SOURCE_ID&appToken=MEU_APP_TOKEN',
                 'name': 'Computador Stilo DS3558 Celeron Windows 10 Home '
                         '18.5&#39;&#39; - Preto',
                 'price': 1349.1,
                 'priceFrom': 2229.0,
                 'store': {'id': 6117,
                           'link': 'https://developer.lomadee.com/redir/validation/?sourceId=MEU_SOURCE_ID&appToken=MEU_APP_TOKEN',
                           'name': 'Positivo',
                           'thumbnail': 'https://www.lomadee.com/programas/BR/6117/imagemBox_80x60.png'},
                 'thumbnail': 'https://loja.meupositivo.com.br/Assets/Produtos/Gigantes/111.jpg?v=1b9087fb-1'},
                {'category': {'id': 0,
                              'link': 'http://api.lomadee.com/v3/MEU_APP_TOKEN/category/_id/0?sourceId=MEU_SOURCE_ID'},
                 'id': '000000000001000974',
                 'installment': {'quantity': 12, 'value': 108.25},
                 'link': 'https://developer.lomadee.com/redir/validation/?sourceId=MEU_SOURCE_ID&appToken=MEU_APP_TOKEN',
                 'name': 'Computador Stilo DS3550 Celeron Windows 10 Home - Preto',
                 'price': 1169.1,
                 'priceFrom': 1799.0,
                 'store': {'id': 6117,
                           'link': 'https://developer.lomadee.com/redir/validation/?sourceId=MEU_SOURCE_ID&appToken=MEU_APP_TOKEN',
                           'name': 'Positivo',
                           'thumbnail': 'https://www.lomadee.com/programas/BR/6117/imagemBox_80x60.png'},
                 'thumbnail': 'https://loja.meupositivo.com.br/Assets/Produtos/Gigantes/DeskStilo_Angulo_400x400px.jpg?v=38f01386-1'}],
     'pagination': {'page': 1, 'size': 12, 'totalPage': 40766, 'totalSize': 489187},
     'requestInfo': {'generatedDate': None, 'message': 'SUCCESS', 'status': 'OK'}}
    """
    parametros = {}

    if loja_id is not None:
        parametros["storeId"] = loja_id

    if quantidade:
        parametros["size"] = quantidade

    if pagina:
        parametros["page"] = pagina

    if ordenacao:
        parametros["sort"] = ordenacao

    endpoint = rotas_oferta.OBTER_POR_CATEGORIA.format(categoria_id)

    return manipulador_requisicoes.get(endpoint, parametros)


def obter_por_id(oferta_id: int, loja_id: int) -> dict:
    """Consulta uma oferta específica

    Parameters
    ----------
    oferta_id: int
        ID da oferta desejada

    loja_id: int
        ID de loja. Utilize esse parâmetro para filtrar ofertas de uma determinada loja

    Returns
    -------
    dict
        Retorna as Ofertas encontradas

    Examples
    --------
    >>> import lomapy
    >>> from pprint import pprint
    >>> app_token = "MEU_APP_TOKEN"
    >>> source_id = "MEU_SOURCE_ID"
    >>> lomapy.autenticar(app_token, source_id)
    >>> resposta = lomapy.ofertas.obter_por_id(oferta_id=100003411, loja_id=5632)
    >>> pprint(resposta)  # doctest: +NORMALIZE_WHITESPACE
    {'offers': [{'category': {'id': 0,
                              'link': 'http://api.lomadee.com/v3/MEU_APP_TOKEN/category/_id/0?sourceId=MEU_SOURCE_ID',
                              'name': 'Geral'},
                 'id': '100003411',
                 'installment': {'quantity': 2, 'value': 87.87},
                 'link': 'https://developer.lomadee.com/redir/validation/?sourceId=MEU_SOURCE_ID&appToken=MEU_APP_TOKEN',
                 'name': 'Caixa De Som Swarovski Bluetooth 15 Cristais Original',
                 'price': 175.75,
                 'priceFrom': 175.75,
                 'store': {'id': 5632,
                           'link': 'https://developer.lomadee.com/redir/validation/?sourceId=MEU_SOURCE_ID&appToken=MEU_APP_TOKEN',
                           'name': 'Americanas.com',
                           'thumbnail': 'https://www.lomadee.com/programas/BR/5632/imagemBox_80x60.png'},
                 'thumbnail': 'https://images-americanas.b2w.io/produtos/01/00/images/100003/4/100003410P1.jpg'}],
     'pagination': {'page': 1, 'size': 1, 'totalPage': 1, 'totalSize': 1},
     'requestInfo': {'generatedDate': None, 'message': 'SUCCESS', 'status': 'OK'}}
    """
    parametros = {}

    if loja_id is not None:
        parametros["storeId"] = loja_id

    endpoint = rotas_oferta.OBTER_POR_ID.format(oferta_id)

    return manipulador_requisicoes.get(endpoint, parametros)


def buscar(palavra_chave: str, categoria_id: int = None, loja_id: int = None, quantidade: int = None,
           pagina: int = None, ordenacao: str = None) -> dict:
    """Consulta as ofertas de uma determinada palavra-chave

    Parameters
    ----------
    palavra_chave: str
        Palavra-chave a ser buscada

    categoria_id: int, optional
        ID de categoria. Utilize esse parâmetro para filtrar ofertas de uma determinada categoria

    loja_id: int, optional
        ID de loja. Utilize esse parâmetro para filtrar ofertas de uma determinada loja

    quantidade: int, optional (padrão=12)
        Quantidade de ofertas. Com este parâmetro você poderá definir o número de ofertas que deseja receber.

    pagina: int, optional
        Página desejada (padrão=1)

    ordenacao: str, optional (padrão="rating")
        Ordenação dos resultados. Opções: rating (Ordena por melhor avaliação) e price (Ordena por menor preço).

    Returns
    -------
    dict
        Retorna as Ofertas encontradas

    Examples
    --------
    >>> import lomapy
    >>> from pprint import pprint
    >>> app_token = "MEU_APP_TOKEN"
    >>> source_id = "MEU_SOURCE_ID"
    >>> lomapy.autenticar(app_token, source_id)
    >>> categoria = lomapy.categorias.obter_todas()["categories"][0]
    >>> resposta = lomapy.ofertas.buscar(palavra_chave="mouse", categoria_id=categoria["id"])
    >>> # Atenção: Mostrado apenas duas ofertas, por questão de espaço
    >>> pprint(resposta)  # doctest: +NORMALIZE_WHITESPACE
    {'offers': [{'category': {'id': 0,
                              'link': 'http://api.lomadee.com/v3/MEU_APP_TOKEN/category/_id/0?sourceId=MEU_SOURCE_ID'},
                 'id': '00053604',
                 'installment': {'quantity': 1, 'value': 36.9},
                 'link': 'https://developer.lomadee.com/redir/validation/?sourceId=MEU_SOURCE_ID&appToken=MEU_APP_TOKEN',
                 'name': 'Mouse Gamer Fortrek Black Hawk OM-703 7 Botões + Scroll '
                         '– Preto/Azul',
                 'price': 33.94,
                 'priceFrom': 36.9,
                 'store': {'id': 6064,
                           'link': 'https://developer.lomadee.com/redir/validation/?sourceId=MEU_SOURCE_ID&appToken=MEU_APP_TOKEN',
                           'name': 'Rede Schumann',
                           'thumbnail': 'https://www.lomadee.com/programas/BR/6064/imagemBox_80x60.png'},
                 'thumbnail': 'http://d3alv7ekdacjys.cloudfront.net/Custom/Content/Products/10/69/1069594_mouse-gamer-fortrek-black-hawk-om-703-7-botoes-scroll-preto-azul_z1_637030130715854141'},
                {'category': {'id': 0,
                              'link': 'http://api.lomadee.com/v3/MEU_APP_TOKEN/category/_id/0?sourceId=MEU_SOURCE_ID'},
                 'id': '00053604-00053604',
                 'installment': {'quantity': 1, 'value': 36.9},
                 'link': 'https://developer.lomadee.com/redir/validation/?sourceId=MEU_SOURCE_ID&appToken=MEU_APP_TOKEN',
                 'name': 'Mouse Gamer Fortrek Black Hawk OM-703 7 Botões + Scroll '
                         '– Preto/Azul',
                 'price': 33.94,
                 'priceFrom': 36.9,
                 'store': {'id': 6064,
                           'link': 'https://developer.lomadee.com/redir/validation/?sourceId=MEU_SOURCE_ID&appToken=MEU_APP_TOKEN',
                           'name': 'Rede Schumann',
                           'thumbnail': 'https://www.lomadee.com/programas/BR/6064/imagemBox_80x60.png'},
                 'thumbnail': 'http://d3alv7ekdacjys.cloudfront.net/Custom/Content/Products/10/69/1069594_mouse-gamer-fortrek-black-hawk-om-703-7-botoes-scroll-preto-azul_z1_637030130715854141'}],
     'pagination': {'page': 1, 'size': 12, 'totalPage': 112, 'totalSize': 1343},
     'requestInfo': {'generatedDate': None, 'message': 'SUCCESS', 'status': 'OK'}}
    """
    parametros = {
        "keyword": palavra_chave,
    }

    if categoria_id is not None:
        parametros["categoryId"] = categoria_id

    if loja_id is not None:
        parametros["storeId"] = loja_id

    if quantidade:
        parametros["size"] = quantidade

    if pagina:
        parametros["page"] = pagina

    if ordenacao:
        parametros["sort"] = ordenacao

    if loja_id is None and categoria_id is None:
        raise ValueError("loja_id ou categoria_id precisam ser definidos")

    endpoint = rotas_oferta.BUSCAR

    return manipulador_requisicoes.get(endpoint, parametros)


def obter_por_loja(loja_id: int, categoria_id: int = None, quantidade: int = None, pagina: int = None,
                   ordenacao: str = None) -> dict:
    """Consulta as ofertas de uma determinada loja

    Parameters
    ----------
    loja_id: int
        ID de loja. Utilize esse parâmetro para filtrar ofertas de uma determinada loja

    categoria_id: int, optional
        ID de categoria. Utilize esse parâmetro para filtrar ofertas de uma determinada categoria

    quantidade: int, optional (padrão=12)
        Quantidade de ofertas. Com este parâmetro você poderá definir o número de ofertas que deseja receber.

    pagina: int, optional (padrão=1)
        Página desejada.

    ordenacao: str, optional (padrão="rating")
        Ordenação dos resultados. Opções: rating (Ordena por melhor avaliação) e price (Ordena por menor preço).

    Returns
    -------
    dict
        Retorna as Ofertas encontradas

    Examples
    --------
    >>> import lomapy
    >>> from pprint import pprint
    >>> app_token = "MEU_APP_TOKEN"
    >>> source_id = "MEU_SOURCE_ID"
    >>> lomapy.autenticar(app_token, source_id)
    >>> resposta = lomapy.ofertas.obter_por_loja(5632)
    >>> # Atenção: Mostrado apenas duas ofertas, por questão de espaço
    >>> pprint(resposta)  # doctest: +NORMALIZE_WHITESPACE
    {'offers': [{'category': {'id': 0,
                              'link': 'http://api.lomadee.com/v3/MEU_APP_TOKEN/category/_id/0?sourceId=MEU_SOURCE_ID'},
                 'id': '100003411',
                 'installment': {'quantity': 2, 'value': 87.87},
                 'link': 'https://developer.lomadee.com/redir/validation/?sourceId=MEU_SOURCE_ID&appToken=MEU_APP_TOKEN',
                 'name': 'Caixa De Som Swarovski Bluetooth 15 Cristais Original',
                 'price': 175.75,
                 'priceFrom': 175.75,
                 'store': {'id': 5632,
                           'link': 'https://developer.lomadee.com/redir/validation/?sourceId=MEU_SOURCE_ID&appToken=MEU_APP_TOKEN',
                           'name': 'Americanas.com',
                           'thumbnail': 'https://www.lomadee.com/programas/BR/5632/imagemBox_80x60.png'},
                 'thumbnail': 'https://images-americanas.b2w.io/produtos/01/00/images/100003/4/100003410P1.jpg'},
                {'category': {'id': 6458,
                              'link': 'http://api.lomadee.com/v3/MEU_APP_TOKEN/category/_id/6458?sourceId=MEU_SOURCE_ID'},
                 'id': '100006135',
                 'installment': {'quantity': 7, 'value': 145.7},
                 'link': 'https://developer.lomadee.com/redir/validation/?sourceId=MEU_SOURCE_ID&appToken=MEU_APP_TOKEN',
                 'name': 'Caixa Amplificada Frahm Mf800 - Usb - Bt - Controle '
                         'Remoto',
                 'price': 1019.9,
                 'priceFrom': 1019.9,
                 'store': {'id': 5632,
                           'link': 'https://developer.lomadee.com/redir/validation/?sourceId=MEU_SOURCE_ID&appToken=MEU_APP_TOKEN',
                           'name': 'Americanas.com',
                           'thumbnail': 'https://www.lomadee.com/programas/BR/5632/imagemBox_80x60.png'},
                 'thumbnail': 'https://images-americanas.b2w.io/produtos/01/00/images/100006/1/100006134P1.jpg'}],
     'pagination': {'page': 1, 'size': 12, 'totalPage': 15411, 'totalSize': 184930},
     'requestInfo': {'generatedDate': None, 'message': 'SUCCESS', 'status': 'OK'}}
    """
    parametros = {}

    if categoria_id is not None:
        parametros["categoryId"] = categoria_id

    if quantidade:
        parametros["size"] = quantidade

    if pagina:
        parametros["page"] = pagina

    if ordenacao:
        parametros["sort"] = ordenacao

    endpoint = rotas_oferta.OBTER_POR_LOJA.format(loja_id)

    return manipulador_requisicoes.get(endpoint, parametros)
