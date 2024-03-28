# SPDX-License-Identifer: MIT

def procura_maior(lista):
    """Retorna o maior elemento de uma lista."""
    maior = lista[0]

    for item in lista[1:]:
        if item > maior:
            maior = item

    return maior

def procura_menor(lista):
    """Retorna o menor elemento de uma lista."""
    menor = lista[0]

    for item in lista[1:]:
        if item < menor:
            menor = item

    return menor

def procura_impares(lista):
    """Retorna os elementos ímpares de uma lista."""
    elementos_impares = []

    for item in lista:
        if item % 2 != 0:
            elementos_impares.append(item)

    return elementos_impares

def procura_pares(lista):
    """Retorna os elementos pares de uma lista."""
    elementos_pares = []

    for item in lista:
        if item % 2 == 0:
            elementos_pares.append(item)

    return elementos_pares
