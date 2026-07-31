"""Registro central de agentes C-Level disponibles."""

from __future__ import annotations

from .base_agent import BaseCLevelAgent
from .hr_agent.agent import HRAgent

AGENT_REGISTRY: dict[str, type[BaseCLevelAgent]] = {
    "hr": HRAgent,
}


def create_agent(agent_key: str) -> BaseCLevelAgent:
    try:
        agent_cls = AGENT_REGISTRY[agent_key]
    except KeyError as exc:
        available = ", ".join(sorted(AGENT_REGISTRY))
        raise ValueError(f"Agente '{agent_key}' no existe. Disponibles: {available}") from exc
    return agent_cls()
