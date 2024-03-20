# SPDX-License-Identifer: MIT

# language: pt
Funcionalidade: Realiza operações sobre listas

@peso:2
Cenário: Procura o maior elemento em uma lista
  Dada uma lista arbitrária
  Quando procuro o maior elemento na lista
  Então o resultado é o maior elemento da lista


Cenário: Procura o menor elemento em uma lista
  Dada uma lista arbitrária
  Quando procuro o menor elemento na lista
  Então o resultado é o menor elemento da lista


Cenário: Procura todos os elementos ímpares em uma lista
  Dada uma lista arbitrária
  Quando procuro os elementos ímpares em uma lista
  Então o resultado contém todos os elementos ímpares da lista e apenas os elementos ímpares


Cenário: Procura todos os elementos pares em uma lista
  Dada uma lista arbitrária
  Quando procuro os elementos pares em uma lista
  Então o resultado contém todos os elementos pares da lista e apenas os elementos pares
