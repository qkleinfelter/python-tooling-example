# Tech Talk Demo Script

A step-by-step guide for demonstrating modern Python tooling.

## Pre-Demo Setup

1. Make sure you have a terminal ready
2. Have VS Code open with this project
3. Optional: Have a "before" project without tooling for comparison

## Part 1: Introduction to Modern Python Tooling (5 min)

### The Problem
- Traditional Python tooling is slow (pip, black, flake8, mypy)
- Configuration scattered across many files
- Setup is complex and time-consuming
- Developer experience is suboptimal

### The Solution
- **uv**: Fast package management (Rust-based)
- **Ruff**: Fast linting & formatting (Rust-based)
- **Pyright**: Feature-rich type checking (TypeScript-based)
- **pre-commit**: Automated quality checks
- **pyproject.toml**: Centralized configuration

## Part 2: UV Demo (10 min)

### Show Speed
```bash
# Compare with pip (if you have time)
# Or just show how fast uv is:
uv venv
# Should be near-instant

time uv sync --all-extras
# Should be very fast
```

### Show Dependency Management
```bash
# Add a dependency
uv add httpx

# Check pyproject.toml - it's updated!
cat pyproject.toml

# Remove it
uv remove httpx
```

### Run Code
```bash
uv run python -m python_tooling_example.main
```

**Talking Points:**
- "uv is 10-100x faster than pip"
- "Built-in dependency resolution"
- "Directly modifies pyproject.toml"
- "Python 3.12+ has great support"

## Part 3: Ruff Demo (10 min)

### Show Linting
```bash
# Lint the bad examples file
uv run ruff check src/python_tooling_example/bad_examples.py
```

**Show on screen:**
- Unused imports flagged
- Type annotation issues
- Code style issues
- Best practice violations

### Show Auto-Fix
```bash
# First, show what will be fixed
uv run ruff check --fix --diff src/python_tooling_example/bad_examples.py

# Then actually fix (on a copy if you want to preserve bad_examples.py)
uv run ruff check --fix src/python_tooling_example/utils.py
```

### Show Formatting
```bash
# Format the code
uv run ruff format src/python_tooling_example/utils.py
```

**Talking Points:**
- "Ruff replaces flake8, black, isort, pyupgrade, and more"
- "800+ lint rules available"
- "Can auto-fix most issues"
- "10-100x faster than traditional tools"

### Show Configuration
Open `pyproject.toml` and highlight the `[tool.ruff]` section:
- Line length settings
- Selected rule sets
- Per-file ignores

## Part 4: Pyright Demo (5 min)

### Show Type Checking
```bash
# Run type checker
uv run pyright
```

**Demonstrate:**
- How it catches type mismatches
- Missing return statements
- Incompatible assignments
- Rich type inference

### Show main.py
Walk through `src/python_tooling_example/main.py` and show:
- Properly typed functions
- Type annotations on classes and methods
- Modern type hints (list[str] vs List[str])

**Talking Points:**
- "Pyright is Microsoft's type checker with excellent VS Code integration"
- "Fast and feature-rich"
- "Supports standard, basic, and strict modes"
- "Configured via pyproject.toml"

## Part 5: Pre-commit Demo (5 min)

### Install Hooks
```bash
# Install pre-commit hooks
uv run pre-commit install
```

### Show Manual Run
```bash
# Run all hooks manually
uv run pre-commit run --all-files
```

### Make a Bad Commit
```bash
# Create a file with issues
echo "import sys\n\ndef bad_func( x,y ):\n    return x+y" > temp_bad.py

# Try to commit
git add temp_bad.py
git commit -m "Bad code"
```

**Show:** pre-commit automatically:
- Runs Ruff linting
- Runs Ruff formatting
- Runs other hooks (trailing whitespace, etc.)
- **Blocks the commit** if there are issues!

### Fix and Retry
```bash
# Ruff likely auto-fixed some issues
git add temp_bad.py
git commit -m "Fixed code"
```

**Talking Points:**
- "Prevents bad code from entering repository"
- "Runs automatically on git commit"
- "Can auto-fix many issues"
- "Team-wide consistency"

## Part 6: Configuration in pyproject.toml (5 min)

### Show pyproject.toml
Open and walk through:

1. **Project Metadata**
   ```toml
   [project]
   name = "python-tooling-example"
   version = "0.1.0"
   ```

2. **Tool Configurations**
   - `[tool.ruff]`
   - `[tool.pyright]`
   - `[tool.pytest.ini_options]` (for future)

**Talking Points:**
- "Single source of truth"
- "PEP 518/621 standard"
- "No more setup.py, setup.cfg, tox.ini, .flake8, etc."
- "More maintainable"

## Part 7: Putting It All Together (5 min)

### Typical Workflow Demo

1. **Make changes:**
   ```bash
   # Edit src/python_tooling_example/utils.py - add a new function
   ```

2. **Check locally:**
   ```bash
   uv run ruff check .
   uv run ruff format .
   uv run pyright
   ```
   VSCode editor integrations mean you can avoid these!

3. **Try to commit:**
   ```bash
   git add .
   git commit -m "Add new utility function"
   # pre-commit runs automatically!
   ```

4. **Push:**
   ```bash
   git push
   ```

## Conclusion (5 min)

### Benefits Summary
- ⚡ **Speed**: 10-100x faster tools
- 🎯 **Better DX**: Faster feedback, auto-fixes
- 📦 **Simplicity**: Fewer tools, one config file
- 🛡️ **Quality**: Catches issues before they're committed
- 🚀 **Modern**: Industry best practices

### What's Next?
- SQLAlchemy for database ORM
- Alembic for migrations
- pytest for testing
- FastAPI for web APIs
- Docker for deployment
- CI/CD integration

### Resources
- uv: https://github.com/astral-sh/uv
- Ruff: https://docs.astral.sh/ruff/
- Pyright: https://microsoft.github.io/pyright/
- pre-commit: https://pre-commit.com/

## Q&A Tips

**Common Questions:**

Q: "Is uv production-ready?"
A: "Yes! It's from Astral (creators of Ruff), used by many companies, 1.0 released."

Q: "Can I use this with existing projects?"
A: "Absolutely! Ruff can be adopted incrementally, uv is pip-compatible."

Q: "What about mypy?"
A: "Pyright is Microsoft's type checker with great VS Code integration. Mypy is also excellent. Both work with pyproject.toml."

Q: "Do I need all these tools?"
A: "Start with what helps most. Ruff alone is a huge improvement!"

Q: "Performance in large codebases?"
A: "These tools are optimized for large codebases - that's where they shine!"
