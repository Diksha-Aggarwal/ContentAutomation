from src.agents.base_agent import BaseAgent
from src.graph.state import AgentState
from src.llm.llm_loader import OpenSourceLLM
from src.llm.prompts import VALIDATOR_PROMPT
from src.utils.device import resolve_device
from src.utils.config_loader import load_yaml


class ValidatorAgent(BaseAgent):
    name = "ValidatorAgent"

    def __init__(self):
        cfg = load_yaml("configs/models.yaml")["validator"]
        device = resolve_device(cfg["device"])

        self.llm = OpenSourceLLM(
            model_name=cfg["model_name"],
            device=device,
            max_new_tokens=cfg["max_new_tokens"],
        )

    def run(self, state: AgentState) -> AgentState:
        self.log(state, "Validating summary using LLM")

        prompt = VALIDATOR_PROMPT.format(summary=state.summary)

        output = self.llm.generate(prompt)

        # Simple parsing (improve later)
        state.validation_score = 0.9
        state.validation_feedback = output.strip()

        return state
