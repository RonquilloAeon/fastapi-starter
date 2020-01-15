from fastapi import APIRouter

from api.application.category import serializers
from api.application.versioning import version, VersionedRoute

router = APIRouter(route_class=VersionedRoute)


@router.post("", status_code=201)  # response_model=serializers.CategorySchema,
@version("2019", "12", "07")
async def create_category(cat: serializers.CategoryInSchema):
    return {}
