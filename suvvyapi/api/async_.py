import string
from random import choices
from typing import BinaryIO

import httpx

from suvvyapi.types.attachment import Attachment, input_to_attachments
from suvvyapi.types.enum import SuvvyMessageSender
from suvvyapi.types.exceptions import (
    InvalidToken, CustomChannelDisabled, InvalidFileType, NegativeBalance,
    ValidationError, SuvvyError
)
from suvvyapi.types.link import Link


class AsyncSuvvy(httpx.AsyncClient):
    """Asynchronous client for Suvvy AI API"""

    def __init__(
        self,
        token: str,
        *,
        base_url: str = "https://api.suvvy.ai",
    ) -> None:
        super().__init__(
            base_url=base_url,
            headers={"Authorization": f"Bearer {token}"},
            timeout=30,
        )

    async def send_message(
        self,
        chat_id: str,
        source: str,
        text: str | None = None,
        attachments: list[Attachment | str | tuple[str, bytes] | BinaryIO]
        | None = None,
        placeholders: dict[str, str] | None = None,
        link: Link | None = None,
        client_name: str | None = None,
        client_phone: str | None = None,
        message_sender: SuvvyMessageSender = SuvvyMessageSender.CUSTOMER,
        message_id: str | None = None,
    ) -> None:
        """Send message to Suvvy

        :param chat_id: Chat ID
        :param source: Source
        :param text: Message text. Required if attachments are not specified.
        :param attachments: Attachments. Required if text is not specified.
        :param placeholders: Instruction placeholders
        :param link: Link
        :param client_name: Client name
        :param client_phone: Client phone
        :param message_sender: Message sender (customer or employee)
        :param message_id: Message ID. Used to prevent repeated answers. Created randomly if not specified.
        """
        message_id = message_id or "".join(
            choices(string.ascii_letters + string.digits, k=10)
        )
        if text is None and not attachments:
            raise ValueError("Either text or attachments must be specified")

        response = await self.post(
            "/api/webhook/custom/message",
            json={
                "api_version": 1,
                "chat_id": chat_id,
                "source": source,
                "text": text,
                "attachments": [a.to_dict() for a in input_to_attachments(attachments)] if attachments else [],
                "placeholders": placeholders or {},
                "link": link.to_dict() if link is not None else None,
                "client_name": client_name,
                "client_phone": client_phone,
                "message_sender": message_sender.value,
                "message_id": message_id,
            },
        )

        match response.status_code:
            case 200:
                return
            case 401:
                raise InvalidToken
            case 424:
                raise CustomChannelDisabled
            case 415:
                raise InvalidFileType(f"Allowed types: {response.json()["allowed_mime_types"]}")
            case 402:
                raise NegativeBalance
            case 422:
                raise ValidationError(response.json())
            case _:
                raise SuvvyError(response.json())
