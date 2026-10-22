
from tools import search_web


def research_question(question: str) -> dict:
    """Research one question using web search."""

    results = search_web(question)

    return {
        "question": question,
        "sources": results,
        "summary": (
            "\n\n".join(
                f"Source: {item['title']}\n"
                f"URL: {item['url']}\n"
                f"Content: {item['content']}"
                for item in results
            )
            if results
            else "No relevant search results were found."
        ),
    }
