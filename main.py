
from pathlib import Path

from graph import research_graph


def main() -> None:
    topic = input("Enter a research topic: ").strip()

    if not topic:
        print("Please enter a research topic.")
        return

    initial_state = {
        "topic": topic,
        "research_questions": [],
        "research_results": [],
        "review_feedback": "",
        "review_count": 0,
        "final_report": "",
        "approved": False,
    }

    print("\nResearch team is working. Please wait...\n")

    try:
        result = research_graph.invoke(initial_state)

        report = result.get("final_report", "")

        if not report:
            print("No report was generated.")
            return

        output_dir = Path("reports")
        output_dir.mkdir(exist_ok=True)

        safe_topic = "".join(
            char if char.isalnum() or char in "-_" else "_"
            for char in topic
        )[:60]

        report_path = output_dir / f"{safe_topic or 'research_report'}.md"
        report_path.write_text(report, encoding="utf-8")

        print("Research completed!")
        print(f"Report saved to: {report_path.resolve()}")
        print("\n--- Report Preview ---\n")
        print(report[:3000])

        if len(report) > 3000:
            print("\n... (open the Markdown file to read the full report)")

    except Exception as error:
        print(f"\nResearch failed: {error}")
        print("Check your API keys, internet connection, and terminal output.")


if __name__ == "__main__":
    main()
