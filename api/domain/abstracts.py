import abc
from contextlib import asynccontextmanager
from pydantic import BaseModel
from sqlalchemy.orm.session import Session
from typing import Any, Callable, ContextManager, List, Union


class Entity(BaseModel):
    pass


class Event(BaseModel):
    pass


# See https://git.io/Jebn5
class AbstractRepository(abc.ABCMeta):
    @abc.abstractmethod
    def add(self, entity: Entity) -> None:
        pass

    @abc.abstractmethod
    def get(self, reference: Any) -> Entity:
        pass


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session) -> None:
        super().__init__()
        self.session = session

    def __init_subclass__(cls, entity: Entity, entity_name: str, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.entity_name = entity_name
        setattr(cls, entity_name, entity)

    def _get_entity(self) -> Entity:
        return getattr(self, self.entity_name)

    def add(self, entity: Entity) -> None:
        self.session.add(entity)

    def get(self, reference: Any) -> Entity:
        return self.session.query(self._get_entity())\
            .filter_by(reference=reference).one()

    def list(self) -> List[Entity]:
        return self.session.query(self._get_entity()).all()


@asynccontextmanager
async def pgsql_unit_of_work(session_factory: Callable) -> ContextManager:
    transaction = await session_factory()

    try:
        yield transaction
    finally:
        transaction.rollback()  # Has no effect if user commits


# @asynccontextmanager
# async def pgsql_unit_of_work(
#     session_factory: Callable[[], Session]
# ) -> ContextManager[Session]:
#     session = await session_factory()
#
#     try:
#         yield session
#     finally:
#         session.rollback()  # Has no effect if user commits
#         session.close()
