import uuid
from rich import print

from src.graph.state import AgentState
from src.graph.graph_builder import build_graph


def main():
    app = build_graph()

    initial_state = AgentState(
        run_id=str(uuid.uuid4()),
        mode="demo"
    )

    # LangGraph returns dict
    final_state_dict = app.invoke(initial_state)

    # Convert dict back to AgentState
    final_state = AgentState(**final_state_dict)

    print("\n[bold green]=== DEMO RUN COMPLETE ===[/bold green]\n")

    print("[bold]Summary:[/bold]")
    print(final_state.summary)

    print("\n[bold]Validation:[/bold]")
    print(f"Score: {final_state.validation_score}")
    print(f"Feedback: {final_state.validation_feedback}")

    print("\n[bold]Logs:[/bold]")
    for log in final_state.logs:
        print(log)


if __name__ == "__main__":
    main()
