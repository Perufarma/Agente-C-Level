"""Agente Senior de Recursos Humanos (CHRO)."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from ..base_agent import AgentConfig, BaseCLevelAgent

SYSTEM_PROMPT_PATH = Path(__file__).parent / "system_prompt.md"


class HRAgent(BaseCLevelAgent):
    """Chief Human Resources Officer senior: reclutamiento, políticas y
    cumplimiento, desempeño y desarrollo, clima laboral, compensaciones y
    beneficios, onboarding/offboarding, people analytics, seguridad y salud
    en el trabajo, seguridad patrimonial, y productividad."""

    def __init__(self, client: Any | None = None):
        config = AgentConfig(
            name="Agente Senior de Recursos Humanos",
            role="CHRO",
            system_prompt_path=SYSTEM_PROMPT_PATH,
        )
        super().__init__(config, client=client)
