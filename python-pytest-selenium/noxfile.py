"""Main nox file for the project"""

import nox

nox.options.sessions = ["pytest"]


@nox.session(venv_backend="none")
def pytest(session):
    """Test execution in current environment"""
    session.run(
        "python3",
        "-m",
        "pytest",
        "--showlocals",
        "--html=report.html",
        "--self-contained-html",
        "--verbose",
        "tests/",
    )


@nox.session(tags=("lint",))
def isonv(session):
    """Sort import for a grate good"""
    session.install("isort")
    session.run("isort", "noxfile.py", "tests", "lib")


@nox.session(tags=("lint",))
def black(session):
    """Apply black code stile for style and code quility"""
    session.install("black")
    session.run("black", "noxfile.py", "tests", "lib")


@nox.session(tags=("lint",))
def pylint(session):
    """Check code with pilint"""
    session.install(
        "pylint",
        "nox",
        "pytest",
        "pytest_randomly",
        "pytest_html",
        "selenium",
        "pyperclip",
    )
    session.run("pylint", "lib", "tests/", "noxfile.py")


@nox.session(tags=("lint",))
def flake8(session):
    """flacke8 tests for a code quality"""
    session.install("flake8", "flake8-pyproject")
    session.run("flake8", ".", "--count", "--exclude", ".nox,.venv")


@nox.session(tags=("lint",))
def mypy(session):
    """Check types definitions with mypy"""
    session.install(
        "mypy", "nox", "pytest_randomly", "pytest_html", "selenium", "pyperclip"
    )
    session.run("mypy", "--install-types")
    session.run("mypy", "noxfile.py")
    session.run("mypy", "lib")
    session.run("mypy", "tests/")
