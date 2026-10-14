"""Configuración clínica del módulo de triaje de enfermería.

Centro de Salud Vistahermosa · Consulta de Enfermería
Los umbrales los valida la Dirección Médica: no se cambian sin Pull Request.
"""

# --- Pacientes ---
# En Atención Primaria se atiende en Pediatría hasta los 14 años incluidos.
EDAD_MAXIMA_PEDIATRIA = 14

# --- Temperatura (ºC) ---
TEMP_HIPOTERMIA = 35.0
TEMP_FIEBRE = 38.0

# --- Frecuencia cardiaca (lpm, adulto en reposo) ---
FC_BRADICARDIA = 50
FC_TAQUICARDIA = 100

# --- Tensión arterial (mmHg) ---
TA_SISTOLICA_ALTA = 140
TA_DIASTOLICA_ALTA = 90

# --- Registro de triaje ---
CONSTANTES_OBLIGATORIAS = ["temperatura", "frecuencia_cardiaca", "tension"]
