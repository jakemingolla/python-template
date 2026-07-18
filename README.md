# python-template

A minimal Python project template with [uv](https://docs.astral.sh/uv/), strict typing (basedpyright), linting (ruff), and pytest.

## Prerequisites

- **Python 3.13.5** — match `.python-version` (pyenv or similar is recommended)
- **[just](https://github.com/casey/just)** — runs the common workflows below (`brew install just`, or see [installation](https://github.com/casey/just#installation))
- **uv** — not required upfront; `just install` installs the pinned version from `.uv-version` if uv is missing

## Quick start

Clone the repo, install dependencies, and run tests:

```bash
git clone <repo-url>
cd python-template
just install
just test
```

Tests do not require a `.env` file.

## Recipes

| Recipe | Description |
| --- | --- |
| `just install` | Install dependencies (`uv sync --frozen`) |
| `just test` | Run unit and integration tests |
| `just test-unit` | Run tests in `test/unit/` |
| `just test-integration` | Run tests in `test/integration/` |
| `just test-only` | Run tests marked with `only` |
| `just lint` | Run ruff and basedpyright |
| `just format` | Format code with ruff |
| `just dev` / `just run` | Run the app (`python -m src.main`) |
| `just` | List all recipes |

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
