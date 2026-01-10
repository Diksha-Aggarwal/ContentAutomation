from src.agents.base_agent import BaseAgent
from src.graph.state import AgentState
from src.llm.llm_loader import OpenSourceLLM
from src.llm.prompts import GENERATOR_PROMPT
from src.utils.device import resolve_device
from src.utils.config_loader import load_yaml


class GeneratorAgent(BaseAgent):
    name = "GeneratorAgent"

    def __init__(self):
        cfg = load_yaml("configs/models.yaml")["generator"]
        device = resolve_device(cfg["device"])

        self.llm = OpenSourceLLM(
            model_name=cfg["model_name"],
            device=device,
            max_new_tokens=cfg["max_new_tokens"],
        )

    def run(self, state: AgentState) -> AgentState:
        self.log(state, "Generating summary using LLM")

        # Demo sources
        sources_text = """
        - Open-source LLM adoption is increasing
        - Multi-agent systems are gaining popularity
        - Observability is becoming critical in AI systems
        """

        prompt = GENERATOR_PROMPT.format(sources=sources_text)

        output = self.llm.generate(prompt)

        # Extract only summary part
        state.summary = output.split("Summary:")[-1].strip()

        return state
