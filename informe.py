"""Genera el informe de triaje que ve el médico al abrir la cita."""

from datetime import date

import config
from constantes import (
    calcular_edad,
    clasificar_frecuencia_cardiaca,
    clasificar_temperatura,
    clasificar_tension,
    es_pediatrico,
)


def generar_informe(paciente, mediciones, hoy=None):
    """Devuelve el informe de triaje como texto."""
    edad = calcular_edad(paciente["fecha_nacimiento"], hoy)
    if es_pediatrico(paciente["fecha_nacimiento"], hoy):
        servicio = "Pediatría"
    else:
        servicio = "Medicina de Familia"

    lineas = [
        "=== INFORME DE TRIAJE ===",
        f"Paciente: {paciente['nombre']} (NHC {paciente['nhc']})",
        f"Edad: {edad} años · Derivar a: {servicio}",
    ]

    if "temperatura" in mediciones:
        t = mediciones["temperatura"]
        lineas.append(f"Temperatura: {t} → {clasificar_temperatura(t)}")
    if "frecuencia_cardiaca" in mediciones:
        fc = mediciones["frecuencia_cardiaca"]
        lineas.append(f"Frecuencia cardiaca: {fc} → {clasificar_frecuencia_cardiaca(fc)}")
    if "tension" in mediciones:
        sis, dia = mediciones["tension"]
        lineas.append(f"Tensión arterial: {sis}/{dia} → {clasificar_tension(sis, dia)}")

    faltan = [c for c in config.CONSTANTES_OBLIGATORIAS if c not in mediciones]
    if faltan:
        lineas.append("Faltan constantes obligatorias: " + ", ".join(faltan))

    return "\n".join(lineas)


if __name__ == "__main__":
    # Datos SINTÉTICOS: nunca se suben datos reales de pacientes a un repositorio.
    paciente = {
        "nombre": "Paciente Prueba 001",
        "nhc": "SINT-0001",
        "fecha_nacimiento": date(2011, 11, 20),
    }
    mediciones = {
        "temperatura": 38.4,
        "frecuencia_cardiaca": 112,
        "tension": (128, 82),
    }
    # Fecha fija para que el informe sea reproducible en clase.
    print(generar_informe(paciente, mediciones, hoy=date(2026, 10, 13)))
