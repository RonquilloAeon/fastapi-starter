from domain import abstracts


class Category:
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"<Category {self.name}>"


class PgSQLRepository:
    def __init__(self, session) -> None:
        super().__init__()
        self.session = session

    def __init_subclass__(cls, entity, entity_name, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.entity_name = entity_name
        setattr(cls, entity_name, entity)

    def _get_entity(self):
        return getattr(self, self.entity_name)

    def add(self, entity) -> None:
        self.session.add(entity)

    def get(self, reference):
        return self.session.query(self._get_entity())\
            .filter_by(reference=reference).one()

    def list(self):
        return self.session.query(self._get_entity()).all()


class CategoryRepository(
    abstracts.SqlAlchemyRepository,
    entity=Category,
    entity_name="category"
):
    pass


class UnitOfWork:
    def __init__(self, session_factory) -> None:
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()  # type: Session
        self.products = CategoryRepository()
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()


async def create_category_service(name: str, uow) -> None:
    async with uow:
        uow.add(Category(name))
        uow.commit()
