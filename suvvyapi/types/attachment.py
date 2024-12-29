from dataclasses import dataclass
from typing import Literal


@dataclass
class Attachment:
    """Attachment"""
    file_name: str
    file_type: Literal["image", "audio"]
    data: str
    message_id: str
