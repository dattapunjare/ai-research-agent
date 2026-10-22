from typing import TypedDict


class ResearchState(TypedDict):
    topic: str
    research_questions: list[str]
    research_results: list[dict]
    review_feedback: str
    review_count: int
    final_report: str
    approved: bool