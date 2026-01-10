from langgraph.graph import StateGraph, END
from src.graph.state import AgentState
from src.agents.generator_agent import GeneratorAgent
from src.agents.validator_agent import ValidatorAgent

def build_graph():
    generator = GeneratorAgent()
    validator = ValidatorAgent()

    graph = StateGraph(AgentState)

    graph.add_node("generate", generator.run)
    graph.add_node("validate", validator.run)

    graph.set_entry_point("generate")
    graph.add_edge("generate", "validate")
    graph.add_edge("validate", END)

    return graph.compile()
