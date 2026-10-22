
from llm import llm


def write_report(topic: str, research_results: list[dict]) -> str:
    """Write a structured report using the collected research."""

    research_text = ""

    for result in research_results:
        research_text += (
            f"\n## Research question: {result.get('question', '')}\n"
            f"{result.get('summary', '')}\n"
        )

    prompt = f"""
    You are a professional research report writer.

    Write a clear, well-organized report about: {topic}

    Use the research notes below:
    {research_text}

    Requirements:
    1. Include a title and executive summary.
    2. Organize the main findings with useful headings.
    3. Include challenges and future opportunities.
    4. Cite sources using the URLs provided in the research notes.
    5. Do not invent sources, facts, statistics, or URLs.
    6. Mention limitations or missing evidence when relevant.
    7. Finish with a conclusion and a list of source links.
    8. Use Markdown formatting.

    Return only the report in Markdown.
    """

    response = llm.invoke(prompt)
    content = response.content

    if not isinstance(content, str) or not content.strip():
        raise ValueError("The writer did not return a valid report.")

    return content
