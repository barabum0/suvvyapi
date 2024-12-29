import base64
import string
from dataclasses import dataclass
from random import choices
from typing import Literal, BinaryIO

import magic

MIME_TO_EXTENSION: dict[str, str] = {
    "audio/ogg": "ogg",
    "audio/mpeg": "mp3",
    "audio/mp4": "mp4",
    "audio/wav": "wav",
    "audio/webm": "webm",
    "audio/x-wav": "wav",
    "audio/m4a": "m4a",
    "audio/x-m4a": "m4a",
    "image/png": "png",
    "image/jpeg": "jpeg",
    "image/gif": "gif",
}


@dataclass
class Attachment:
    """Attachment"""
    file_name: str
    file_type: Literal["image", "audio"]
    data: str
    message_id: str


def determine_attachment_type(mybytes: bytes) -> Literal["image", "audio"]:
    mime_type = magic.from_buffer(mybytes, mime=True)
    if mime_type in ["image/png", "image/jpeg", "image/gif"]:
        return "image"
    elif mime_type in ["audio/ogg", "audio/mpeg", "audio/wav", "audio/x-wav", "audio/webm", "audio/mp4", "audio/m4a", "audio/x-m4a"]:
        return "audio"
    else:
        raise ValueError("Invalid file type")


def determine_extension(mybytes: bytes) -> str:
    mime_type = magic.from_buffer(mybytes, mime=True)
    return MIME_TO_EXTENSION[mime_type]


def input_to_attachments(input_list: list[Attachment | str | tuple[str, bytes] | BinaryIO]) -> list[Attachment]:
    attachments: list[Attachment] = []
    for a in input_list:
        if isinstance(a, Attachment):
            attachments.append(a)
        elif isinstance(a, str):
            with open(a, "rb") as file:
                data = file.read()
                attachments.append(
                    Attachment(
                        file_name=file.name,
                        file_type=determine_attachment_type(data),
                        data=base64.b64encode(data).decode("utf-8"),
                        message_id="".join(choices(string.ascii_letters + string.digits, k=10))
                    )
                )
        elif isinstance(a, tuple):
            if not isinstance(a[0], str) or not isinstance(a[1], bytes):
                raise ValueError("Invalid attachment")

            attachments.append(
                Attachment(
                    file_name=a[0],
                    file_type=determine_attachment_type(a[1]),
                    data=base64.b64encode(a[1]).decode("utf-8"),
                    message_id="".join(choices(string.ascii_letters + string.digits, k=10))
                )
            )
        elif isinstance(a, BinaryIO):
            data = a.read()
            attachments.append(
                Attachment(
                    file_name=a.name or "unknown",
                    file_type=determine_attachment_type(data),
                    data=base64.b64encode(data).decode("utf-8"),
                    message_id="".join(choices(string.ascii_letters + string.digits, k=10))
                )
            )
        else:
            raise ValueError("Invalid attachment")
    return attachments
