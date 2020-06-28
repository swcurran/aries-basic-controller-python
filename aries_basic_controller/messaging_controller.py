from .base_controller import BaseController
from aiohttp import ClientSession
import logging
import base64

logger = logging.getLogger("messaging")

class MessagingController(BaseController):

    def __init__(self, admin_url: str, client_session: ClientSession):
        super().__init__(admin_url, client_session)


    def default_handler(self, payload):
        logger.debug("Message Recieved ", payload)

    async def send_message(self, connection_id, msg):
        response = await self.admin_POST(f"/connections/{connection_id}/send-message", {
            "content": msg,
        })
        return response

    async def trust_ping(self, connection_id: str, msg: str):
        response = await self.admin_POST(f"/connections/{connection_id}/send-ping", {"content": msg})
        return response
