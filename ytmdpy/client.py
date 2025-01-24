__all__ = (
    "Client",
)


from typing import (
    Any,
    Optional,
    overload,
)

from ytmdpy.enums import Command, RepeatMode
from ytmdpy.exceptions import AuthorizationError
from ytmdpy.http import HTTP


class Client:
    API_VERSION: str = "v1"

    def __init__(
        self,
        app_id: int,
        app_name: str,
        app_version: str,
    ) -> None:
        self.app_id = app_id
        self.app_name = app_name
        self.app_version = app_version
        self._token: Optional[str] = None
        self._authenticated = False
        self.http = HTTP(
            app_id=app_id,
            app_name=app_name,
            app_version=app_version,
        )

    async def _send_command(self, command: str, data: Any = None) -> dict:
        return await self.http.post(
            route=f"/api/{Client.API_VERSION}/command",
            json={"command": command, "data": data},
        )

    @overload
    async def authenticate(self, token: None = ...) -> tuple[int, str]:
        ...

    @overload
    async def authenticate(self, token: str = ...) -> None:
        ...

    async def authenticate(self, token: Optional[str] = None) -> Optional[tuple[int, str]] :
        if token:
            self._authenticated = True
            self._token = token
            self.http.base_headers["Authorization"] = token
            return

        auth_code_response = await self.http.post(
            route=f"/api/{Client.API_VERSION}/auth/requestcode",
        )
        auth_code = auth_code_response["code"]
        if auth_code == "AUTHORIZATION_DISABLED":
            raise AuthorizationError("Authorization is disabled on the server.")

        auth_request_response = await self.http.post(
            route=f"/api/{Client.API_VERSION}/auth/request",
            json={"code": auth_code},
        )
        auth_token = auth_request_response["token"]
        self._authenticated = True
        self._token = auth_token
        self.http.base_headers["Authorization"] = auth_token
        return (auth_code, auth_token)

    async def get_server_metadata(self) -> dict:
        return await self.http.get(
            route=f"/api/{Client.API_VERSION}/metadata",
        )

    async def get_state(self) -> dict:
        return await self.http.get(
            route=f"/api/{Client.API_VERSION}/state",
        )

    async def get_playlists(self) -> dict:
        return await self.http.get(
            route=f"/api/{Client.API_VERSION}/playlists",
        )

    async def toggle_playing(self) -> None:
        await self._send_command(Command.PLAY_PAUSE)

    async def play(self) -> None:
        await self._send_command(Command.PLAY)

    async def pause(self) -> None:
        await self._send_command(Command.PAUSE)

    async def volume_up(self) -> None:
        await self._send_command(Command.VOLUME_UP)

    async def volume_down(self) -> None:
        await self._send_command(Command.VOLUME_DOWN)

    async def set_volume(self, volume: int) -> None:
        await self._send_command(Command.SET_VOLUME)

    async def mute(self) -> None:
        await self._send_command(Command.MUTE)

    async def unmute(self) -> None:
        await self._send_command(Command.UNMUTE)

    async def seek_to(self, seconds: int) -> None:
        await self._send_command(Command.SEEK_TO, data=seconds)

    async def change_video(
        self,
        video_id: Optional[str] = None,
        playlist_id: Optional[str] = None,
    ) -> None:
        await self._send_command(
            command=Command.CHANGE_VIDEO,
            data={
                "video_id": video_id,
                "playlist_id": playlist_id,
            }
        )

    async def next(self) -> None:
        await self._send_command(Command.NEXT)

    async def previous(self) -> None:
        await self._send_command(Command.previous)

    async def repeat_mode(self, repeat_mode: RepeatMode) -> None:
        await self._send_command(Command.REPEAT_MODE, data=repeat_mode)

    async def shuffle(self) -> None:
        await self._send_command(Command.SHUFFLE)

    async def play_queue_index(self, index: int) -> None:
        await self._send_command(Command.PLAY_QUEUE_INDEX, data=index)

    async def toggle_like(self) -> None:
        await self._send_command(Command.TOGGLE_LIKE)

    async def toggle_dislike(self) -> None:
        await self._send_command(Command.TOGGLE_DISLIKE)
