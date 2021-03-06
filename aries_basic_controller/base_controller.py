from aiohttp import (
    web,
    ClientSession,
    ClientRequest,
    ClientResponse,
    ClientError,
    ClientTimeout,
)

import asyncio
import logging

import json

from .utils import log_msg

EVENT_LOGGER = logging.getLogger("event")

class repr_json:
    def __init__(self, val):
        self.val = val

    def __repr__(self) -> str:
        if isinstance(self.val, str):
            return self.val
        return json.dumps(self.val, indent=4)


class BaseController:

    def __init__(self, admin_url: str, client_session):
        self.admin_url = admin_url
        self.client_session = client_session
        self.color = None
        self.prefix = None

    def log(self, *msg, **kwargs):
        self.handle_output(*msg, **kwargs)

    @property
    def prefix_str(self):
        if self.prefix:
            return f"{self.prefix:10s} |"

    def handle_output(self, *output, source: str = None, **kwargs):
        end = "" if source else "\n"
        if source == "stderr":
            color = "fg:ansired"
        elif not source:
            color = self.color or "fg:ansiblue"
        else:
            color = None
        log_msg(*output, color=color, prefix=self.prefix_str, end=end, **kwargs)


    async def admin_request(
        self, method, path, data=None, text=False, params=None
    ) -> ClientResponse:
        params = {k: v for (k, v) in (params or {}).items() if v is not None}
        async with self.client_session.request(
            method, self.admin_url + path, json=data, params=params
        ) as resp:
            resp.raise_for_status()
            resp_text = await resp.text()
            if not resp_text and not text:
                return None
            if not text:
                try:
                    return json.loads(resp_text)
                except json.JSONDecodeError as e:
                    raise Exception(f"Error decoding JSON: {resp_text}") from e
            return resp_text


    async def admin_GET(self, path, text=False, params=None) -> ClientResponse:
        try:
            EVENT_LOGGER.debug("Controller GET %s request to Agent", path)
            response = await self.admin_request("GET", path, None, text, params)
            EVENT_LOGGER.debug(
                "Response from GET %s received: \n%s", path, repr_json(response),
            )
            return response
        except ClientError as e:
            self.log(f"Error during GET {path}: {str(e)}")
            raise

    async def admin_POST(
            self, path, data=None, text=False, params=None
    ) -> ClientResponse:
        try:
            EVENT_LOGGER.debug(
                "Controller POST %s request to Agent%s",
                path,
                (" with data: \n{}".format(repr_json(data)) if data else ""),
            )
            response = await self.admin_request("POST", path, data, text, params)
            EVENT_LOGGER.debug(
                "Response from POST %s received: \n%s", path, repr_json(response),
            )
            return response
        except ClientError as e:
            self.log(f"Error during POST {path}: {str(e)}")
            raise


