# SPDX-License-Identifer: MIT

"""Implementação do exercício zero."""


def procura_maior(lista):
    """Procura maior item na lista usando procura linear."""
    maior = lista[0]
    for item in lista[1:]:
        if item > maior:
            maior = item
    return maior
