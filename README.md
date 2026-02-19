# Modern Python Tooling Demo

This repository demonstrates modern Python development tools and best practices, including:

- 🚀 **uv** - Lightning-fast Python package installer and resolver
- ⚡ **Ruff** - Extremely fast Python linter and formatter (replaces flake8, black, isort, and more)
- 🔍 **Pyright** - Fast, feature-rich type checker for Python
- 🪝 **pre-commit** - Git hooks for automated code quality checks

## Quick Start

### Installation

1. Install [uv](https://github.com/astral-sh/uv):
   ```bash
   # On Windows (PowerShell)
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

   # On macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv sync --all-extras
   ```

3. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

### Running the Demo

```bash
# Run the main module
python -m python_tooling_example.main

# Or use uv run
uv run python -m python_tooling_example.main
```

## Tool Overview

### 🚀 uv

[uv](https://github.com/astral-sh/uv) is a blazingly fast Python package installer and resolver, written in Rust. It's designed as a drop-in replacement for pip, pip-tools, and virtualenv.

**Key features:**
- 10-100x faster than pip
- Single dependency resolver
- Built-in virtual environment management
- Compatible with all pip features

**Common commands:**
```bash
uv venv                    # Create virtual environment
uv pip install package     # Install a package
uv sync                    # Install all project dependencies
uv add package             # Add a dependency to pyproject.toml
uv run python script.py    # Run a script in the uv environment
```

### ⚡ Ruff

[Ruff](https://github.com/astral-sh/ruff) is an extremely fast Python linter and formatter that can replace multiple tools (flake8, black, isort, pyupgrade, and more).

**Key features:**
- 10-100x faster than existing linters
- Supports 800+ lint rules
- Built-in formatter (replaces Black)
- Auto-fixes for many issues
- Configuration via pyproject.toml

**Common commands:**
```bash
ruff check .              # Lint all files
ruff check --fix .        # Lint and auto-fix issues
ruff format .             # Format all files
ruff check --watch .      # Watch mode for development
```

**Configuration:** See `[tool.ruff]` in [pyproject.toml](pyproject.toml)

### 🔍 Pyright

[Pyright](https://github.com/microsoft/pyright) is a fast, feature-rich type checker for Python from Microsoft.

**Key features:**
- Fast type checking written in TypeScript/Node.js
- Rich type inference
- Excellent VS Code integration
- Supports standard, basic, and strict type checking modes
- Configuration via pyproject.toml

**Common commands:**
```bash
pyright                   # Type check all files
pyright src/              # Type check specific directory
pyright --watch           # Watch mode
```

**Configuration:** See `[tool.pyright]` in [pyproject.toml](pyproject.toml)

### 🪝 pre-commit

[pre-commit](https://pre-commit.com/) is a framework for managing git pre-commit hooks, ensuring code quality before commits.

**Key features:**
- Automatic code quality checks before commits
- Supports multiple languages and tools
- Easy configuration
- Prevents bad commits

**Common commands:**
```bash
pre-commit install           # Install hooks
pre-commit run --all-files   # Run all hooks manually
pre-commit autoupdate        # Update hook versions
```

**Configuration:** See [.pre-commit-config.yaml](.pre-commit-config.yaml)

## Project Structure

```
.
├── src/
│   └── python_tooling_example/    # Main package
│       ├── __init__.py            # Package initialization
│       ├── main.py                # Demo code showcasing tooling
│       ├── utils.py               # Utility functions with type hints
│       └── bad_examples.py        # Intentionally broken code for demos
├── pyproject.toml                 # Project configuration and tool settings
├── .pre-commit-config.yaml        # Pre-commit hooks configuration
├── UV_COMMANDS.md                 # Quick reference for uv commands
├── DEMO_SCRIPT.md                 # Step-by-step presentation guide
└── README.md                      # This file
```

## Tool Configuration

All tool configurations are centralized in [pyproject.toml](pyproject.toml), following modern Python best practices:

- **Ruff**: Linting rules, formatting options
- **Pyright**: Type checking strictness and options
- **pytest**: Test configuration (for future use)

## Development Workflow

1. Make code changes
2. Run formatters and linters:
   ```bash
   ruff format .
   ruff check --fix .
   pyright
   ```
3. Or simply try to commit - pre-commit will run all checks automatically!
   ```bash
   git add .
   git commit -m "Your message"
   ```

## Why These Tools?

**Speed**: Modern tools like uv, Ruff, and Pyright are designed for performance and developer experience.

**Developer Experience**: Faster feedback loops, better error messages, and automatic fixes mean less time fighting tools and more time coding.

**All-in-One Configuration**: Everything is configured in `pyproject.toml`, following PEP standards and reducing configuration files.

**Industry Adoption**: These tools are rapidly becoming the standard in modern Python development.

## Resources

- [uv Documentation](https://github.com/astral-sh/uv)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Pyright Documentation](https://microsoft.github.io/pyright/)
- [pre-commit Documentation](https://pre-commit.com/)

## License

MIT
