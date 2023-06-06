# Manipulação de arquivos
Em certos momentos precisamos armazenar ou ler dados para serem reutilizados na próxima vez que executarmos nosso programa. Uma forma disso é usando a manipulação de arquivos.

## Como posso fazer isso ?
Existem duas formas de se fazer isso, mas você precisa aprender a primeira para usar a segunda !

### Primeira
```python
# caminho arquivo / modo de manipulação
arquivo = open("arquivo.txt", "r")

# instruções do código

# nunca esqueça de fechar o arquivo
arquivo.close()
```
Os modos de manipulação são:
- r - Apenas leitura.
- w - Apenas escrita, sobreescrevendo todo conteúdo já armazenado.
- a - Apenas escrita, adicionando um novo conteúdo e preservando o anterior.

Para cada modo existem comandos específicos. Se você quiser usar um comando de outro modo ele lhe retornará um erro.

### Segunda
```python
with open("arquivo.txt", "r") as arquivo:
    # instruções do código
```

Dessa forma não precisamos dizer para ele fechar o arquivo, pois o comando `with` já faz isso após o fim do nosso bloco de código.<br>
Esse comando nos da liberdade de usar outras lógicas para nossos códigos, e é muito provável de encontrarem ele em algum código na internet.

## Qual usar ?
As duas formas fazem exatamente a mesma coisa, e quem decide qual usar é você ! Mas não quer dizer que você não irá usar, pois existem vantagens e desvantagens.<br>
A vantagem da primeira é a facilidade da leitura, mas corre risco de não fechar o arquivo.
Já a segunda, esse risco diminui pois acontece de forma automática, e você economiza uma linha de código.

## Comandos
- `.read()` - Retorna todo o conteúdo do arquivo.
- `.readline()` - A cada vez que chamar essa função, ele retorna a próxima linha do arquivo.
- `.readlines()` - Retonar todas as linhas separadas em uma lista.
- `.write()` - Escreve um conteúdo no arquivo.
- `.writelines(lista)` - Escreve uma lista de conteúdos no arquivo.

### Exemplos
```python
# Escrita de conteúdo
with open("arquivo.txt", "a") as arquivo:
    arquivo.write("Olá mundo")
```

```python
# Leitura de conteúdo
with open("arquivo.txt", "a") as arquivo:
    linhas = arquivo.readlines()
    print(linhas)
```