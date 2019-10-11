from datetime import datetime
from fastapi.routing import APIRoute
from re import fullmatch
from starlette.requests import Request
from starlette.responses import Response

from starlette.routing import Match


class VersionedRoute(APIRoute):
    VERSION_HEADER_NAME = 'fsg-plaid-version'

    def get_version(self, scope):
        version_header = list(
            filter(lambda h: h[0] == bytes(self.VERSION_HEADER_NAME, 'utf-8'), scope.get('headers', []))
        )

        if len(version_header) > 0:
            requested_version = version_header[0][1]
            version_check = fullmatch(
                r'^([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))$',
                requested_version.decode('utf-8')
            )

            if version_check:
                target_version = version_check.string
                # TODO debug log
                return target_version

        # Resort to latest
        # TODO find way to retrieve latest version
        return datetime.now().strftime('%Y-%m-%d')

    def matches(self, scope):
        version = self.get_version(scope)
        match, child_scope = super().matches(scope)

        if match != Match.NONE:
            if self.endpoint.__api_version__ <= int(version.replace('-', '')):
                child_scope.update({'api_version': version})
                return match, child_scope

        return Match.NONE, {}

    def get_route_handler(self):
        original_handler = super().get_route_handler()

        async def versioned_route_handler(request: Request) -> Response:
            oh = await original_handler(request)
            oh.headers[self.VERSION_HEADER_NAME] = request.scope['api_version']

            return oh

        return versioned_route_handler


def version(year: str, month: str, day: str):
    """Add version to a path operation function"""
    def decorator(func):
        func.__api_version__ = int(f'{year}{month}{day}')
        return func

    return decorator
