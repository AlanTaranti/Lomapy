# Criar nova release

- 1 - Executar as modificações desejadas

- 2 - Executar os testes. *Configurações do ambiente de testes em [TESTANDO](TESTANDO.md)*

        $ pyenv local 3.5.7 3.6.9
        $ tox
        
- 3 - Alterar a versão do Lomapy em [sdk](lomapy/recursos/sdk/sdk.py)
    
- 4 - Subir alterações

        $ git push
        
- 5 - Compilar codigo

        $ python setup.py sdist bdist_wheel
    
- 6 - Submeter ao PyPI

        $  twine upload --repository pypi dist/*
