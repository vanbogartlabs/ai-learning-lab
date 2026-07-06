# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project state

This is an early-stage learning project scaffolded with `uv`. It currently contains only a placeholder `main.py`. Expect the structure and purpose to evolve as work is added — re-check this file's assumptions against the actual code before relying on them.

## Commands

This project uses [`uv`](https://docs.astral.sh/uv/) for dependency and environment management (Python >=3.14).

- Run the app: `uv run main.py`
- Add a dependency: `uv add <package>`
- Sync the environment from the lockfile: `uv sync`

There is no test suite, linter, or build step configured yet.

## Architecture

- `main.py` — entry point, currently a single `main()` function.
- `pyproject.toml` — project metadata and dependencies (currently just `openai`).
- `uv.lock` — locked dependency versions; regenerate via `uv sync` / `uv add`, don't hand-edit.
