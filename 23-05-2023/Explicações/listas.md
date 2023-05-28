# Como armazenar dados ?
No python podemos armazenar dados de diversas formas. E o uso de listas, tuplas e dicionários

## Listas
As listas são uma forma de armazenar os dados, manipula-los e deleta-los. Usa-se os `[ ]` para se determinar uma lista.

```python
idades = [18, 18, 19, 18, 19, 19, 20, 20, 20, 21, 25, 27, 22]

# Aqui irá mudar o primeiro valor.
idades[0] = 19
```

## Tuplas
As tuplas apenas armazenam dados pré-definidos, não permitindo a alteração. Usa-se os `( )` para se determinar uma tupla.
```python
idades = (18, 18, 19, 18, 19, 19, 20, 20, 20, 21, 25, 27, 22)

# Aqui irá dar erro pois a tupla não permite mudança de valores.
idades[0] = 19
```

## Dicionários
Os dicionários são usados para armazenar os dados de forma mais estruturada. Usa-se `{ }` para definir o dicionário, e identificando cada `dado` com uma `chave`.

```python
# Forma básica
pessoas = {
    "Arthur": 19,
    "Luiz": 18,
    "Duda": 20,
    "Arthie": 21
}

# Ou assim também (Mas recomendado nesse exemplo)
pessoas = [
    {"nome": "Arthur", "idade": 19},
    {"nome": "Luiz", "idade": 18},
    {"nome": "Duda", "idade": 20},
    {"nome": "Arthie", "idade": 21},
]
```
