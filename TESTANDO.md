# Executando os Testes

## 1 - Instalar as dependências do projeto

    $ pip install -r requirements-dev
    
## 2 - Instalar as dependências globais

### 2.1 - Instalar o pyenv
O pyenv permite alternar facilmente entre várias versões do Python.

Maiores informações podem ser obtidas em [pyenv](https://github.com/pyenv/pyenv) e [pyenv-instaler](https://github.com/pyenv/pyenv-installer)

    $ curl https://pyenv.run | bash

### 2.2 - Instalar as dependências de compilação dos interpretadores Python
Para compilar o python, o pyenv precisa de algumas bibliotecas.

Maiores informações por ser obtidas na [wiki do pyenv](https://github.com/pyenv/pyenv/wiki#suggested-build-environment)

#### 2.2.1 - Ubuntu/Debian/Mint

    $ sudo apt-get update
    $ sudo apt-get install --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
    
#### 2.2.2 - Demais distribuições

- Consulte a [Wiki do pyenv](https://github.com/pyenv/pyenv/wiki#suggested-build-environment)

## 2.3 - Instalar os interpretadores

    $ pyenv install 3.5.7
    $ pyenv install 3.6.9
    $ pyenv install 3.7.4
    
## 3 - Definir as chaves da API
Copie o arquivo ".env.exemplo" para ".env" e edite as variáveis de ambientes relacionadas às chaves da API

    $ cp .env.exemplo .env
    
## 4 - Executar os testes
    $ pyenv local 3.5.7 3.6.9 3.7.4
    $ tox
