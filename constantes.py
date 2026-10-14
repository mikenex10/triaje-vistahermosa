"""Clasificación de constantes vitales tomadas en la consulta de enfermería."""

from datetime import date

import config


def calcular_edad(fecha_nacimiento, hoy=None):
    """Devuelve la edad del paciente en años cumplidos."""
    if hoy is None:
        hoy = date.today()
    return hoy.year - fecha_nacimiento.year


def es_pediatrico(fecha_nacimiento, hoy=None):
    """True si el paciente debe atenderse en Pediatría."""
    return calcular_edad(fecha_nacimiento, hoy) <= config.EDAD_MAXIMA_PEDIATRIA


def clasificar_temperatura(temperatura):
    """Clasifica la temperatura axilar en ºC."""
    if temperatura < config.TEMP_HIPOTERMIA:
        return "hipotermia"
    if temperatura >= config.TEMP_FIEBRE:
        return "fiebre"
    return "normal"


def clasificar_frecuencia_cardiaca(fc):
    """Clasifica la frecuencia cardiaca en latidos por minuto."""
    if fc < config.FC_BRADICARDIA:
        return "bradicardia"
    if fc > config.FC_TAQUICARDIA:
        return "taquicardia"
    return "normal"


def clasificar_tension(sistolica, diastolica):
    """Clasifica la tensión arterial (mmHg)."""
    if sistolica >= config.TA_SISTOLICA_ALTA or diastolica >= config.TA_DIASTOLICA_ALTA:
        return "hipertension"
    if sistolica < 90 or diastolica < 60:
        return "hipotension"
    return "normal"
