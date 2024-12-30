from dataclasses import dataclass
from typing import Literal


@dataclass
class Link:
    """Link"""
    url: str
    hint: str | None = None
    type: Literal["user", "chat", "phone", "lead", "other"] = "other"

    def to_dict(self) -> dict:
        return {
            "url": self.url,
            "hint": self.hint,
            "type": self.type
        }
