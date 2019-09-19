# Lomapy

[![Version](https://img.shields.io/pypi/v/lomapy.svg?style=flat)](https://pypi.python.org/pypi/lomapy)
[![Python Version](https://img.shields.io/pypi/pyversions/lomapy?style=flat)](https://pypi.python.org/pypi/lomapy)
[![License](https://img.shields.io/github/license/AlanTaranti/Lomapy)](LICENSE)
## O que é esse o projeto?

É uma biblioteca **não oficial** que disponibiliza um interface em python para a API de Afiliados do Lomadee.
O Lomapy é compatível com versão 3 da API da Lomadee.

## Como instalar e utilizar esse projeto? 

### Instalação
    
    $ pip install lomapy

### Utilização

*Não possui um APP_TOKEN ou SOURCE_ID? Consulte a documentação da [Lomadee](https://developer.lomadee.com/).*

    >>> import lomapy
    >>>
    >>> app_token = {SEU_APP_TOKEN_AQUI}
    >>> source_id = {SEU_SOURCE_ID_AQUI}
    >>>
    >>> lomapy.autenticar(app_token, source_id)
    >>>
    >>> lomapy.categorias.obter_todas()
    
#### Métodos suportados

- Ofertas - 100%
  - categorias 
    - buscar()
    - obter_todas()
    - obter_por_id()
  - lojas
    - obter_todas()
  - ofertas
    - obter_por_categoria()
    - obter_por_id()
    - buscar()
    - obter_por_loja()
    
- Cupons - 0%
  - ~~categorias~~
    - ~~obter_todos()~~
  - ~~lojas~~
    - ~~obter_todas()~~
  - ~~cupons~~
    - ~~obter_todos()~~
    - ~~obter_por_id()~~

- Deeplink - 0%
   - ~~criar deeplink~~

## Como eu entro em contato?
* Email: [alan.taranti@gmail.com](mailto:alan.taranti@gmail.com)
* Website: <a href="http://alantaranti.github.io" target="_blank">alantaranti.github.io</a>
