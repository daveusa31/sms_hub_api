import typing
import aiohttp

from . import types
from . import exceptions


class SmsHub:
    """
    Официальная документация: http://sms-area.org/api/ru/documentation.html
    Репозитортй на github.com: https://github.com/daveusa31/sms_area_api

    Доступные методы:
        balance
        get_activation_list
        get_activation_status
    """

    API_URL = "https://smshub.org/stubs/handler_api.php"

    def __init__(self, api_key: str):
        self.api_key = api_key

    async def _request(self, method: str, action: str, params=None, response_in="dict") -> typing.Union[str, dict]:
        if params is None:
            params = {}

        params = dict(
            api_key=self.api_key,
            action=action,
            **params
        )
        async with aiohttp.ClientSession() as session:
            response: aiohttp.ClientResponse
            async with getattr(session, method)(self.API_URL, params=params) as response:

                if "dict" == response_in:
                    _response = await response.json(content_type=None)
                else:
                    _response = await response.text()

        return _response

    async def _get(self, action, **kwargs):
        return await self._request("get", action, **kwargs)

    def _check_result(self, text: str):
        if "BAD_KEY" == text:
            raise exceptions.InvalidToken
        if "NO_NUMBERS" == text:
            raise exceptions.NoNumbers
        if "NO_ACTIVATION" == text:
            raise exceptions.NoActivation

    async def get_balance(self) -> float:
        response = await self._get("getBalance", response_in="text")
        self._check_result(response)
        return float((response).split(":")[1])

    async def get_numbers_status(self, country=None, operator=None):
        params = {}
        if country is not None:
            params["country"] = country
        if operator is not None:
            params["operator"] = operator

        return await self._get("getNumbersStatus", params=params)

    async def get_number(self, service, operator=None, country=None) -> types.Activation:
        params = {"service": service}
        if country is not None:
            params["country"] = country
        if operator is not None:
            params["operator"] = operator

        response = await self._get("getNumber", params=params, response_in="text")
        self._check_result(response)
        activation_id: int = int(response.split(":")[1])
        number: int = int(response.split(":")[2])
        return types.Activation(activation_id, number=number)

    async def set_status(self, activation_id, status):
        return await self._get("setStatus", params={"id": activation_id, "status": status}, response_in="text")

    async def get_status(self, activation_id: typing.Union[str, int]):
        response = await self._get("getStatus", params={"id": activation_id}, response_in="text")
        self._check_result(response)
        return response

    async def get_prices(self, service=None, country=None):
        params = {}
        if service is not None:
            params["service"] = service

        if country is not None:
            params["country"] = country

        return await self._get("getPrices", params=params)
