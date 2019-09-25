"""
.. module:: Ofertas
   :synopsis: Interage com as ofertas do Lomadee.
"""
from lomapy.helpers.padronizar_resposta import padronizar_resposta_oferta
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
    >>> resposta = lomapy.ofertas.obter_por_categoria(categoria["id"], quantidade=2)
    >>> # Atenção: Mostrado apenas duas ofertas, por questão de espaço
    >>> pprint(resposta)  # doctest: +NORMALIZE_WHITESPACE
    {
        'ofertas': [
            {
                'categoria': {
                    'id': 0,
                    'link': 'http://api.lomadee.com/v3/MEU_APP_TOKEN/category/_id/0?sourceId=MEU_SOURCE_ID',
                    'nome': None,
                    'quantidade_ofertas': None
                },
                'id': '000000000001000969',
                'link': 'https://developer.lomadee.com/redir/validation/?sourceId=MEU_SOURCE_ID&appToken=MEU_APP_TOKEN',
                'loja': {
                    'comissao_maxima': None,
                    'eventos': [],
                    'id': 6117,
                    'link': 'https://developer.lomadee.com/redir/validation/?sourceId=MEU_SOURCE_ID&appToken=MEU_APP_TOKEN',
                    'nome': 'Positivo',
                    'quantidade_ofertas': None,
                    'thumbnail': 'https://www.lomadee.com/programas/BR/6117/imagemBox_80x60.png'
                },
                'nome': 'Computador Stilo DS3558 Celeron Windows 10 Home 18.5&#39;&#39; - Preto',
                'parcelas': {'quantidade': 12, 'valor': 124.91},
                'preco_atual': 1349.1,
                'preco_original': 2229.0,
                'thumbnail': 'https://loja.meupositivo.com.br/Assets/Produtos/Gigantes/111.jpg?v=1b9087fb-1'
            },
            {
                'categoria': {
                    'id': 0,
                    'link': 'http://api.lomadee.com/v3/MEU_APP_TOKEN/category/_id/0?sourceId=MEU_SOURCE_ID',
                    'nome': None,
                    'quantidade_ofertas': None
                },
                'id': '000000000001000974',
                'link': 'https://developer.lomadee.com/redir/validation/?sourceId=MEU_SOURCE_ID&appToken=MEU_APP_TOKEN',
                'loja': {
                    'comissao_maxima': None,
                    'eventos': [],
                    'id': 6117,
                    'link': 'https://developer.lomadee.com/redir/validation/?sourceId=MEU_SOURCE_ID&appToken=MEU_APP_TOKEN',
                    'nome': 'Positivo',
                    'quantidade_ofertas': None,
                    'thumbnail': 'https://www.lomadee.com/programas/BR/6117/imagemBox_80x60.png'
                },
                'nome': 'Computador Stilo DS3550 Celeron Windows 10 Home - Preto',
                'parcelas': {'quantidade': 12, 'valor': 108.25},
                'preco_atual': 1169.1,
                'preco_original': 1799.0,
                'thumbnail': 'https://loja.meupositivo.com.br/Assets/Produtos/Gigantes/DeskStilo_Angulo_400x400px.jpg?v=38f01386-1'
            }
        ],
        'paginacao': {
            'pagina': 1,
            'quantidade': 2,
            'total_paginas': 244664,
            'total_quantidade': 489327
        }
    }
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

    resposta = manipulador_requisicoes.get(endpoint, parametros)
    return padronizar_resposta_oferta(resposta)


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
    {
        'ofertas': [
            {
                'categoria': {
                    'id': 0,
                    'link': 'http://api.lomadee.com/v3/MEU_APP_TOKEN/category/_id/0?sourceId=MEU_SOURCE_ID',
                    'nome': 'Geral',
                    'quantidade_ofertas': None
                },
                'id': '100003411',
                'link': 'https://developer.lomadee.com/redir/validation/?sourceId=MEU_SOURCE_ID&appToken=MEU_APP_TOKEN',
                'loja': {
                    'comissao_maxima': None,
                    'eventos': [],
                    'id': 5632,
                    'link': 'https://developer.lomadee.com/redir/validation/?sourceId=MEU_SOURCE_ID&appToken=MEU_APP_TOKEN',
                    'nome': 'Americanas.com',
                    'quantidade_ofertas': None,
                    'thumbnail': 'https://www.lomadee.com/programas/BR/5632/imagemBox_80x60.png'
                },
                'nome': 'Caixa De Som Swarovski Bluetooth 15 Cristais Original',
                'parcelas': {'quantidade': 2, 'valor': 87.87},
                'preco_atual': 175.75,
                'preco_original': 175.75,
                'thumbnail': 'https://images-americanas.b2w.io/produtos/01/00/images/100003/4/100003410P1.jpg'
            }
        ],
        'paginacao': {
            'pagina': 1,
            'quantidade': 1,
            'total_paginas': 1,
            'total_quantidade': 1
        }
    }
    """
    parametros = {}

    if loja_id is not None:
        parametros["storeId"] = loja_id

    endpoint = rotas_oferta.OBTER_POR_ID.format(oferta_id)

    resposta = manipulador_requisicoes.get(endpoint, parametros)
    return padronizar_resposta_oferta(resposta)


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
    >>> resposta = lomapy.ofertas.buscar(palavra_chave="mouse", categoria_id=categoria["id"], quantidade=2)
    >>> pprint(resposta)  # doctest: +NORMALIZE_WHITESPACE
    {
        'ofertas': [
            {
                'categoria': {
                    'id': 0,
                    'link': 'http://api.lomadee.com/v3/MEU_APP_TOKEN/category/_id/0?sourceId=MEU_SOURCE_ID',
                    'nome': None,
                    'quantidade_ofertas': None
                },
                'id': '00053604',
                'link': 'https://developer.lomadee.com/redir/validation/?sourceId=MEU_SOURCE_ID&appToken=MEU_APP_TOKEN',
                'loja': {
                    'comissao_maxima': None,
                    'eventos': [],
                    'id': 6064,
                    'link': 'https://developer.lomadee.com/redir/validation/?sourceId=MEU_SOURCE_ID&appToken=MEU_APP_TOKEN',
                    'nome': 'Rede Schumann',
                    'quantidade_ofertas': None,
                    'thumbnail': 'https://www.lomadee.com/programas/BR/6064/imagemBox_80x60.png'
                },
                'nome': 'Mouse Gamer Fortrek Black Hawk OM-703 7 Botões + Scroll – Preto/Azul',
                'parcelas': {
                    'quantidade': 1,
                    'valor': 36.9
                },
                'preco_atual': 33.94,
                'preco_original': 36.9,
                'thumbnail': 'http://d3alv7ekdacjys.cloudfront.net/Custom/Content/Products/10/69/1069594_mouse-gamer-fortrek-black-hawk-om-703-7-botoes-scroll-preto-azul_z1_637030130715854141'
            },
            {
                'categoria': {
                    'id': 0,
                    'link': 'http://api.lomadee.com/v3/MEU_APP_TOKEN/category/_id/0?sourceId=MEU_SOURCE_ID',
                    'nome': None,
                    'quantidade_ofertas': None
                },
                'id': '00053604-00053604',
                'link': 'https://developer.lomadee.com/redir/validation/?sourceId=MEU_SOURCE_ID&appToken=MEU_APP_TOKEN',
                'loja': {
                    'comissao_maxima': None,
                    'eventos': [],
                    'id': 6064,
                    'link': 'https://developer.lomadee.com/redir/validation/?sourceId=MEU_SOURCE_ID&appToken=MEU_APP_TOKEN',
                    'nome': 'Rede Schumann',
                    'quantidade_ofertas': None,
                    'thumbnail': 'https://www.lomadee.com/programas/BR/6064/imagemBox_80x60.png'
                },
                'nome': 'Mouse Gamer Fortrek Black Hawk OM-703 7 Botões + Scroll – Preto/Azul',
                'parcelas': {
                    'quantidade': 1,
                    'valor': 36.9
                },
                'preco_atual': 33.94,
                'preco_original': 36.9,
                'thumbnail': 'http://d3alv7ekdacjys.cloudfront.net/Custom/Content/Products/10/69/1069594_mouse-gamer-fortrek-black-hawk-om-703-7-botoes-scroll-preto-azul_z1_637030130715854141'
            }
        ],
        'paginacao': {
            'pagina': 1,
            'quantidade': 2,
            'total_paginas': 679,
            'total_quantidade': 1358
        }
    }
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

    resposta = manipulador_requisicoes.get(endpoint, parametros)
    return padronizar_resposta_oferta(resposta)


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
    >>> resposta = lomapy.ofertas.obter_por_loja(5632, quantidade=2)
    >>> pprint(resposta)  # doctest: +NORMALIZE_WHITESPACE
    {
        'ofertas': [
            {
                'categoria': {
                    'id': 0,
                    'link': 'http://api.lomadee.com/v3/MEU_APP_TOKEN/category/_id/0?sourceId=MEU_SOURCE_ID',
                    'nome': None,
                    'quantidade_ofertas': None
                },
                'id': '100003411',
                'link': 'https://developer.lomadee.com/redir/validation/?sourceId=MEU_SOURCE_ID&appToken=MEU_APP_TOKEN',
                'loja': {
                    'comissao_maxima': None,
                    'eventos': [],
                    'id': 5632,
                    'link': 'https://developer.lomadee.com/redir/validation/?sourceId=MEU_SOURCE_ID&appToken=MEU_APP_TOKEN',
                    'nome': 'Americanas.com',
                    'quantidade_ofertas': None,
                    'thumbnail': 'https://www.lomadee.com/programas/BR/5632/imagemBox_80x60.png'
                },
                'nome': 'Caixa De Som Swarovski Bluetooth 15 Cristais Original',
                'parcelas': {'quantidade': 2, 'valor': 87.87},
                'preco_atual': 175.75,
                'preco_original': 175.75,
                'thumbnail': 'https://images-americanas.b2w.io/produtos/01/00/images/100003/4/100003410P1.jpg'
            },
            {
                'categoria': {
                    'id': 6458,
                    'link': 'http://api.lomadee.com/v3/MEU_APP_TOKEN/category/_id/6458?sourceId=MEU_SOURCE_ID',
                    'nome': None,
                    'quantidade_ofertas': None
                },
                'id': '100006135',
                'link': 'https://developer.lomadee.com/redir/validation/?sourceId=MEU_SOURCE_ID&appToken=MEU_APP_TOKEN',
                'loja': {
                    'comissao_maxima': None,
                    'eventos': [],
                    'id': 5632,
                    'link': 'https://developer.lomadee.com/redir/validation/?sourceId=MEU_SOURCE_ID&appToken=MEU_APP_TOKEN',
                    'nome': 'Americanas.com',
                    'quantidade_ofertas': None,
                    'thumbnail': 'https://www.lomadee.com/programas/BR/5632/imagemBox_80x60.png'
                },
                'nome': 'Caixa Amplificada Frahm Mf800 - Usb - Bt - Controle Remoto',
                'parcelas': {'quantidade': 7, 'valor': 145.7},
                'preco_atual': 1019.9,
                'preco_original': 1019.9,
                'thumbnail': 'https://images-americanas.b2w.io/produtos/01/00/images/100006/1/100006134P1.jpg'
            }
        ],
        'paginacao': {
            'pagina': 1,
            'quantidade': 2,
            'total_paginas': 92465,
            'total_quantidade': 184930
        }
    }
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

    resposta = manipulador_requisicoes.get(endpoint, parametros)
    return padronizar_resposta_oferta(resposta)
