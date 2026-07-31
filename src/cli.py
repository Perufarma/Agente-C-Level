"""CLI simple para chatear con un agente C-Level desde la terminal."""

from __future__ import annotations

import argparse

from .agents.registry import create_agent


def main() -> None:
    parser = argparse.ArgumentParser(description="Chatea con un agente C-Level.")
    parser.add_argument("--agent", default="hr", help="Clave del agente a usar (ej: hr)")
    args = parser.parse_args()

    agent = create_agent(args.agent)
    print(f"Hablando con: {agent.config.name} ({agent.config.role}). Escribe 'salir' para terminar.\n")

    while True:
        try:
            message = input("Tú: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if message.lower() in {"salir", "exit", "quit"}:
            break
        if not message:
            continue

        reply = agent.ask(message)
        print(f"\n{agent.config.name}: {reply}\n")


if __name__ == "__main__":
    main()
