
import os

from dotenv import load_dotenv

load_dotenv()


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

MODEL = os.getenv("MODEL", "gemini-2.5-flash")

MAX_REVIEWS = int(os.getenv("MAX_REVIEWS", "2"))


if not GOOGLE_API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY is missing. Add it to your .env file."
    )

if not TAVILY_API_KEY:
    raise ValueError(
        "TAVILY_API_KEY is missing. Add it to your .env file."
    )

