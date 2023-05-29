# Por que aprender ?
Os módulos e bibliotecas nos ajudam a organizar o nosso código, e deixá-lo mais agradável na leitura e no entendimento do mesmo. Assim determinamos o que cada arquivo terá, e será mais fácil de localizar os elementos.

# Módulos
## O que é ?
É um conjunto de funções que serão reutilizadas.

## Como criar ?
Basta criar um arquivo com formato `.py` e coloca-las lá.

```python
# basicos.py
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b
```

```python
# main.py
import basicos

resultado = basicos.soma(5, 5)

# ou

from basicos import soma

resultado = soma(5, 5)
```

# Biblioteca
## O que é ?
É um conjunto de módulos criados para serem reutilizados.

## Como criar ?
Primeiro crie uma pasta com o nome da sua biblioteca. Exemplo: `biblioteca`

Dentro dela crie o arquivo `__init__.py`. Ele serve como um módulo inicial para quando você importar a biblioteca.
```python
# biblioteca/__init__.py
def media(valores):
    soma = sum(valores)
    media = soma / len(valores)
    return media
```

```python
# main.py

import biblioteca

biblioteca.media()

# ou

from biblioteca import media

media()
```

Dentro dessa pasta `biblioteca` você pode colocar outros arquivos (módulos).
```python
# biblioteca/basicos.py
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b
```

```python
# main.py
from biblioteca import basicos

basicos.multiplicacao()

# ou

from biblioteca.basicos import multiplicacao

multiplicacao()
```