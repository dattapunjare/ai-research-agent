
from llm import llm


def review_research(research_results: list[dict]) -> dict:
    """Review research quality and provide actionable feedback."""

    if not research_results:
        return {
            "approved": False,
            "feedback": "No research results were provided. Research again.",
        }

    research_text = ""

    for result in research_results:
        research_text += (
            f"\nQuestion: {result.get('question', '')}\n"
            f"Summary: {result.get('summary', '')}\n"
        )

    prompt = f"""
    You are a careful research quality reviewer.

    Review the research below for relevance, coverage, and source links.

    Research:
    {research_text}

    Approve only if the research addresses the questions and includes
    useful evidence with source URLs. Do not claim that you independently
    verified sources.

    Return exactly one JSON object with these keys:
    "approved" (true or false)
    "feedback" (a short explanation of missing evidence or improvements)

    Example:
    {{"approved": true, "feedback": "Research covers the main questions."}}
    """

    response = llm.invoke(prompt)
    content = response.content

    if not isinstance(content, str):
        raise ValueError("The reviewer returned an unexpected response.")

    import json

    review = json.loads(content)

    if not isinstance(review.get("approved"), bool):
        raise ValueError("The review must include a boolean 'approved' value.")

    if not isinstance(review.get("feedback"), str):
        raise ValueError("The review must include string feedback.")

    return review
