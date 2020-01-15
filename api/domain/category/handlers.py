from api.domain.abstracts import AbstractRepository, Event
from api.domain.category import models


async def create_changelog(event: Event, repo: AbstractRepository) -> None:
    entity = models.Category(**event.dict())
    await repo.add(entity)
