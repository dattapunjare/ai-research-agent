# AI Research Team

An AI-powered research assistant built with **Python, LangGraph, Google Gemini, and Tavily**. It automates the research process by generating research questions, searching the web, reviewing findings, and producing a structured Markdown report with source links.

## Features

- **Research Planning:** Generates four focused questions based on the user's topic.
- **Web Research:** Uses Tavily to collect relevant web search results.
- **Research Review:** Evaluates research relevance, coverage, and source availability.
- **Feedback Loop:** Repeats research when the review does not approve the findings, up to the configured review limit.
- **Report Generation:** Uses Google Gemini to create a detailed Markdown report.
- **Source References:** Includes source URLs to help readers verify research claims.
- **Report Export:** Saves the generated report as a Markdown file in the `reports/` directory.

## Tech Stack

- **Python** — Core programming language
- **LangGraph** — Research workflow orchestration
- **Google Gemini** — AI-powered planning, review, and writing
- **Tavily** — Web search and research retrieval
- **uv** — Python project and dependency management
- **python-dotenv** — Environment variable management

## How It Works

1. **Planner:** Creates four research questions from the given topic.
2. **Researcher:** Searches the web for each question.
3. **Reviewer:** Evaluates the collected research and provides feedback.
4. **Research Loop:** Repeats research if necessary, within the configured review limit.
5. **Writer:** Generates a structured research report in Markdown.
6. **Export:** Saves the final report to the `reports/` directory.

## Project Structure

```text
ai-research-agent/
├── agents/
│   ├── __init__.py
│   ├── approval.py
│   ├── planner.py
│   ├── researcher.py
│   ├── reviewer.py
│   └── writer.py
├── src/
│   └── ai_research_agent/
│       └── __init__.py
├── .env.example
├── .gitignore
├── .python-version
├── config.py
├── graph.py
├── llm.py
├── main.py
├── pyproject.toml
├── README.md
├── state.py
├── tools.py
└── uv.lock
```

## Requirements

- Python version compatible with `.python-version`
- [uv](https://docs.astral.sh/uv/)
- Google Gemini API key
- Tavily API key
- Internet connection

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/dattapunjare/ai-research-agent.git
cd ai-research-agent
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Configure environment variables

Copy `.env.example` to `.env`.

On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Open `.env` and add your own API keys:

```env
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
MODEL=gemini-2.5-flash
MAX_REVIEWS=2
```

**Security:** Never commit or upload your `.env` file. Keep API keys private.

### 4. Run the project

```bash
uv run python main.py
```

Enter a research topic when prompted, for example:

```text
AI agents in healthcare
```

The application will start the research workflow and generate a report.

## Output

Generated reports are saved in the `reports/` directory as Markdown files.

Example:

```text
reports/
└── AI_agents_in_healthcare_.md
```

Open the `.md` file in VS Code to read the full report. You can also use **Ctrl + Shift + V** to preview its Markdown formatting.

## Environment Variables

| Variable | Purpose |
|---|---|
| `GOOGLE_API_KEY` | Authenticates requests to Google Gemini |
| `TAVILY_API_KEY` | Authenticates web searches |
| `MODEL` | Specifies the Gemini model |
| `MAX_REVIEWS` | Configures the review limit |

## Limitations

- Research quality depends on the search results and AI-generated analysis.
- Source links should be opened and checked before relying on claims.
- The workflow does not guarantee that every claim is accurate.
- API access and usage may be subject to provider limits and costs.

## Future Improvements

- Parallel research across multiple questions
- Improved report formatting with a clickable table of contents
- Stronger source verification and citation handling
- Human approval before final report generation
- PDF report export
- Automated tests and improved error handling


