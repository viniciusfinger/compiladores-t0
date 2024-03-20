Instruções para a realização do exercício
=========================================

**Prazo máximo para a entrega do exercício: 27/03/2024**

Objetivos
---------

O objetivo desse exercício é praticar o uso do Git e do Github, e entender
como será realizada a avaliação dos trabalhos de implementação da disciplina
de Compiladores.

Objetivos secundários do exercício é familiarizar o aluno com ferramentas de
automação de testes da linguagem Python, como o `tox` e o `behave`.


Instruções
----------

O primeiro passo é realizar um _fork_ do projeto no
[Github](https://github.com/exercicios-programacao/compiladores-t0), para o
seu usuário. Esse passo irá criar um repositório do seu usuário que pode ser
utilizado para o desenvolvimento do trabalho.

Após, você deverá obter uma cópia local do projeto, utilizando o `git`:

```
git clone https://github.com/<seu_usuario>/compiladores-t0
```

A partir dessa cópia local você irá implementar o código que falta para que
os testes existentes completem com sucesso.

Para executar os testes, utilize o comando `behave`. (Veja como preparar o
ambiente de desenvolvimento no arquivo [README.md](README.md)).

Uma vez que os testes executam corretamente, você pode verificar outras
métricas de qualidade de código, executando programas como `flake8`,
`pylint` ou `pydocstyle`. Estes programas fazem verificação de boas práticas
de codificação na linguagem Python.

A forma mais simples de executar todos os comandos é utilizando o programa
`tox`, que foi configurado neste projeto para executar tanto os testes de
avaliação do código, como os testes de verificação.

```
tox
```

Para executar apenas os testes de boas práticas de codificação, execute:

```
tox -e lint
```

Uma vez que você está satisfeito com os resultados (mesmo que sejam ainda
resultados parciais), você pode _commitar_, localmente, seu trabalho:

```
git add <arquivos_novos_ou_modificados>
git commit
```

Para verificar a avaliação oficial, você precisará criar um
_pull request_. Para isso deve, primeiro, enviar seu trabalho para o seu
repositório no Github:

```
git pull
```

Nesse caso, se executado na linha de comando, o git irá mostrar um link
para criar o _pull request_ contra o repositório original. Basta completar
as informações e criar o _pull request_, que a avaliação oficial será
executada e pode ser acompanhada na aba _Checks_.

Entre as informações que você precisa preencher estão:

* Nome completo do aluno no _título_ do _pull request_.
* Citar quais foram suas dificuldades no campo de texto do _pull request_.

Caso você não utilize a linha de comando o processo de criação do
_pull request_ deve ser realizado pelo Github, ou utilizando as ferramentas
do seu ambiente de desenvolvimento escolhido.


Tarefas
-------

Você deve completar o código de forma a passar nos testes automatizados.
Para isso, você precisa implementar, no módulo `zero`, os métodos:

* `procura_maior(dados: list) -> int`
    : Retorna o inteiro com o maior valor, presente na lista.
* `procura_menor(dados: list) -> int`
    : Retorna o inteiro com o menor valor, presente na lista.
* `procura_impares(dados: list) -> list`
    : Retorna a lista de elementos ímpares, presentes na lista.
* `procura_pares(dados: list) -> list`
    : Retorna a lista de elementos pares, presentes na lista.

Como exemplo, parte do trabalho já foi realizado, e foi incluida a
implementação do método `procura_maior(dados: list) -> int`.


Importante
----------

* A nota final do trabalho será atribuída pelo professor, baseado na nota
da avaliação automática, de acordo com o resultado disponível na data de
entrega do trabalho. Um comentário irá marcar o número (_hash_) do _commit_
utilizado para a avaliação.

* Sempre que você alterar o estado do _branch_ que você utilizou para criar
o _pull request_, a avaliação será executada novamente, logo, você pode
utilizar essa característica para acompanhar o seu desenvolvimento.

* Para este trabalho, apenas o arquivo `src/zero.py` pode ser alterado.

* O resultado desse exercício não fará parte da nota do grau.


Sobre a Avaliação
-----------------

Ao requisitar o _pull request_ uma série de testes serão executados e uma
indicação da nota obtida no trabalho será fornecida. Note que esta nota pode
aumentar ou diminuir dependendo de outros fatores, como falhas nos testes de
qualidade de código, que diminuiriam a nota, ou soluções criativas e/ou
elegantes, que aumentariam a nota.

> **IMPORTANTE:** não é permitida a alteração de **nenhum** arquivo fora do
diretório `src`. Caso você queira adicionar mais testes, crie novos
arquivos no diretório `features`, mas não modifique os arquivos existentes.

