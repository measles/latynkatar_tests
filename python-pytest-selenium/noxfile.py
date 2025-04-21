import nox

nox.options.sessions = ["pytest"]


@nox.session(venv_backend="none")
def pytest(session):
    session.run("python3", "-m", "pytest", "--showlocals", "--html=report.html", "--self-contained-html", "--verbose", "tests/")
