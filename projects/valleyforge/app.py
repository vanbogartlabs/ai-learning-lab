from services.claude_service import ClaudeService

REPORT_PROMPT = """You are evaluating a startup idea. Analyze the following \
business idea and produce a validation report with these sections:

1. Problem - What painful, expensive, or annoying problem does this solve?
2. Target Customer - Who would pay for this? Be specific.
3. Value Proposition - Why would someone choose this instead of doing nothing?
4. Revenue Model - How could this make money?
5. Competition - Who already solves this problem?
6. Risks - What could make this fail?
7. MVP - What is the smallest useful version we could build?
8. Score - Score this idea from 1-10 with a one-sentence justification.

Business idea:
{idea}
"""


def analyze_idea(idea: str) -> str:
    claude = ClaudeService()
    return claude.ask(REPORT_PROMPT.format(idea=idea))


def main():
    print("AI Business Idea Validator")
    print("==========================")
    idea = input("Enter your business idea: ")

    report = analyze_idea(idea)
    print(report)


if __name__ == "__main__":
    main()
