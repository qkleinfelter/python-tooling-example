# UV Commands Demo

This document shows common `uv` commands for the tech talk demo.

## Setup Commands

```bash
# Install uv (if not already installed)
# Windows (PowerShell):
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS/Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Project Initialization

```bash
# Create a new project
uv init my-project

# Create a virtual environment
uv venv

# Activate the virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

## Dependency Management

```bash
# Install all project dependencies from pyproject.toml
uv sync

# Install with optional dependencies
uv sync --all-extras

# Add a new dependency
uv add requests

# Add a development dependency
uv add --dev pytest

# Add a specific version
uv add "pydantic>=2.0.0"

# Remove a dependency
uv remove requests

# Update all dependencies
uv lock --upgrade

# Install a package (like pip install)
uv pip install numpy

# Install from requirements.txt
uv pip install -r requirements.txt
```

## Running Code

```bash
# Run a script in the uv environment
uv run python main.py

# Run a module
uv run -m pytest

# Run with inline dependencies (no venv needed!)
uv run --with httpx python script.py
```

## Tool Integration

```bash
# Run ruff via uv
uv run ruff check .
uv run ruff format .

# Run ty via uv
uv run ty .

# Run pre-commit via uv
uv run pre-commit run --all-files
```

## Speed Comparison Demo

```bash
# Time uv vs pip installation (for demo)
# Create two fresh environments and time them:

# With pip:
time (python -m venv venv-pip && venv-pip/bin/pip install requests pandas numpy)

# With uv:
time (uv venv venv-uv && uv pip install requests pandas numpy)

# uv is typically 10-100x faster!
```

## Useful Flags

```bash
# Show what would be installed without installing
uv sync --dry-run

# Sync only production dependencies (no dev)
uv sync --no-dev

# Force reinstall
uv sync --reinstall

# Verbose output
uv sync -v

# Very verbose (debug)
uv sync -vv
```

## Why uv?

**Speed**: Written in Rust, 10-100x faster than pip
**Correctness**: Better dependency resolution
**Simplicity**: Replaces pip, pip-tools, virtualenv, and more
**Modern**: Built with modern Python packaging standards

## Comparison with Traditional Tools

| Task | Traditional | uv |
|------|-------------|-----|
| Install package | `pip install requests` | `uv pip install requests` |
| Create venv | `python -m venv .venv` | `uv venv` |
| Add dependency | Edit requirements.txt + pip install | `uv add requests` |
| Sync deps | `pip install -r requirements.txt` | `uv sync` |
| Lock dependencies | `pip-compile` | `uv lock` |
