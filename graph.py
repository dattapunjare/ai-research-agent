
from langgraph.graph import StateGraph, START, END

from state import ResearchState
from agents.planner import plan_research
from agents.researcher import research_question
from agents.reviewer import review_research
from agents.writer import write_report


def planner_node(state: ResearchState) -> dict:
    """Create research questions for the topic."""
    questions = plan_research(state["topic"])

    return {
        "research_questions": questions,
        "research_results": [],
        "review_feedback": "",
        "review_count": 0,
        "approved": False,
    }


def researcher_node(state: ResearchState) -> dict:
    """Research each question."""
    results = [
        research_question(question)
        for question in state["research_questions"]
    ]

    return {"research_results": results}


def reviewer_node(state: ResearchState) -> dict:
    """Review the collected research."""
    review = review_research(state["research_results"])

    return {
        "approved": review["approved"],
        "review_feedback": review["feedback"],
        "review_count": state.get("review_count", 0) + 1,
    }


def writer_node(state: ResearchState) -> dict:
    """Write the final report."""
    report = write_report(
        state["topic"],
        state["research_results"],
    )

    return {"final_report": report}


def route_after_review(state: ResearchState) -> str:
    """Choose whether to write the report or research again."""
    if state["approved"]:
        return "writer"

    if state["review_count"] >= 2:
        return "writer"

    return "researcher"


builder = StateGraph(ResearchState)

builder.add_node("planner", planner_node)
builder.add_node("researcher", researcher_node)
builder.add_node("reviewer", reviewer_node)
builder.add_node("writer", writer_node)

builder.add_edge(START, "planner")
builder.add_edge("planner", "researcher")
builder.add_edge("researcher", "reviewer")

builder.add_conditional_edges(
    "reviewer",
    route_after_review,
    {
        "writer": "writer",
        "researcher": "researcher",
    },
)

builder.add_edge("writer", END)

research_graph = builder.compile()

