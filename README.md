# Agente C-Level

Framework para construir agentes de IA que representan roles ejecutivos
(C-Level) de la organización, impulsados por la API de Claude (Anthropic).

Cada agente tiene un rol, un prompt de sistema y un historial de conversación
propios, pero comparte una base común (`BaseCLevelAgent`) para que agregar un
nuevo rol ejecutivo sea simple y consistente.

## Estructura

```
src/
├── agents/
│   ├── base_agent.py      # Clase base compartida por todos los agentes C-Level
│   ├── registry.py        # Registro de agentes disponibles (clave -> clase)
│   └── hr_agent/          # Agente Senior de RRHH (CHRO)
│       ├── agent.py
│       └── system_prompt.md
└── cli.py                 # CLI simple para chatear con un agente
tests/
└── test_hr_agent.py
```

## Agente disponible: RRHH / CHRO

El `HRAgent` actúa como un Chief Human Resources Officer senior, cubriendo:

- Reclutamiento y selección
- Políticas y cumplimiento laboral
- Gestión del desempeño y desarrollo
- Clima laboral y relaciones con empleados
- Compensaciones y beneficios
- Onboarding y offboarding
- People analytics y planificación de talento
- Seguridad y salud en el trabajo (SST)
- Seguridad patrimonial
- Productividad

Su rol y estilo de respuesta están definidos en
`src/agents/hr_agent/system_prompt.md`.

## Cómo agregar un nuevo agente C-Level (CFO, CTO, CMO, ...)

1. Crear una carpeta `src/agents/<rol>_agent/` con `agent.py` y
   `system_prompt.md`.
2. En `agent.py`, crear una subclase de `BaseCLevelAgent` que apunte a su
   propio `system_prompt.md` (ver `hr_agent/agent.py` como referencia).
3. Registrar la nueva clase en `src/agents/registry.py`.

## Instalación

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # y completar ANTHROPIC_API_KEY
```

## Uso

```bash
python -m src.cli --agent hr
```

## Tests

```bash
python -m unittest discover -s tests
```
