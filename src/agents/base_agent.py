from abc import ABC, abstractmethod
from src.graph.state import AgentState

class BaseAgent(ABC):
    name: str

    def log(self, state: AgentState, message: str):
        state.logs.append(f"[{self.name}] {message}")
        return state

    @abstractmethod
    def run(self, state: AgentState) -> AgentState:
        pass
