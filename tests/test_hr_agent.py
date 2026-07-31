import sys
import unittest
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.agents.hr_agent.agent import HRAgent  # noqa: E402
from src.agents.registry import create_agent  # noqa: E402


class _FakeMessages:
    def __init__(self, reply_text: str):
        self._reply_text = reply_text

    def create(self, **kwargs):
        return SimpleNamespace(
            content=[SimpleNamespace(type="text", text=self._reply_text)]
        )


class _FakeClient:
    def __init__(self, reply_text: str = "Respuesta simulada de RRHH"):
        self.messages = _FakeMessages(reply_text)


class HRAgentTests(unittest.TestCase):
    def test_responds_and_tracks_history(self):
        agent = HRAgent(client=_FakeClient())

        reply = agent.ask("¿Cómo estructuro un proceso de selección para un gerente de planta?")

        self.assertEqual(reply, "Respuesta simulada de RRHH")
        self.assertEqual(agent.history[0]["role"], "user")
        self.assertEqual(agent.history[1]["content"], "Respuesta simulada de RRHH")
        self.assertEqual(agent.config.role, "CHRO")

    def test_reset_clears_history(self):
        agent = HRAgent(client=_FakeClient())
        agent.ask("Hola")
        agent.reset()
        self.assertEqual(agent.history, [])

    def test_system_prompt_loaded(self):
        agent = HRAgent(client=_FakeClient())
        self.assertIn("Reclutamiento y selección", agent.system_prompt)
        self.assertIn("Clima laboral", agent.system_prompt)
        self.assertIn("Compensaciones y beneficios", agent.system_prompt)
        self.assertIn("Onboarding y offboarding", agent.system_prompt)
        self.assertIn("People analytics y planificación de talento", agent.system_prompt)
        self.assertIn("Seguridad y salud en el trabajo", agent.system_prompt)
        self.assertIn("Seguridad patrimonial", agent.system_prompt)
        self.assertIn("Productividad", agent.system_prompt)

    def test_registry_creates_hr_agent(self):
        agent = create_agent("hr")
        self.assertIsInstance(agent, HRAgent)

    def test_registry_raises_for_unknown_agent(self):
        with self.assertRaises(ValueError):
            create_agent("cfo")


if __name__ == "__main__":
    unittest.main()
