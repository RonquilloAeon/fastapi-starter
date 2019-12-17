import abc
from typing import Any, List, Union


class Entity(abc.ABCMeta):
    ref: Union[bool, None] = None

    def __hash__(self) -> int:
        return hash(self.ref)

    @abc.abstractmethod
    def __repr__(self) -> str:
        pass


# See https://github.com/cosmicpython/code/blob/chapter_06_aggregate_exercise/src/allocation/repository.py
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

    def __init_subclass__(cls, model: Entity, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.model = model

    def add(self, entity: Entity) -> None:
        self.session.add(entity)

    def get(self, reference: Any) -> Entity:
        return self.session.query(self.model).filter_by(reference=reference).one()

    def list(self) -> List[Entity]:
        return self.session.query(self.model).all()
