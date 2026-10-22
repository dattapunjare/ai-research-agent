
import json

from llm import llm


def plan_research(topic: str) -> list[str]:
    """Break a research topic into focused research questions."""

    prompt = f"""
    You are a research planning assistant.

    Topic: {topic}

    Create exactly 4 distinct research questions that together
    provide a useful overview of this topic.

    Cover:
    1. Background and key concepts
    2. Current developments
    3. Applications and real-world examples
    4. Challenges and future opportunities

    Return ONLY a valid JSON array of four strings.
    Example: ["Question 1", "Question 2", "Question 3", "Question 4"]
    """

    response = llm.invoke(prompt)
    content = response.content

    if not isinstance(content, str):
        raise ValueError("The planner returned an unexpected response.")

    content = content.strip()

    if content.startswith("```"):
        content = content.split("\n", 1)[1]
        content = content.rsplit("```", 1)[0].strip()

    questions = json.loads(content)

    if not isinstance(questions, list) or len(questions) != 4:
        raise ValueError("The planner must return exactly four questions.")

    if not all(isinstance(q, str) and q.strip() for q in questions):
        raise ValueError("Every research question must be a non-empty string.")

    return questions
