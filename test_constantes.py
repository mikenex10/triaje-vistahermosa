"""Tests unitarios del módulo de triaje. Ejecutar con: pytest"""

from datetime import date

import config
from constantes import (
    calcular_edad,
    clasificar_frecuencia_cardiaca,
    clasificar_temperatura,
    clasificar_tension,
    es_pediatrico,
)

HOY = date(2026, 10, 13)


def test_calcular_edad():
    assert calcular_edad(date(1980, 3, 15), hoy=HOY) == 46


def test_es_pediatrico():
    assert es_pediatrico(date(2020, 1, 10), hoy=HOY)
    assert not es_pediatrico(date(1990, 5, 2), hoy=HOY)


def test_clasificar_temperatura():
    assert clasificar_temperatura(34.5) == "hipotermia"
    assert clasificar_temperatura(36.8) == "normal"
    assert clasificar_temperatura(38.0) == "fiebre"


def test_clasificar_frecuencia_cardiaca():
    assert clasificar_frecuencia_cardiaca(45) == "bradicardia"
    assert clasificar_frecuencia_cardiaca(72) == "normal"
    assert clasificar_frecuencia_cardiaca(115) == "taquicardia"


def test_clasificar_tension():
    assert clasificar_tension(config.TA_SISTOLICA_ALTA, 70) == "hipertension"
    assert clasificar_tension(110, config.TA_DIASTOLICA_ALTA) == "hipertension"
    assert clasificar_tension(config.TA_SISTOLICA_ALTA - 1, config.TA_DIASTOLICA_ALTA - 1) == "normal"
    assert clasificar_tension(85, 55) == "hipotension"
