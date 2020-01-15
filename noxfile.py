import nox


@nox.session(python="3.8", reuse_venv=True)
def dev(session):
    """For creating a development virtual environment. Handy for setting interpreter in
    IDE.
    """
    session.install("-r", "test-requirements.txt")


@nox.session(python="3.8", reuse_venv=True)
def format(session):
    session.install("black")
    session.run("black", "api")


@nox.session(python="3.8", reuse_venv=True)
def check(session):
    session.install("flake8")
    session.run("flake8", "api")


@nox.session(python="3.8", reuse_venv=True)
def test(session):
    session.install("-r", "test-requirements.txt")
    session.run(
        "pytest",
        "--cov=api",
        *session.posargs,
        env={
            "DATABASE_URL": "postgresql://turbo:passpass@localhost:5432/test_apidb",
            "TESTING": "true"
        }
    )
