import asyncio
import asyncpg
import pytest
from contextlib import asynccontextmanager
from migri import run_initialization, run_migrations
from starlette.testclient import TestClient
from typing import Generator

from application import app
from config import Config

config = Config()
TEST_DATABASE_URL = config.DATABASE_URL.replace(config.DATABASE_URL.path, "")
TEST_DB_NAME = config.DATABASE_URL.path.replace("/", "")


@asynccontextmanager
async def db_conn(database_url: str) -> Generator[asyncpg.Connection, None, None]:
    conn = await asyncpg.connect(database_url)

    try:
        yield conn
    finally:
        await conn.close()


async def run_db_statement(statement: str) -> None:
    async with db_conn(f"{TEST_DATABASE_URL}/postgres") as conn:
        await conn.execute(statement)


async def set_up_db() -> None:
    async with db_conn(config.DATABASE_URL) as conn:
        await run_initialization(conn, force_close_conn=False)
        await run_migrations("api/migrations", conn)


def pytest_configure(config) -> None:
    asyncio.run(run_db_statement(f"CREATE DATABASE {TEST_DB_NAME}"))
    asyncio.run(set_up_db())


def pytest_unconfigure(config) -> None:
    asyncio.run(run_db_statement(f"DROP DATABASE {TEST_DB_NAME}"))


@pytest.yield_fixture
def test_client() -> Generator[TestClient, None, None]:
    asyncio.set_event_loop(asyncio.new_event_loop())

    with TestClient(app) as client:
        yield client
