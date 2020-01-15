from pydantic import BaseModel


class CategoryInSchema(BaseModel):
    name: str

    class Config:
        orm_mode: True


class CategorySchema(CategoryInSchema):
    id: int
