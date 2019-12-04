import nox


@nox.session(python="3.8", reuse_venv=True)
def test(session):
    session.install("-r", "test-requirements.txt")
    session.run("pytest", "--cov=work", *session.posargs)
