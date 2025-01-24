__all__ = (
    "HTTP",
)


from typing import Any, Optional

from aiohttp import ClientSession


class HTTP:
    BASE_URL: str = "http://127.0.0.1:9863"

    def __init__(
        self,
        app_id: str,
        app_name: str,
        app_version: str,
        session: Optional[ClientSession] = None,
    ) -> None:
        self.app_id = app_id
        self.app_name = app_name
        self.app_version = app_version
        self._session = session or ClientSession()
        self.base_headers: dict[str, Any] = {}
        self.base_json: dict[str, Any] = {
            "appId": self.app_id,
            "appName": self.app_name,
            "appVersion": self.app_version,
        }

    async def get(
        self,
        route: str,
        headers: Optional[dict[str, str]] = None,
    ) -> dict[str, Any]:
        headers = headers or {}
        headers.update(self.base_headers)
        async with self._session.get(
            url=HTTP.BASE_URL + route,
            headers=headers,
        ) as response:
            response.raise_for_status()
            return await response.json()

    async def post(
        self,
        route: str,
        headers: Optional[dict[str, str]] = None,
        json: Optional[dict[str, str]] = None,
    ) -> dict[str, Any]:
        headers = headers or {}
        json = json or {}
        headers.update(self.base_headers)
        json.update(self.base_json)
        async with self._session.post(
            url=HTTP.BASE_URL + route,
            headers=headers,
            json=json,
        ) as response:
            response.raise_for_status()
            if await response.text() == "":
                return {}
            if response.headers.get("Content-Type", "").split(";")[0] == "application/json":
                return await response.json()
            return {}


