"""Nox sessoins."""
from nox_poetry import Session
from nox_poetry import session

locations = "f1pystats", "tests", "noxfile.py", "docs/conf.py"
python_versions = ['3.11', '3.12', '3.13']


@session(python=python_versions[-1])
def lint(session: Session) -> None:
    """Runs linting for the package."""
    args = session.posargs or locations
    session.install("flake8",
                    "flake8-black",
                    "flake8-import-order",
                    "flake8-bugbear",
                    "flake8-annotations",
                    "flake8-docstrings",
                    "darglint")
    session.run("flake8", *args)


@session(python=python_versions)
def mypy(session: Session) -> None:
    """Runs type checking the package."""
    args = session.posargs or locations
    session.install("mypy",
                    "types-requests",
                    "numpy",
                    "pytest",
                    "nox_poetry",
                    "types-toml")
    session.run("mypy", *args)


@session(python=python_versions)
def tests(session: Session) -> None:
    """Run all tests."""
    session.install("pytest",
                    "requests",
                    "pandas")
    session.run("pytest")


@session(python=python_versions[-1])
def code_coverage(session: Session) -> None:
    """Run package coverage."""
    session.install("pytest",
                    "pytest-cov",
                    "requests",
                    "pandas")
    session.run("pytest", "--cov", "--cov-report=lcov")


@session(python=python_versions[-1])
def docs(session: Session) -> None:
    """Build the documentation."""
    session.install("sphinx",
                    "sphinx-autodoc-typehints",
                    "furo",
                    "toml")
    session.run("sphinx-build", "-M", "html", "docs", "docs/_build")
