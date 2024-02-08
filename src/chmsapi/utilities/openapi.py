from fastapi import FastAPI
from fastapi.routing import APIRoute


def custom_generate_unique_id(route: APIRoute):
    return f"{route.name}"


def simplify_operation_ids(app: FastAPI) -> None:
    """
    Simplify the operating ID so that the client to generate a simpler API function name
    :param app:
    :return:
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name
