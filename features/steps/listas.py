# SPDX-License-Identifer: MIT

"""Implementação dos testes para listas."""

from random import randint

from behave import given, when, then  # pylint: disable=no-name-in-module
from common_test import (
    import_module_error,
    import_function_error_message,
    expected_observed_mismatch,
)

try:
    import zero
except ImportError as imperr:
    import_module_error(imperr.name)


def __assert_def(function_name):
    assert hasattr(zero, function_name), import_function_error_message(
        zero.__name__, function_name
    )


@given("uma lista arbitrária")
def _cria_lista(context):
    context.lista = [randint(1, 1000) for _ in range(randint(1, 100))]


@when("procuro o maior elemento na lista")
def _procura_maior_elemento(context):
    __assert_def("procura_maior")
    context.result = zero.procura_maior(context.lista)


@then("o resultado é o maior elemento da lista")
def _compara_resultado_maior_elemento(context):
    expected = max(context.lista)
    assert context.result == expected, expected_observed_mismatch(
        expected, context.result
    )


@when("procuro o menor elemento na lista")
def _procura_menor_elemento(context):
    __assert_def("procura_menor")
    context.result = zero.procura_menor(context.lista)


@then("o resultado é o menor elemento da lista")
def _compara_resultado_menor_elemento(context):
    expected = min(context.lista)
    assert context.result == expected, expected_observed_mismatch(
        expected, context.result
    )


@when("procuro os elementos ímpares em uma lista")
def _procura_elementos_impares(context):
    __assert_def("procura_impares")
    context.result = zero.procura_impares(context.lista)


@then(
    "o resultado contém todos os elementos ímpares da lista "
    "e apenas os elementos ímpares"
)
def _compara_resultado_elementos_impares(context):
    expected = [item for item in context.lista if item % 2 == 1]
    assert context.result == expected, expected_observed_mismatch(
        expected, context.result
    )


@when("procuro os elementos pares em uma lista")
def _procura_elementos_pares(context):
    __assert_def("procura_pares")
    context.result = zero.procura_pares(context.lista)


@then(
    "o resultado contém todos os elementos pares da lista "
    "e apenas os elementos pares"
)
def _compara_elementos_pares(context):
    expected = [item for item in context.lista if item % 2 == 0]
    assert context.result == expected, expected_observed_mismatch(
        expected, context.result
    )
