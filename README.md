# python-template

A minimal Python project template with [uv](https://docs.astral.sh/uv/), strict typing (basedpyright), linting (ruff), and pytest.

## Prerequisites

- **Python 3.13.5** — match `.python-version` (pyenv or similar is recommended)
- **[just](https://github.com/casey/just)** — command runner for common workflows (`brew install just`, or see [installation](https://github.com/casey/just#installation))
- **uv** — not required upfront; `just install` installs the pinned version from `.uv-version` if uv is missing

## Quick start

Clone the repo, install dependencies, and run tests:

```bash
git clone <repo-url>
cd python-template
just install
just test
```

Run `just` with no arguments to list all recipes. Tests do not require a `.env` file.

## Configuration (`.env`)

Runtime settings live in a `.env` file at the project root (gitignored). Values are loaded by [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) — see `src/config/types.py` for the schema.

Create `.env` before running `just dev`:

```dotenv
OPENAI_API_KEY=your-key-here
# optional; defaults to gpt-4o-mini
DEFAULT_MODEL=gpt-4o-mini
```

Environment variable names use uppercase with underscores; they map to the snake_case fields on `Config` (e.g. `openai_api_key` → `OPENAI_API_KEY`).

## Templating a new project

When starting a new repo from this template, rename or update at least:

| Location | What to change |
| --- | --- |
| `pyproject.toml` | `name`, `description`, and any project metadata |
| `src/main.py` | Entry-point message and application logic |
| `src/config/types.py` | Config fields for your service |
| `README.md` | Project name, setup notes, and links |

Keep the justfile, lint/type-check config, and test layout unless your project needs different tooling.
