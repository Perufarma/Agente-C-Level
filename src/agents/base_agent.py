"""Clase base compartida por todos los agentes ejecutivos (C-Level)."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class AgentConfig:
    name: str
    role: str
    system_prompt_path: Path
    model: str = field(default_factory=lambda: os.getenv("ANTHROPIC_MODEL", "claude-sonnet-5"))
    max_tokens: int = 2048
    temperature: float = 0.4


class BaseCLevelAgent:
    """Base para un agente ejecutivo respaldado por la API de Claude.

    El cliente de Anthropic se crea de forma perezosa (solo cuando se
    necesita) para que instanciar un agente no requiera tener el paquete
    `anthropic` instalado ni una API key configurada, por ejemplo en tests
    donde se inyecta un cliente falso.
    """

    def __init__(self, config: AgentConfig, client: Any | None = None):
        self.config = config
        self.client = client
        self.system_prompt = config.system_prompt_path.read_text(encoding="utf-8")
        self.history: list[dict[str, str]] = []

    def _get_client(self) -> Any:
        if self.client is None:
            from anthropic import Anthropic

            self.client = Anthropic()
        return self.client

    def ask(self, message: str) -> str:
        self.history.append({"role": "user", "content": message})

        response = self._get_client().messages.create(
            model=self.config.model,
            max_tokens=self.config.max_tokens,
            temperature=self.config.temperature,
            system=self.system_prompt,
            messages=self.history,
        )

        reply = "".join(
            block.text for block in response.content if getattr(block, "type", None) == "text"
        )
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def reset(self) -> None:
        self.history.clear()
