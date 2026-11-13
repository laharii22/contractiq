
import os
from pathlib import Path

from dotenv import load_dotenv
from anthropic import (
    Anthropic,
    AuthenticationError,
    RateLimitError,
    APIConnectionError,
    APIStatusError,
)


# Find the main ContractIQ project folder
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Load environment variables from the project's .env file
load_dotenv(PROJECT_ROOT / ".env")


def create_client() -> Anthropic:
    """Create an authenticated Anthropic API client."""

    api_key = os.getenv("ANTHROPIC_API_KEY")

    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY was not found in .env")

    return Anthropic(api_key=api_key)



def send_test_message(prompt: str) -> str:
    """Send a prompt to Claude and return its text response."""

    client = create_client()

    try:
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=100,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.content[0].text

    except AuthenticationError as error:
        raise RuntimeError("Invalid Anthropic API key.") from error

    except RateLimitError as error:
        raise RuntimeError("Anthropic API rate limit exceeded.") from error

    except APIConnectionError as error:
        raise RuntimeError("Could not connect to Anthropic API.") from error

    except APIStatusError as error:
        raise RuntimeError(
            f"Anthropic API returned status {error.status_code}."
        ) from error

