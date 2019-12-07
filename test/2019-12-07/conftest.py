import pytest

API_VERSION = "2019-12-07"


@pytest.fixture
def version_header() -> dict:
    return {"api-version": API_VERSION}
