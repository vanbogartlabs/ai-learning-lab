# CLAUDE.md

This file provides guidance to Claude Code when working in the `valleyforge` project.

## Project state

ValleyForge is an early-stage AI Co-Founder Platform. Currently a single CLI flow:
it takes a business idea from the user and asks Claude to produce a structured
validation report (problem, target customer, value proposition, revenue model,
competition, risks, MVP, score).

## Commands

Uses [`uv`](https://docs.astral.sh/uv/) for dependency and environment management
(Python >=3.14).

- Run the app: `uv run app.py`
- Add a dependency: `uv add <package>`
- Sync the environment from the lockfile: `uv sync`

There is no test suite, linter, or build step configured yet.

## Architecture

- `app.py` — entry point. `main()` prompts for a business idea and prints the
  report returned by `analyze_idea()`, which calls `ClaudeService.ask()`.
- `services/claude_service.py` — `ClaudeService` wraps the Anthropic SDK client
  and exposes `ask(prompt) -> str`.
- `config/settings.py` — loads `.env` via `python-dotenv` and exposes
  `ANTHROPIC_API_KEY`; raises at import time if the key is missing.
- `.env` — holds `ANTHROPIC_API_KEY`; gitignored, never commit it.
