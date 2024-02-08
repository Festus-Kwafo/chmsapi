from datetime import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel

from src.chmsapi.config.settings import settings


class CustomCodeBase(Enum):
    """Custom code base class"""

    @property
    def code(self):
        """
        Get the status code
        """
        return self.value[0]

    @property
    def msg(self):
        """
        Get the status code information
        """
        return self.value[1]


class CustomResponseCode(CustomCodeBase):
    "" "Custom Response Status Code" "" "" "" "" "" ""

    Http_200 = (200, 'request success')
    Http_201 = (201, 'new request successful ')
    Http_202 = (202, 'The request has been accepted, but the processing has not been completed')
    Http_204 = (204, 'The request was successful, but the content was not returned')
    Http_400 = (400, 'request error')
    Http_401 = (401, 'Unauthorized')
    Http_403 = (403, 'Forbidden access')
    Http_404 = (404, 'The resource of request does not exist')
    Http_410 = (410, 'The request resources have been permanently deleted')
    Http_422 = (422, 'request parameters illegal')
    Http_425 = (425, 'cannot execute the request, because the server cannot meet the requirements')
    Http_429 = (429, 'Excessive requests, server limit')
    Http_500 = (500, 'Internal error of the server')
    Http_502 = (502, 'gateway error')
    Http_503 = (503, 'The server cannot handle the request for the time being')
    Http_504 = (504, 'gateway timeout')


class CustomErrorCode(CustomCodeBase):
    """Custom error status code"""

    CAPTCHA_ERROR = (40001, 'Verification code error')


class ResponseModel(BaseModel):
    """
    统一返回模型

    .. tip::

        如果你不想使用 ResponseBase 中的自定义编码器，可以使用此模型，返回数据将通过 fastapi 内部的编码器自动解析并返回；
        此返回模型会生成 openapi schema 文档

    E.g. ::

        @router.get('/test', response_model=ResponseModel)
        def test():
            return ResponseModel(data={'test': 'test'})

        @router.get('/test')
        def test() -> ResponseModel:
            return ResponseModel(data={'test': 'test'})

        @router.get('/test')
        def test() -> ResponseModel:
            res = CustomResponseCode.HTTP_200
            return ResponseModel(code=res.code, msg=res.msg, data={'test': 'test'})
    """  # noqa: E501

    code: int = CustomResponseCode.Http_200.code
    msg: str = CustomResponseCode.Http_200.msg
    data: Any | None = None

    class Config:
        json_encoders = {datetime: lambda x: x.strftime(settings.DATETIME_FORMAT)}
