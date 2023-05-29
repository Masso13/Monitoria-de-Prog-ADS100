# Funções
Na programação existe momentos que acabamos repitindo muita linha de código. Para evitar isso foi criado as funções, que nos ajudam a reutilizar nosso próprio código.

No python usamos o comando `def` para criar uma função. Em seguida o `nome` da mesma e seus `parâmetros`.

```python
def quadratica(x):
    return x**2

print(quadratica(5))
print(quadratica(2))
```

Outro exemplo

```python
def pegarDadosPessoa(nome, pessoas):
    for pessoa in pessoas:
        if pessoa["nome"] == nome:
            break
    return pessoa

pessoas = [
    {"nome": "Arthur", "idade": 19},
    {"nome": "Luiz", "idade": 18},
    {"nome": "Duda", "idade": 20},
    {"nome": "Arthie", "idade": 21},
]

dados1 = pegarDadosPessoa("Duda", pessoas)
dados2 = pegarDadosPessoa("Arthie", pessoas)

print(dados1)
print(dados2)
```