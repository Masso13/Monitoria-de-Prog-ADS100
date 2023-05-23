# For
No python podemos usar o comando `for` para percorrer uma lista, sendo ela um `dicionario`, `tupla` ou `lista simples`. Nesse caso o `for` é um loop com limite.

Digamos que temos uma lista de idades
```python
idades = [18, 18, 19, 18, 19, 19, 20, 20, 20, 21, 25, 27, 22]
```

Você pode percorrer essa lista usando duas formas no `for`:
```python
# Da forma intuitiva
for idade in idades:
    print(idade)

# E da forma não muito agradável
for i in range(len(idades)):
    print(idades[i])
```

# While
No python podemos criar um loop infinito usando o comando `while`. O limite dele é dado por uma condição ou através do comando `break` dentro dele.

```python
numero = 0

while numero < 5:
    print(numero)

    # Aqui eu crio uma condição para forçar o loop parar.
    if numero == 3: 
        break

    numero+=1
```
O resultado da variável `numero` será a soma do resultado anterior com +1.