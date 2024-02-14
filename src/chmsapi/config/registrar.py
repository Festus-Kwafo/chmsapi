from fastapi import FastAPI

from chmsapi.api.routers import v1
from chmsapi.config.settings import settings
from chmsapi.utilities.health_check import ensure_unique_route_names
from chmsapi.utilities.openapi import simplify_operation_ids
from fastapi_pagination import add_pagination


def register_app():
    app = FastAPI(
        title=settings.TITLE,
        version=settings.VERSION,
        description=settings.DESCRIPTION,
        docs_url=settings.DOCS_URL,
        redoc_url=settings.REDOCS_URL,
        openapi_url=settings.OPENAPI_URL,

    )
    register_router(app)
    register_middleware(app)
    add_pagination(app)

    return app


def register_router(app: FastAPI):
    """
    :param app: FastAPI
    :return:
    """
    # API
    app.include_router(v1)

    # Extra
    ensure_unique_route_names(app)
    simplify_operation_ids(app)


def register_middleware(app: FastAPI):
    if settings.MIDDLEWARE_ACCESS:
        from chmsapi.middleware.access_middleware import AccessMiddleware

        app.add_middleware(AccessMiddleware)

    # CORS: Always at the end
    if settings.MIDDLEWARE_CORS:
        from fastapi.middleware.cors import CORSMiddleware

        app.add_middleware(
            CORSMiddleware,
            allow_origins=['*'],
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*'],
        )
