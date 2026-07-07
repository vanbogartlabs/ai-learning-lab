from anthropic import Anthropic

from config.settings import ANTHROPIC_API_KEY


class ClaudeService:
    def __init__(self):
        self.client = Anthropic(api_key=ANTHROPIC_API_KEY)

    def ask(self, prompt: str) -> str:
        response = self.client.messages.create(
            model="claude-sonnet-5",
            max_tokens=1200,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return next(block.text for block in response.content if block.type == "text")
